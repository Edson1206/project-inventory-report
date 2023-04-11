import csv
import json
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    def import_csv(path):
        data = []
        with open(path, encoding="utf8") as file:
            path_csv = csv.DictReader(file)
            for row in path_csv:
                data.append(row)
        return data

    def import_json(path):
        with open(path) as file:
            path_json = json.load(file)
            return path_json

    @classmethod
    def import_data(cls, path, type):
        data = []
        if path.endswith(".csv"):
            data = Inventory.import_csv(path)
        if path.endswith(".json"):
            data = Inventory.import_json(path)

        if type == "simples":
            return SimpleReport.generate(data)
        if type == "completo":
            return CompleteReport.generate(data)
