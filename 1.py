class Report:
    """
    Клас відповідає за управління даними звіту.
    """
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def get_report_data(self):
        return f"Title: {self.title}\nContent: {self.content}"


class ReportPrinter:
    """
    Клас відповідає за друк звіту.
    """
    def print_report(self, report):
        print("Printing Report...")
        print(report.get_report_data())


class ReportSaver:
    """
    Клас відповідає за збереження звіту у файл.
    """
    def save_report(self, report, filename):
        with open(filename, 'w') as file:
            file.write(report.get_report_data())
        print(f"Report saved to {filename}")


# Використання
report = Report("Monthly Sales", "Sales increased by 15% this month.")
printer = ReportPrinter()
saver = ReportSaver()

# Друк звіту
printer.print_report(report)

# Збереження звіту у файл
saver.save_report(report, "monthly_sales.txt")
