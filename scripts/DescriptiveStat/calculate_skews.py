import pandas as pd
import matplotlib.pyplot as plt

PATH_TO_COCK = '../../interim/DescriptiveStat/codonusage_table_cock.csv'
PATH_TO_TERM = '../../interim/DescriptiveStat/codonusage_table_term.csv'

# we're using the light strand but descript the heavy one, so every nucleotide is inverted

def get_skew_df(codon_table):
    codon_table = pd.read_csv(codon_table)

    GAskew = (codon_table['nC'] - codon_table['nT'])/(codon_table['nC'] + codon_table['nT'])
    TCskew = (codon_table['nG'] - codon_table['nA'])/(codon_table['nG'] + codon_table['nA'])
    Stg_Sac = (codon_table['neutralC'] + codon_table['neutralA']) - (codon_table['neutralT'] + codon_table['neutralG'])
    IDs = codon_table['Species_name']
    genes = codon_table['Gene_name']

    skews = IDs.to_frame().merge(GAskew.rename('GAskew'), left_index=True, right_index=True)
    skews = skews.merge(genes.rename('Gene_name'), left_index=True, right_index=True)
    skews = skews.merge(TCskew.rename('TCskew'), left_index=True, right_index=True)
    skews = skews.merge(Stg_Sac.rename('Stg-Sac'), left_index=True, right_index=True)

    return (skews)


cock_skew = get_skew_df(PATH_TO_COCK)
term_skew = get_skew_df(PATH_TO_TERM)


Organism = pd.Series(["Cockroach"]*len(cock_skew))
cock_skew = cock_skew.merge(Organism.rename('Organism'), left_index=True, right_index=True)

Organism = pd.Series(["Termite"]*len(term_skew))
term_skew = term_skew.merge(Organism.rename('Organism'), left_index=True, right_index=True)


skews = pd.concat([cock_skew, term_skew])
skews.to_csv("../../interim/DescriptiveStat/cock_term_skews.csv", na_rep='NA')


#cock_skew.to_csv("../../interim/DescriptiveStat/cock_skew.csv", na_rep='NA')
#term_skew.to_csv("../../interim/DescriptiveStat/term_skew.csv", na_rep='NA')
