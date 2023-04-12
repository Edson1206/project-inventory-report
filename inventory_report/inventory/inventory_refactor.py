from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class InventoryRefactor:
    def __init__(self, importer):
        self.importer = importer
        self.data = []

    def import_data(self, path: str, type: str):
        inventory_data = self.importer.import_data(path)
        self.data.extend(inventory_data)

        if type == "simples":
            return SimpleReport.generate(inventory_data)
        if type == "completo":
            return CompleteReport.generate(inventory_data)
