"""Preprocessing Functions"""
from typing import Union
import regex as re


######################################################
# Check the length of HLA
######################################################
def _hla_length_filter(hla: str) -> str:
    """
    Ensuring that the HLA does not have more specificity than Allel level
    by truncating on the fisrt colon. HLA-Gene*Allel:protein
    Parameters
    ----------
    hla : string
        HLA molecule string
    Notes
    -----
    In nomenclature HLA's could have more long specificities
    http://hla.alleles.org/nomenclature/naming.html
    Raises
    ------
    ValueError
    Examples
    --------
    >>> _hla_length_filter('DRB1*13:01:01')
    'DRB1*13:01'
    """

    if not set([":", "*"]).issubset(set(hla)):
        raise ValueError("HLA is not accoring to the expected format")

    colon_location = [m.start() for m in re.finditer(":", hla)]
    colon_number = len(colon_location)
    if colon_number > 1:
        colon_second = colon_location[1]
        hla = hla[0:colon_second]
    return hla


######################################################
# List of sets or set of sets to set
######################################################
def _return_set(input_set: Union[str, set]) -> set:
    """
    Returns a set of strings from a set with all its child sets.
    Parameters
    ----------
    hla : string
        path to the file
    Examples
    --------
    >>> _return_set({{'a'}, {'b','c'}, {'d'}} or [{'a'}, {'b','c'}, {'d'}] )
    {'a', 'b', 'c', 'd' }
    """

    return {value for sub_set in input_set for value in sub_set}
