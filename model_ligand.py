from modeller import *
from modeller.automodel import *

# cria o ambiente para o MODELLER realizar a modelagem
env = environ()
env.io.atom_files_directory = ['.', '../atom_files']

# Realiza a leitura da parte de HETATM do PDB utilizado como molde
env.io.hetatm = True

a = automodel(env, 
              alnfile='aling-mult.ali',		# Nome do arquivo de alinhamento que foi obtido pelo scritp "align2d.py"
              knowns=('Molde'),				# Nome do arquivo PDB do Molde
              sequence='SEQ')				# Nome da sequencia alvo

a.starting_model = 1
a.ending_model = 1							# Numero total de modelos que serão gerados

a.make()
