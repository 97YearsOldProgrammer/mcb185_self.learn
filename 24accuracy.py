# F1 score calculator

def f1_score(tp, tn, fp, fn):
	precision = tp/( tp + fp)
	recall    = tp/( tp + fn)
	f1_score  = 2 * (recall * precision)/(recall + precision)
	print(f1_score)

# test

f1_score(18, 4, 3, 2)
f1_score(180,30,18,5)
f1_score(1000,1200,95,58)