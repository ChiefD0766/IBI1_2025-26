import xml.dom.minidom
import xml.sax
from xml.sax import ContentHandler
import datetime

def dom_analyze_go(xml_path):
    """DOM Parsing: Find the GO term with the maximum is_a count in each of the three main ontologies"""
    # Initialize results for three ontologies
    results = {
        "molecular_function": {"id": "", "name": "", "max_is_a": 0},
        "biological_process": {"id": "", "name": "", "max_is_a": 0},
        "cellular_component": {"id": "", "name": "", "max_is_a": 0}
    }

    # Load XML file
    dom_tree = xml.dom.minidom.parse(xml_path)
    terms = dom_tree.getElementsByTagName("term")

    for term in terms:
        # Extract GO term ID
        id_node = term.getElementsByTagName("id")[0]
        go_id = id_node.firstChild.nodeValue

        # Extract term name (handle line breaks/special characters)
        name_node = term.getElementsByTagName("name")[0]
        go_name = name_node.firstChild.nodeValue.strip()

        # Extract ontology namespace
        ns_node = term.getElementsByTagName("namespace")[0]
        namespace = ns_node.firstChild.nodeValue.strip()

        # Count is_a relationships for current term
        is_a_list = term.getElementsByTagName("is_a")
        is_a_count = len(is_a_list)

        # Only process the three target ontologies
        if namespace in results:
            # Update the maximum is_a record for this ontology
            if is_a_count > results[namespace]["max_is_a"]:
                results[namespace]["id"] = go_id
                results[namespace]["name"] = go_name
                results[namespace]["max_is_a"] = is_a_count

    return results

class GOContentHandler(ContentHandler):
    """SAX Handler: Parse XML line by line and count is_a in real time"""
    def __init__(self):
        # Initialize results
        self.results = {
            "molecular_function": {"id": "", "name": "", "max_is_a": 0},
            "biological_process": {"id": "", "name": "", "max_is_a": 0},
            "cellular_component": {"id": "", "name": "", "max_is_a": 0}
        }
        self.current_id = ""
        self.current_name = ""
        self.current_namespace = ""
        self.current_is_a_count = 0

        self.in_term = False
        self.in_id = False
        self.in_name = False
        self.in_namespace = False

    def startElement(self, name, attrs):
        """Triggered when a start tag is encountered"""
        if name == "term":
            self.in_term = True
            # Reset data for new term
            self.current_id = ""
            self.current_name = ""
            self.current_namespace = ""
            self.current_is_a_count = 0
        elif name == "id" and self.in_term:
            self.in_id = True
        elif name == "name" and self.in_term:
            self.in_name = True
            self.current_name = ""
        elif name == "namespace" and self.in_term:
            self.in_namespace = True
        elif name == "is_a" and self.in_term:
            self.current_is_a_count += 1
    def characters(self, content):
        """Triggered when text content is encountered"""
        if self.in_id:
            self.current_id += content.strip()
        elif self.in_name:
            self.current_name += content
        elif self.in_namespace:
            self.current_namespace += content.strip()

    def endElement(self, name):
        """Triggered when an end tag is encountered"""
        if name == "term":
            self.in_term = False
            # Update results when term parsing ends
            ns = self.current_namespace
            if ns in self.results:
                if self.current_is_a_count > self.results[ns]["max_is_a"]:
                    self.results[ns]["id"] = self.current_id
                    self.results[ns]["name"] = self.current_name.strip()
                    self.results[ns]["max_is_a"] = self.current_is_a_count
        elif name == "id":
            self.in_id = False
        elif name == "name":
            self.in_name = False
        elif name == "namespace":
            self.in_namespace = False

def sax_analyze_go(xml_path):
    """SAX Parsing main function"""
    handler = GOContentHandler()
    parser = xml.sax.make_parser()
    parser.setContentHandler(handler)
    parser.parse(xml_path)
    return handler.results

if __name__ == "__main__":
    XML_FILE = "go_obo.xml"

    # Run DOM parsing and measure time
    print("DOM Parsing Results")
    start_dom = datetime.datetime.now()
    dom_results = dom_analyze_go(XML_FILE)
    end_dom = datetime.datetime.now()
    dom_time = (end_dom - start_dom).total_seconds()

    # Print DOM results
    for ns, info in dom_results.items():
        print(f"Ontology: {ns}")
        print(f"  GO ID: {info['id']}")
        print(f"  Name: {info['name']}")
        print(f"  Maximum is_a count: {info['max_is_a']}\n")
    print(f"DOM parsing time: {dom_time:.4f} seconds\n")

    # Run SAX parsing and measure time
    print("SAX Parsing Results")
    start_sax = datetime.datetime.now()
    sax_results = sax_analyze_go(XML_FILE)
    end_sax = datetime.datetime.now()
    sax_time = (end_sax - start_sax).total_seconds()

    # Print SAX results
    for ns, info in sax_results.items():
        print(f"Ontology: {ns}")
        print(f"  GO ID: {info['id']}")
        print(f"  Name: {info['name']}")
        print(f"  Maximum is_a count: {info['max_is_a']}\n")
    print(f"SAX parsing time: {sax_time:.4f} seconds\n")

    # Conclusion: SAX parsing is faster