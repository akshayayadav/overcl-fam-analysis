import re


def get_seqid_sequence_dict(fasta_filename):
    fasta_file = open(fasta_filename, "r")
    current_seqid = ""
    seqid_sequence_dict = {}
    for line in fasta_file:
        line = line.rstrip()
        if re.match(r'^\>', line):
            linearr = re.split(r'\s+', line)
            current_seqid = linearr[0]
            current_seqid = current_seqid[1:]
            seqid_sequence_dict[current_seqid] = ""
        else:
            seqid_sequence_dict[current_seqid] = seqid_sequence_dict[current_seqid] + line

    fasta_file.close()
    return seqid_sequence_dict


def count_sequences_from_fasta(fasta_filename):
    seq_count = 0
    fasta_file = open(fasta_filename, "r")
    for line in fasta_file:
        line = line.rstrip()
        if re.match(r'^>', line):
            seq_count += 1
    fasta_file.close()
    return seq_count


if __name__ == '__main__':
    exit()
