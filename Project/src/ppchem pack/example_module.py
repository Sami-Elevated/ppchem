"Source Code"
import re
import streamlit as st
from rdkit import Chem
from rdkit.Chem import AllChem
from rdkit.Chem.Descriptors import ExactMolWt, MolLogP, NumHDonors, NumHAcceptors
from stmol import showmol
import py3Dmol
from pathlib import Path
import pandas as pd
import os
from streamlit_ketcher import st_ketcher
from rdkit.Chem import rdFingerprintGenerator
import numpy as np
import mols2grid
import streamlit.components.v1 as components
import plotly.figure_factory as ff
from typing import Tuple, List
def name_to_smile():
   pass

def det_m_solvent(amount_solvent):
   prefixes=['g','L']
   if any(p in amount_solvent for p in prefixes):
      for i in amount_solvent:
         if amount_solvent.isdigit() is False:
            return 
   else: 
     return False
   

def m_products():
   pass
    

def det_total_masses(m_chemicals): #calculates the total masses of reactant(s), solvent(s) and product(s) in THAT ORDER
    total_masses=[]
    for chemical in m_chemicals:
       tot_mass=0
       for m_chemical in chemical:
          tot_mass+=m_chemical
       total_masses.append(tot_mass)
    return total_masses

def E_factor(total_masses,wanted_m_product): #calculates the e factor using the list of lists and the wanted amount of product(s)
   waste=total_masses[0]-total_masses[3]+total_masses[2]
   e_factor=waste/wanted_m_product
   return e_factor
