from collections import Counter
from datetime import datetime


class SimpleReport:
    @classmethod
    def generate(self, productList: list):
        return (
            f"Data de fabricação mais antiga: "
            f"{self.oldest_manufacturing_date(productList)}\n"
            f"Data de validade mais próxima: "
            f"{self.closest_expiration_date(productList)}\n"
            f"Empresa com mais produtos: "
            f"{self.company_more_products(productList)}"
        )

    def oldest_manufacturing_date(productList):
        manufacturing_date = [row["data_de_fabricacao"] for row in productList]
        return min(manufacturing_date)

    def closest_expiration_date(productList):
        expire_date = [
            row["data_de_validade"]
            for row in productList
            if row["data_de_validade"] >= str(datetime.today())
        ]
        return min(expire_date)

    def company_more_products(productList):
        companies_list = [row["nome_da_empresa"] for row in productList]
        return Counter(companies_list).most_common()[0][0]
