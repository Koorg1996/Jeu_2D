import jeu

df = pd.DataFrame([["x","x","x","x","x"], ["x", "*","","o","x"],["x","x","x","","x"], ["x", "","","","*","x"]])
test = carte(df)
game = jeu(test)
game._main_()
