import os


def latex_compiler():
    # Creating Output Folder if not present
    if not os.path.exists('output'):
        os.makedirs('output')

    os.chdir('output')
    # Generate Report
    os.system("pdflatex ../scripts/DataReport.tex")
    os.system("pdflatex ../scripts/DataReport.tex")


if __name__ == "__main__":
    latex_compiler()
