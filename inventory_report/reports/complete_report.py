from collections import Counter
from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @classmethod
    def generate(self, productList):
        simple_report_result = SimpleReport.generate(productList)
        list_companies = Counter(
            [row["nome_da_empresa"] for row in productList]
        )
        complete_report_result = ""
        for company, quantity in list_companies.items():
            complete_report_result += f"- {company}: {quantity}\n"
        return (
            f"{simple_report_result}\n"
            f"Produtos estocados por empresa:\n"
            f"{complete_report_result}"
        )
