from Bio import SeqIO

# Separate IDs to single files (extracting only protein sequence)

#fin = "../../raw/blattodea_genbank/new/Cockroach_complete_genome_refseq.gb"
fin = "../../raw/blattodea_genbank/new/Termites_complete_genome_refseq.gb"


for entry in SeqIO.parse(fin, 'gb'):
    for feat in entry.features:
        if feat.type == 'CDS':
            if 'gene' in feat.qualifiers:
                with open(f"../../interim/ForDolphin/separate_ids_term/{entry.id}_{feat.qualifiers['gene'][0]}.faa", "w") as fout:
                    fout.write(f">{entry.id} [{entry.description}]\n{feat.qualifiers['translation'][0]}")

