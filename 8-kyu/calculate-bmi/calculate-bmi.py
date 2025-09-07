def bmi(weight, height):
    bmi = weight / height**2
    base = {"1Underweight":18.5, "2Normal":25, "3Overweight":30, "4Obese":999}
    resultado = [i for i,j in base.items() if j >= bmi]
    resultado.sort()
    resultado = resultado[0]
    return resultado[1:]