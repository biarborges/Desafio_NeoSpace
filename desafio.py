import pandas as pd

modelA = pd.read_csv('modelA.csv', sep=';')
modelB = pd.read_csv('modelB.csv', sep=';')


def calculate_hallucination(model):
    correct_answers = model['Classification'].sum()
    total_answers = len(model)
    hallucination = (total_answers - correct_answers) / total_answers

    return hallucination

def difference(hallucinationA, hallucinationB):
    D = hallucinationA - hallucinationB

    return D


result_modelA = calculate_hallucination(modelA)
result_modelB = calculate_hallucination(modelB)

print("Result: ", difference(result_modelA, result_modelB))
