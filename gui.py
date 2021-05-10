from LoadGames import load_FK, load_O, load_R, load_VP, load_XG

if __name__ == "__main__":
    vp_logged = False
    fk_logged = False
    orion_logged = False
    rm_logged = False
    xg_logged = False
    while True:
        web = input("What do you want to access ('v' 'f' 'o' 'x' 'r'): ")
        if web == 'f':
            load_FK(fk_logged)
            fk_logged = True
        elif web == 'o':
            load_O(orion_logged)
            orion_logged = True
        elif web == 'r':
            load_R(rm_logged)
            rm_logged = True
        elif web == 'v':
            load_VP(vp_logged)
            vp_logged = True
        elif web == 'x':
            load_XG(xg_logged)
            xg_logged = True
