import os


def latex_compiler():
    # Creating output Folder if not present
    if not os.path.exists('output'):
        os.makedirs('output')

    # Changing directory to where output files of latex compilation will be generated
    os.chdir('output')

    # Compiling Latex file - Doing twice to generate Contents table properly
    os.system("pdflatex ../scripts/DataReport.tex > NUL 2>&1")
    os.system("pdflatex ../scripts/DataReport.tex > NUL 2>&1")


if __name__ == "__main__":
    latex_compiler()
