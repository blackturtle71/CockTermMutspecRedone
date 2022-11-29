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

    skews = IDs.to_frame().merge(GAskew.rename('GAskew'), left_index=True, right_index=True)
    skews = skews.merge(TCskew.rename('TCskew'), left_index=True, right_index=True)
    skews = skews.merge(Stg_Sac.rename('Stg-Sac'), left_index=True, right_index=True)

    return skews


cock_skew = get_skew_df(PATH_TO_COCK)
term_skew = get_skew_df(PATH_TO_TERM)


GAskew_bp = plt.boxplot([cock_skew['GAskew'], term_skew['GAskew']], patch_artist = True, notch ='True',)
colors = ['#74B72E', '#466D1D']
for patch, color in zip(GAskew_bp['boxes'], colors):
    patch.set_facecolor(color)
plt.xticks([1, 2], ['Cockroaches', 'Termites'])
plt.ylabel('GA skew')
plt.savefig('../../figures/GAskew.PDF', format='pdf')
plt.clf()

TCskew_bp = plt.boxplot([cock_skew['TCskew'], term_skew['TCskew']], patch_artist = True, notch ='True',)
for patch, color in zip(TCskew_bp['boxes'], colors):
    patch.set_facecolor(color)
plt.xticks([1, 2], ['Cockroaches', 'Termites'])
plt.ylabel('TC skew')
plt.savefig('../../figures/TCskew.PDF', format='pdf')
plt.clf()

Stg_Sac_bp = plt.boxplot([cock_skew['Stg-Sac'], term_skew['Stg-Sac']], patch_artist = True, notch ='True',)
for patch, color in zip(Stg_Sac_bp['boxes'], colors):
    patch.set_facecolor(color)
plt.xticks([1, 2], ['Cockroaches', 'Termites'])
plt.ylabel('Stg-Sac')
plt.savefig('../../figures/Stg-Sac.PDF', format='pdf')