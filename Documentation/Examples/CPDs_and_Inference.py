from pgmpy.factors.discrete import TabularCPD
from pgmpy.models import BayesianModel
from pgmpy.inference import VariableElimination


structure = BayesianModel([('A','B'),
                            ('C','B'),
                            ('B','D')])

A_cpd = TabularCPD(
                variable = 'A',
                variable_card = 2,
                values = [[.2,.8]])

C_cpd = TabularCPD(
                variable = 'C',
                variable_card = 2,
                values = [[.7,.3]])

D_cpd = TabularCPD(
                variable = 'D',
                variable_card = 2,
                values = [[.95, .8, .5],
                        [.05, .2 ,.5]],
                evidence = ['B'],
                evidence_card = [3])

B_cpd = TabularCPD(
                variable = 'B',
                variable_card = 3,
                values = [[.5, .8, .8, .9],
                        [.3, .15 ,.1, .08],
                        [.2, .05, .1, .02]],
                evidence = ['A','C'],
                evidence_card = [2,2])
#ADD CPDs
structure.add_cpds(A_cpd, B_cpd, C_cpd, D_cpd)
#GET CPDs
structure.get_cpds()
#Find active trail nodes
structure.active_trail_nodes('A')
structure.active_trail_nodes('B')
#Find local independencies
structure.local_independencies('A')
structure.local_independencies('B')
#Get all independencies

structure.get_independencies()

#MAKING INFERENCES
structure_infer = VariableElimination(structure)
prob_D = structure_infer.query(variables = ['D'])
print(prob_D['D'])

prob_D_good_A = structure_infer.query(
                                variables = ['D','A'])
print(prob_D_good_A['A'])
print(prob_D_good_A['D'])

prob_D_good_A = structure_infer.query(
                                variables = ['D','B','A'])
print(prob_D_good_A['B'])
print(prob_D_good_A['D'])


###############################
prob_D_bad_A = structure_infer.query(
                        variables = ['D'],
                        evidence = {'A':1})
print(prob_D_bad_A['D'])

prob_D_bad_A = structure_infer.query(
                        variables = ['D'],
                        evidence = {'A':0})
print(prob_D_bad_A['D'])


#Most probable state for a Variable
print(structure_infer.map_query( variables = ['A']))
print(structure_infer.map_query( variables = ['D']))
print(structure_infer.map_query( variables = ['B']))
