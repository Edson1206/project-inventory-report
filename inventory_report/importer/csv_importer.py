import csv

from inventory_report.importer.importer import Importer


class CsvImporter(Importer):
    @classmethod
    def import_data(self, path):
        if path.endswith(".csv"):
            with open(path, "r", encoding="utf-8") as file:
                path_csv = list(csv.DictReader(file))
            return path_csv
        raise ValueError("Arquivo inválido")
