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

    @lru_cache(maxsize=None)
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

#Funkcija simetricen, ki preveri ali je niz simetricen ali ne.(Verjetno obstaja se lazje/ hitreje)
def simetricen(n):
    niz = n
    obrnjen = ""
    if len(n) == 0:
        return False
    elif len(n) == 1:
        return True
    else:
        while len(n) > 0:
            z = n[-1]
            obrnjen += z
            n = n[:-1]
        if niz == obrnjen:
            return True
        else:
            return False

# Stevilo delov bomo pogledali na naslednji nacin:
# Na zacetku preverimo, ali je nas niz ze palindrom, in ce je bo funkcija vrnila 1, saj pri ponovne klicu klicemo s praznim nizom (niz[:0] == "")
# Ce pa ta ni palindrom, se bomo nazaj klicali z ena vecjim indeksom, in to ponavljali, dokler ne najdemo palindroma. Potem pa se klicemo z nizom brez ze najdenega palindroma in indexom 0.
# Primer (ABC, 0) -> (ABC , 1) -> (ABC, 2) , C je palindrom -> 1 + (AB, 0) -> 1 + (AB, 1), B je palindrom -> 1 + 1 + (A, 0) -> A je palindrom -> 3 

def stevilo_delov(niz):

    @lru_cache(maxsize=None)
    def prestej_pomozna(niz ,i):
        dobri_deli = 0
        if len(niz) == 0:
            return dobri_deli
        elif simetricen(niz[i:]) == False:
            return dobri_deli + prestej_pomozna(niz, i + 1)
        elif simetricen(niz[i:]) == True:
            dobri_deli += 1
            return dobri_deli + prestej_pomozna(niz[:i], 0)
        return dobri_deli

    return prestej_pomozna(niz, 0)