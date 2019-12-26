import numpy as np
import matplotlib.pyplot as plt

def main():
    X = np.array([0.0400, 0.0625, 0.1111, 0.0400, 0.1111])
    Y = np.array([2.2943, 2.0428, 1.5132, 2.2387, 1.5010])

    A = np.array([X,np.ones(len(X))])
    A = A.T
    a,b = np.linalg.lstsq(A,Y)[0]
    print(a,b)

    plt.plot(X,Y,"ro")
    plt.plot(X,(a*X+b),"g--")
    plt.grid()
    plt.show()


if __name__ == '__main__':
    main()