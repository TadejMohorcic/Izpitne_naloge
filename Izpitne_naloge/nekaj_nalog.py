from functools import lru_cache

# 24.1.2018

def pozresni_lisjak(matrix, n):
    st_vrstic = len(matrix)
    st_stolpcev = len(matrix[0]) 

    @lru_cache(maxsize=None)
    def lisjak_pomozna(i, j, n):
        val = matrix[i][j]
        if n == 0:
            return 0
        elif j == (st_stolpcev - 1):
            if i == (st_vrstic - 1):
                return val
            else:
                return val + lisjak_pomozna(i + 1, 0, n -1)    
        else:
            if i == (st_vrstic - 1):
                return val + lisjak_pomozna(i, j + 1, n - 1)
            else:
                return val + max(lisjak_pomozna(i, j + 1, n - 1), lisjak_pomozna(i + 1, 0, n - 1))

    return lisjak_pomozna(0, 0, n)

pozresni_lisjak([[1,2,0,5],[0,4,1,1],[8,0,4,2]], 6)

# Izpit 10.2.2020

def rad_imam_zaporedja(k, n):

    @lru_cache(maxsize=None)
    def zaporedja_pomozna(trenutni, abs, dol):
        st_zaporedij = 0
        if dol == 1:
            return 1   
        else:
            for j in range(max(0, trenutni - abs), trenutni + abs + 1):
                st_zaporedij += zaporedja_pomozna(trenutni + j, abs, dol - 1)
        return st_zaporedij

    return zaporedja_pomozna(0, k, n)

rad_imam_zaporedja(5, 3)

# 28.1.2020

def mama_franca(dolzina, stevilo, sirina):

    @lru_cache
    def slepa_mama(n, m, l):
        stevilo_dobrih_postavitev = 0
        if n == l and m == 1:
            return 1
        elif m == 1 and n > l:
            return n - l + 1
        elif n <= 0 and m > 0:
            return 0
        elif n < m * l:
            return 0
        else:
            for j in range(l + 1, n + 1):
                stevilo_dobrih_postavitev += slepa_mama(n - j, m - 1, l)
            return stevilo_dobrih_postavitev

    return slepa_mama(dolzina, stevilo, sirina)

mama_franca(9, 3, 2)