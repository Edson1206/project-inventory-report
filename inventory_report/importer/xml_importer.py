import xmltodict

from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    @classmethod
    def import_data(self, path):
        with open(path, "r", encoding="utf-8") as file:
            if path.endswith(".xml"):
                read_file = xmltodict.parse(file.read())
                response = read_file["dataset"]["record"]
                return response
            raise ValueError("Arquivo inválido")
