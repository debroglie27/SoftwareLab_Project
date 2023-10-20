import os
from scripts.globals import check_folder


def latex_compiler():
    check_folder('output')

    # Changing directory to where output files of latex compilation will be generated
    os.chdir('output')

    # Compiling Latex file - Doing twice to generate Contents table properly
    os.system("pdflatex ../scripts/DataReport.tex > NUL 2>&1")
    os.system("pdflatex ../scripts/DataReport.tex > NUL 2>&1")


if __name__ == "__main__":
    latex_compiler()
