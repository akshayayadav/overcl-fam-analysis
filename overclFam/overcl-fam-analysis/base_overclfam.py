class BasePath:
    outpath = "/home/aayadav/research/overcl-fam-analysis/lgf5/"
    outgroup_fasta_filename = "/data/orthofinder_legumes/02_proteomes_outgroup/orthofinder_legumes_outgroups.fa"
    family_fasta_filedir = "/data/orthofinder_legumes/orthofinder_legumes_family_fasta/"
    species_profile_filename = "/home/aayadav/research/overcl-fam-analysis/legume.profile"

    # for workflow directly processing rooted family trees
    rooted_famtrees_dir = "/data/lgf5/56_trees_combined/"

    phmmer_executable = "phmmer"
    mafft_executable = "mafft"
    raxml_executable = "raxmlHPC-PTHREADS-AVX"
    fasttree_executable = "FastTreeMP"
    hmmbuild_executable = "hmmbuild"
    hmmsearch_executable = "hmmsearch"

    fasta_database_fileextension = "_db.fa"
    phmmertlbout_fileextension = ".phmmertlbout"
    seqlist_fileextension = ".seqlist"
    fam_outgrp_fasta_fileextension = "_outgroup_sequences.fa"
    msa_outfileextension = "_outgroup_sequences.fa.msa"
    msa_famoutfileextension = ".msa"
    raxml_tree_fileprefix = "RAxML_bestTree."
    fasttree_fileextension = ".fasttree"
    rooted_fasttree_fileextension = ".rooted_fasttree"
    tree_score_fileextension = ".tree_score"
    clade_fileextension = ".ingroup_monophyletic_clades"
    hmm_fileextension = ".hmm"
    hmmsearch_fileextension = ".hmmsearch"

    def print_base_paths(self):
        print 'Output path : {0}'.format(self.outpath)
        print 'Outgroup proteomes : {0}'.format(self.outgroup_fasta_filename)
        print 'Family fasta files : {0}'.format(self.family_fasta_filedir)


if __name__ == '__main__':
    basepath = BasePath()
    basepath.print_base_paths()
