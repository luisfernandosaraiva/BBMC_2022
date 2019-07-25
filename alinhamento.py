from modeller import *

# cria o ambiente para o MODELLER realizar o alinhamento
env = environ()
aln = alignment(env)

#parametros necessarios para o alinhamento
mdl = model(env, file='2GEK', model_segment=('FIRST:A','LAST:A'))	# especifique o codigo do molde e a cadeia
aln.append_model(mdl, align_codes='2GEKA', atom_files='2GEK.pdb')	# especifique o codigo do molde com a cadeia e o codigo .pdb
aln.append(file='teste.ali', align_codes='teste')					# especifique a sequencia alvo e o nome da sequencia
aln.align2d()														# realiza o alinhamento
aln.write(file='teste_align.ali', alignment_format='PIR')			# salva um arquivo .ali
aln.write(file='teste_align.pap', alignment_format='PAP')			# salva um arquivo .pap
