import csv
import json
import xmltodict
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory():
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

    def import_xml(path):
        response = []
        with open(path) as file:
            read_file = file.read()
            file_xml = xmltodict.parse(read_file)
            for value in file_xml['dataset']['record']:
                response.append(value)
            return response

    @classmethod
    def import_data(cls, path, type):
        data = []
        if path.endswith(".csv"):
            data = Inventory.import_csv(path)
        if path.endswith(".json"):
            data = Inventory.import_json(path)
        if path.endswith(".xml"):
            data = Inventory.import_xml(path)

        if type == "simples":
            return SimpleReport.generate(data)
        else:
            return CompleteReport.generate(data)
