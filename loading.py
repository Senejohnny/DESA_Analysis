"""
Loading operations
"""

import sys
import pandas as pd

print(sys.path)
# print(__name__)


def load_epitope_db(path: str) -> pd.DataFrame:
    """
    path: abs path to the Epitope DB
    """
    # Load different sheets from excel file & concatenate all vertically
    df_1 = pd.read_excel(path, sheet_name="ABC")
    df_2 = pd.read_excel(path, sheet_name="DRB1")
    df_3 = pd.read_excel(path, sheet_name="DQB1")
    return pd.concat([df_1, df_2, df_3])


def _load_hla(path: str) -> pd.DataFrame:
    """
    Internal function to just load HLA data
    """
    hla = pd.read_excel(path)
    hla = hla.rename(
        columns={
            "RecipientHLAType_PROCAREorNMDP": "Recipient_HLA",
            "DonorHLAType_PROCAREorNMDP": "Donor_HLA",
        }
    )
    return hla


def _load_mfi(path: str) -> pd.DataFrame:
    """
    Load the Mean Flourescent Information file.
    Parameters
    ----------
    path : string
        path to the file
    """

    mfi = pd.read_csv(path, sep=";")
    mfi["Specificity"] = mfi["Specificity"].apply(lambda x: set(x.split(",")))
    mfi = mfi.drop(
        [
            "SampleID",
            "CatalogID",
            "Gate_LUM",
            "Analyte_LUM",
            "MedianFI",
            "TMeanFI",
            "Probe77_MedianFI",
            "Probe77_TMeanFI",
            "CON1_MedianFI",
            "CON1_TMeanFI",
        ],
        axis=1,
    )
    return mfi
