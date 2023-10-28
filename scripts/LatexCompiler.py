import os
from scripts.Globals import check_folder


def latex_compiler() -> None:
    """
    Compile a LaTeX file to generate a PDF report.

    This function compiles a LaTeX file, 'DataReport.tex,' to generate a PDF report. It does the compilation twice to ensure
    the Table of Contents is generated properly.

    The generated PDF report is saved in the 'output' directory.

    Example usage:
    latex_compiler()

    Note: The function assumes that the LaTeX source file ('DataReport.tex') is located in the 'scripts' directory,
    and it will change the working directory to 'output' where the PDF output is saved.
    """

    print("Compiling Latex File...")

    # Checking whether 'output' folder exists, if not then create 'output' folder
    check_folder('output')

    # Changing directory to where output files of latex compilation will be generated
    os.chdir('output')

    # Compiling Latex file - Doing twice to generate Contents table properly
    os.system("pdflatex ../scripts/DataReport.tex > NUL 2>&1")
    os.system("pdflatex ../scripts/DataReport.tex > NUL 2>&1")

    print("Done")


if __name__ == "__main__":
    latex_compiler()
