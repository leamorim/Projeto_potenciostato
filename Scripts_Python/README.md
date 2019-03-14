#Descrição das funções utilizadas para Suavização, Baseline Correction e Find Peaks

Smoothing Filter(Savitzky-Golav) / Baseline Correction(ALPS) / Find peaks(find_peaks scipy) e find_peak (Encontra máximo global)

## FILTRO DE SUAVIZAÇÃO (SAVITZKY-GOLAV)

* Lista de parâmetros: 
                        1. Array para suavizar
                        2. window_length --> largura da janela do filtro
                        3. polyorder --> ordem do polinômio a ser usado no filtro
                        
* Retorna: Vetor suavizado

        from scipy.signal import savgol_filter
        #valores usados nos testes --> window_length = 11 e polyorder = 2
        y = savgol_filter(y,window_length = 11,polyorder = 2)

## BASELINE CORRECTION(ALPS)
### (não contém todos os parâmetros listados aqui, apenas os utilizados nos teste)
* Lista de parâmetros: 
    1. Array(Y) para calcular o baseline
    2. lam --> Lambda que se refere a suavização e costuma ter valores entre 10^2 e 10^9
    3. p --> Assimetria e costuma ter valores entre 0.1 e 0.001
    
* Retorna: O algoritmo retorna um vetor que se refere ao baseline

        import numpy as np
        from scipy import sparse
        from scipy.sparse.linalg import spsolve

        def baseline_alps(y, lam, p, niter=10):
            L = len(y)
            D = sparse.diags([1,-2,1],[0,-1,-2], shape=(L,L-2))
            w = np.ones(L)
            for i in range(niter):
                W = sparse.spdiags(w, 0, L, L)
                Z = W + lam * D.dot(D.transpose())
                z = spsolve(Z, w*y)
                w = p * (y > z) + (1-p) * (y < z)
            return z
        #valores usados nos testes --> lam = 3000 e p = 0.0001
        baseline = baseline_alps(b,lam = 3000,p = 0.0001)


## FINDPEAKS
### Função find_peaks()
* Lista de parâmetros:
        1. Array(Y) para se procurar os picos
        2. height --> quantidade de picos a serem encontrados
    
* Retorna: o índice dos picos e um dicionário com informações sobre os picos dependendo dos parâmetros passados
    
    Lista de parâmetros:
        Array(y) para se procurar o máximo global
    Retorna: o índice onde foi encontrado o máximo global

        from scipy.signal import find_peaks
        #ret_y contém o índice do pico
        ret_y, dic = find_peaks(y,height = 1)


        def find_peak(y): 
            N = y.size
            max = y[0]
            i_max = 0
            for i in range (1,N):
                if y[i] > max:
                    max = y[i]
                    i_max = i   
            return i_max
        i_max = pico(y)
### Função find_peak()
    
* Lista de parâmetros:
        1. Array(y) para se procurar o máximo global
* Retorna: o índice onde foi encontrado o máximo global

        def find_peak(y): 
            N = y.size
            max = y[0]
            i_max = 0
            for i in range (1,N):
                if y[i] > max:
                    max = y[i]
                    i_max = i   
            return i_max
        i_max = pico(y)