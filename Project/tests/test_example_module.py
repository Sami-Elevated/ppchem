#from ppchem pack.example_module import hello_smiles


# Test the function


def det_total_masses(m_chemicals): #calculates the total masses of reactants, solvents and products in THAT ORDER
    total_masses=[]
    for chemical in m_chemicals:
       tot_mass=0
       for m_chemical in chemical:
          tot_mass+=m_chemical
       total_masses.append(tot_mass)
    return total_masses

x=[[1,2,3],[1,2,3,4],[1,2,3,7]]
print(det_total_masses(x))