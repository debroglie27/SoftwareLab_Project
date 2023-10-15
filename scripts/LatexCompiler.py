import os


def latex_compiler():
    # Creating Output Folder if not present
    if not os.path.exists('output'):
        os.makedirs('output')

    os.chdir('output')
    # Generate Report
    os.system("pdflatex ../scripts/DataReport.tex > NUL 2>&1")
    os.system("pdflatex ../scripts/DataReport.tex > NUL 2>&1")


if __name__ == "__main__":
    latex_compiler()
