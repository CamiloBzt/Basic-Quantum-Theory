import numpy as np


def adjunta(vector):
    return vector.transpose().conjugate()


def unitary(mat):
    matDg = mat.transpose().conjugate()
    mult = np.matmul(mat, matDg)
    iden = np.identity(len(mat))
    if mult.all() == iden.all():
        return True
    return False


def probabilidad(vectorKet, pos):
    vectorKet[pos][0] = np.linalg.norm(vectorKet[pos][0]) ** 2 / np.linalg.norm(vectorKet) ** 2
    return vectorKet[pos][0]


def transitar(vectorKet, vectorKet2):
    result = np.dot(adjunta(vectorKet2), vectorKet)
    return np.linalg.norm(result) ** 2


def valorEsperado(mat, vectorKet):
    mult = np.matmul(mat, vectorKet)
    valor = np.dot(mult.transpose().conjugate(), vectorKet)[0][0]
    return valor


def varianza(mat, vectorKet):
    esp = valorEsperado(mat, vectorKet)
    idenE = esp * np.identity(len(mat))
    valorDelta = mat - idenE
    matl = np.matmul(valorDelta, valorDelta)
    vari = valorEsperado(matl, vectorKet)[0][0]
    return vari


def medida(mat):
    return np.linalg.eig(mat)[0]


def estados(mat):
    return np.linalg.eig(mat)[1]


def ejercicio1():
    mat = np.array([[1, -1j / 2, 0, -3 / 2],
                    [1j / 2, 1, 3 / 2, 0],
                    [0, 3 / 2, 1, -1j / 2],
                    [-3 / 2, 0, 1j / 2, 1]])
    vectSta = np.array([[0, 1], [1, 0]])
    spinVals = 1.0545718176461565e-34 / 2 * vectSta
    est = estados(spinVals)

    print(medida(mat))
    print()
    print(estados(mat))
    print()
    print(est)


def ejercicio2():
    vectorKet = np.array([1 / np.sqrt(2), 1j / np.sqrt(2)])
    vectSta = np.array([[0, 1], [1, 0]])

    spinVals = 1.0545718176461565e-34 / 2 * vectSta

    est = estados(spinVals)

    p1 = np.linalg.norm(np.inner(vectorKet, est[0])) ** 2
    p2 = np.linalg.norm(np.inner(vectorKet, est[1])) ** 2
    landa1 = medida(spinVals)[0]
    landa2 = medida(spinVals)[1]
    print()
    print(p1)
    print(p2)
    print()
    print(landa1)
    print(landa2)
    print()
    print("Value Distribution -- ", p1 * landa1 + p2 * landa2)


def ejercicio3():
    u1 = np.array([[0, 1], [1, 0]])
    u2 = np.array([[1 / np.sqrt(2), 1 / np.sqrt(2)], [1 / np.sqrt(2), -1 / np.sqrt(2)]])
    print(u1, unitary(u1))
    print()
    print(u2, unitary(u2))
    print()
    u3 = np.matmul(u1, u2)
    print(u3, unitary(u3))


def ejercicio4():
    mat = np.array([[0, 1 / np.sqrt(2), 1 / np.sqrt(2), 0],
                    [1j / np.sqrt(2), 0, 0, 1 / np.sqrt(2)],
                    [1 / np.sqrt(2), 0, 0, 1j / np.sqrt(2)],
                    [0, 1 / np.sqrt(2), -1 / np.sqrt(2), 0]])
    vect = np.array([[1], [0], [0], [0]])
    print(mat)
    print(vect)
    print()
    res = vect
    for i in range(3):
        res = np.matmul(mat, res)
    print(res)
    print()
    print(3)
    print()
    print(probabilidad(res, 3))
