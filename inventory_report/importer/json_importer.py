import json

from inventory_report.importer.importer import Importer


class JsonImporter(Importer):
    @classmethod
    def import_data(self, path):
        with open(path, "r", encoding="utf-8") as file:
            if path.endswith(".json"):
                path_json = json.load(file)
                return path_json
            raise ValueError("Arquivo inválido")
