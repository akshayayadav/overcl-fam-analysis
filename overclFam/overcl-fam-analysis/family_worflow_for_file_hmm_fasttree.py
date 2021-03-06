import sys
from build_family_msa import BuildFastaMSA
from build_hmm import BuildHMM
from execute_hmmsearch import HMMsearch
from closest_nonfamily_sequences_hmm import ClosestNonFamilySequencesHMMsearch
from write_sequences_hmm import WriteSequencesToFile
from build_msa import BuildMSA
from tree_building_fasttree import BuildFastTree
from root_tree import TreeRooting
from family_scoring_fasttree import PairBasedTreeScore
from clade_extration_fasttree import IngroupClades


def execute_workflow_for_family(fam_id, hmmsearch_evalue_cutoff, msa_num_threads, outgroup_id_arr,
                                tree_building_num_threads, clade_species_representation_cutoff,
                                non_family_seq_count_cutoff):
    # fam_id = "OG0000243"
    # phmmer_evalue_cutoff = "1e-5"
    # msa_num_threads = 5
    # outgroup_id_arr = ['prupe', 'cucsa', 'arath', 'vitvi', 'solly']
    # tree_building_num_threads = 5
    # clade_species_representation_cutoff = 0.7

    print 'Processing family {}'.format(fam_id)

    print "Building family MSA"
    family_msa = BuildFastaMSA(fam_id)
    family_msa.build_msa_from_fasta()
    print "Family MSA done"

    print "Building family HMM"
    family_hmm = BuildHMM(fam_id)
    family_hmm.build_hmm_from_msa()
    print "Family HMM done"

    print "Searching family HMM against outgroup fasta"
    family_hmmsearch = HMMsearch(fam_id, hmmsearch_evalue_cutoff)
    family_hmmsearch.search_family_hmm_against_outgroupfasta()
    print "Family HMM search against outgroup fasta done"

    print "Searching for closest outgroup sequences"
    closest_outgroup_sequences = ClosestNonFamilySequencesHMMsearch(fam_id, non_family_seq_count_cutoff)
    status = closest_outgroup_sequences.get_top_sequences_from_hmmsearch()
    if status == 0:
        return None
    print "Closest outgroup sequence search done"

    print "Writing family-outgroup fasta"
    family_outgroup_fasta = WriteSequencesToFile(fam_id)
    family_outgroup_fasta.write_fasta_from_sequence_list()
    print "Family-outgroup fasta done"

    print "Build family-outgroup MSA"
    family_outgroup_msa = BuildMSA(fam_id, msa_num_threads)
    family_outgroup_msa.build_msa_from_fasta()
    print "Family-outgroup MSA done"

    print "Building family-outgroup tree"
    family_outgroup_tree = BuildFastTree(fam_id)
    family_outgroup_tree.execute_fasttree()
    print "Family-outgroup ML tree done"

    print "Rooting tree using outgroups"
    rooted_family_outgroup_tree = TreeRooting(fam_id, outgroup_id_arr, non_family_seq_count_cutoff)
    rooted_family_outgroup_tree.root_tree()
    print "Tree rooting done"

    print "Scoring family-outgroup ML tree"
    family_tree_score = PairBasedTreeScore(fam_id)
    family_tree_score.score_family_tree()
    print "Family-outgroup ML tree scoring done"

    print "Extracting ingroup clades"
    ingroup_clades = IngroupClades(fam_id, clade_species_representation_cutoff)
    ingroup_clades.get_ingroup_monoplyletic_clades()
    print "Ingroup clade extraction done\n\n"


def main():
    fam_id = sys.argv[1]
    hmmsearch_evalue_cutoff = "1e-5"
    msa_num_threads = 10
    outgroup_id_arr = ['prupe', 'cucsa', 'arath', 'vitvi', 'solly']
    tree_building_num_threads = 10
    clade_species_representation_cutoff = 0.7
    non_family_seq_count_cutoff = 10

    execute_workflow_for_family(fam_id, hmmsearch_evalue_cutoff, msa_num_threads, outgroup_id_arr,
                                tree_building_num_threads, clade_species_representation_cutoff,
                                non_family_seq_count_cutoff)


if __name__ == '__main__':
    main()
