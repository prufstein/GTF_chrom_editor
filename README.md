# GTF_chrom_editor
A short script to modify GTF files to change the chromosome notations based on assembley reports.

NB, I know that this process is fairly trivial, but this is an exercise in creating a repeatable codebase to solve the problem.

Assembley Reports are downloaded from the annotation; 

e.g.
https://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/009/914/755/GCF_009914755.1_T2T-CHM13v2.0/GCF_009914755.1_T2T-CHM13v2.0_assembly_report.txt
for human T2T

Please run 
prepare_assembley_report.sh on the annotation text file using the format; bash prepare_assembley_report.sh in.file out.file

You can then use the python script to change the chromosome annotations. By default it changes from RefSeq-Accn to chrom number but this can be edited. 
