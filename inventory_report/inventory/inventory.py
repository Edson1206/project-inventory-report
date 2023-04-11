import csv
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

    @classmethod
    def import_data(cls, path, type):
        data = []
        if path.endswith(".csv"):
            data = Inventory.import_csv(path)

        if type == "simples":
            return SimpleReport.generate(data)
        if type == "completo":
            return CompleteReport.generate(data)
