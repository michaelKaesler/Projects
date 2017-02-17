from __future__ import print_function 
import sys
import math



#first, read data into two arrays, left column for the state, right column for observation
#the two arrays are linked by their indicies

with open("typos20.data") as f:
	f = [x.strip() for x in f if x.strip()]
	data = [tuple(x.split()) for x in f[0:]]
	states = [x[0] for x in data]
	evidence = [x[1] for x in data]
	#print("states",evidence) works
	
with open("typos20Test.data") as f:
	f = [x.strip() for x in f if x.strip()]
	data = [tuple(x.split()) for x in f[0:]]
	states_test = [x[0] for x in data]
	evidence_test = [x[1] for x in data]
	#print("states",evidence) works
	


letters = 'abcdefghijklmnopqrstuvwxyz_'


#INITIAL DISTRIBUTION
initial_dict = {}
def initial(letter):
	#initial_dict[letter] = {}
	x = 2.0/27.0
	y = 1.0/27.0
	if (letter == "b"):
		initial_dict["b"] = x
	else:
		initial_dict[letter] = y

for elt in list(letters):
	initial(elt)


#get TRANSITION PROBABILITIES, 
#making function that will get looped through by every letter in alaphabet
#(by for elt in list(statestring)) will make a graph holding the list for
#every letter (as keys) and every list off those keys hold all the letters that
#come after that particular letter, will need to calculate the probs based off that
#new 'sample' 
holding_dict = {}
def makeLists(letter):
	holding_dict[letter] = []
	for i in xrange(len(states)-1):
		if (states[i] == letter):
			holding_dict[letter].append(states[i+1])

#now, creating all of the holding_dict
for elt in list(letters):
	makeLists(elt)


#CALCULATING TRANSITION PROBABILITES
#counting dict contains the transition probabilites
counting_dict = {}
count = {}
def count_tran(letter):
	counting_dict[letter] = {}
	
	
	a = float(holding_dict[letter].count("a"))
	b = float(holding_dict[letter].count("b"))
	c = float(holding_dict[letter].count("c"))
	d = float(holding_dict[letter].count("d"))
	e = float(holding_dict[letter].count("e"))
	f = float(holding_dict[letter].count("f"))
	g = float(holding_dict[letter].count("g"))
	h = float(holding_dict[letter].count("h"))
	i = float(holding_dict[letter].count("i"))
	j = float(holding_dict[letter].count("j"))
	k = float(holding_dict[letter].count("k"))
	l = float(holding_dict[letter].count("l"))
	m = float(holding_dict[letter].count("m"))
	n = float(holding_dict[letter].count("n"))
	o = float(holding_dict[letter].count("o"))
	p = float(holding_dict[letter].count("p"))
	q = float(holding_dict[letter].count("q"))
	r = float(holding_dict[letter].count("r"))
	s = float(holding_dict[letter].count("s"))
	t = float(holding_dict[letter].count("t"))
	u = float(holding_dict[letter].count("u"))
	v = float(holding_dict[letter].count("v"))
	w = float(holding_dict[letter].count("w"))
	x = float(holding_dict[letter].count("x"))
	y = float(holding_dict[letter].count("y"))
	z = float(holding_dict[letter].count("z"))
	zz = float(holding_dict[letter].count("_"))
	
	
	prob_a = float((1.0+a)/((27.0 + len(holding_dict[letter]))))
	prob_b = float((1.0+b)/((27.0 + len(holding_dict[letter]))))
	prob_c = float((1.0+c)/((27.0 + len(holding_dict[letter]))))
	prob_d = float((1.0 +d)/((27.0 + len(holding_dict[letter]))))
	prob_e = float((1.0+e)/((27.0 + len(holding_dict[letter]))))
	prob_f = float((1.0+f)/((27.0 + len(holding_dict[letter]))))
	prob_g = float((1.0+g)/((27.0 + len(holding_dict[letter]))))
	prob_h = float((1.0+h)/((27.0 + len(holding_dict[letter]))))
	prob_i = float((1.0+i)/((27.0 + len(holding_dict[letter]))))
	prob_j = float((1.0+j)/((27.0 + len(holding_dict[letter]))))
	prob_k = float((1.0 + k)/((27.0 + len(holding_dict[letter]))))
	prob_l = float((1.0+l)/((27.0 + len(holding_dict[letter]))))
	prob_m = float((1.0+m)/((27.0 + len(holding_dict[letter]))))
	prob_n = float((1.0+n)/((27.0 + len(holding_dict[letter]))))
	prob_o = float((1.0+o)/((27.0 + len(holding_dict[letter]))))
	prob_p = float((1.0+p)/((27.0 + len(holding_dict[letter]))))
	prob_q = float((1.0+q)/((27.0 + len(holding_dict[letter]))))
	prob_r = float((1.0+r)/((27.0 + len(holding_dict[letter]))))
	prob_s = float((1.0+s)/((27.0 + len(holding_dict[letter]))))
	prob_t = float((1.0+t)/((27.0 + len(holding_dict[letter]))))
	prob_u = float((1.0+u)/((27.0 + len(holding_dict[letter]))))
	prob_v = float((1.0+v)/((27.0 + len(holding_dict[letter]))))
	prob_w = float((1.0+w)/((27.0 + len(holding_dict[letter]))))
	prob_x = float((1.0+x)/((27.0 + len(holding_dict[letter]))))
	prob_y = float((1.0+y)/((27.0 + len(holding_dict[letter]))))
	prob_z = float((1.0+z)/((27.0 + len(holding_dict[letter]))))
	prob_zz = float((1.0+zz)/((27.0 +len(holding_dict[letter]))))
	
	counting_dict[letter]["a"] = prob_a
	counting_dict[letter]["b"] = prob_b
	counting_dict[letter]["c"] = prob_c
	counting_dict[letter]["d"] = prob_d
	counting_dict[letter]["e"] = prob_e
	counting_dict[letter]["f"] = prob_f
	counting_dict[letter]["g"] = prob_g
	counting_dict[letter]["h"] = prob_h
	counting_dict[letter]["i"] = prob_i
	counting_dict[letter]["j"] = prob_j
	counting_dict[letter]["k"] = prob_k
	counting_dict[letter]["l"] = prob_l
	counting_dict[letter]["m"] = prob_m
	counting_dict[letter]["n"] = prob_n
	counting_dict[letter]["o"] = prob_o
	counting_dict[letter]["p"] = prob_p
	counting_dict[letter]["q"] = prob_q
	counting_dict[letter]["r"] = prob_r
	counting_dict[letter]["s"] = prob_s
	counting_dict[letter]["t"] = prob_t
	counting_dict[letter]["u"] = prob_u
	counting_dict[letter]["v"] = prob_v
	counting_dict[letter]["w"] = prob_w
	counting_dict[letter]["x"] = prob_x
	counting_dict[letter]["y"] = prob_y
	counting_dict[letter]["z"] = prob_z
	counting_dict[letter]["_"] = prob_zz
for elt in list(letters):
	count_tran(elt)

'''print("probability for a given |")
print(*counting_dict["a"], sep="\n") ## can do this sepearatly for each one to get right format
#that we need'''

#CALCULATE EMISSION PROBABILITES

emis_hold_dict = {}
def hold_emis(letter):
	emis_hold_dict[letter] = []
	for i in xrange(len(states)):
		if (states[i] == letter):
			emis_hold_dict[letter].append(evidence[i])
	
for elt in list(letters):
	hold_emis(elt)

#print ("list for f", emis_hold_dict["f"])  WORKS

emis_count = {}
def count_emis(letter):
	emis_count[letter] = {}
	
	if (letter == "a"):
		a = float(emis_hold_dict["a"].count("a"))
		q = float(emis_hold_dict["a"].count("q"))
		s = float(emis_hold_dict["a"].count("s"))
		z = float(emis_hold_dict["a"].count("z"))
		prob_a = float(((1+a)/(4+len(emis_hold_dict["a"]))))
		prob_q = float(((1+q)/(4+len(emis_hold_dict["a"]))))
		prob_s = float(((1+s)/(4+len(emis_hold_dict["a"]))))
		prob_z = float(((1+z)/(4+len(emis_hold_dict["a"]))))
		emis_count["a"]["a"] = prob_a
		emis_count["a"]["q"] = prob_q
		emis_count["a"]["s"] = prob_s
		emis_count["a"]["z"] = prob_z
		
	if (letter == "b"):
		b = float(emis_hold_dict["b"].count("b"))
		g = float(emis_hold_dict["b"].count("g"))
		h = float(emis_hold_dict["b"].count("h"))
		n = float(emis_hold_dict["b"].count("n"))
		v = float(emis_hold_dict["b"].count("v"))
		prob_b = float(((1+b)/(5+len(emis_hold_dict["b"]))))
		prob_g = float(((1+g)/(5+len(emis_hold_dict["b"]))))
		prob_h = float(((1+h)/(5+len(emis_hold_dict["b"]))))
		prob_n = float(((1+n)/(5+len(emis_hold_dict["b"]))))
		prob_v = float(((1+v)/(5+len(emis_hold_dict["b"]))))
		emis_count["b"]["b"] = prob_b
		emis_count["b"]["g"] = prob_g
		emis_count["b"]["h"] = prob_h
		emis_count["b"]["n"] = prob_n
		emis_count["b"]["v"] = prob_v
		
	if (letter == "c"):
		c = float(emis_hold_dict["c"].count("c"))
		d = float(emis_hold_dict["c"].count("d"))
		f = float(emis_hold_dict["c"].count("f"))
		v = float(emis_hold_dict["c"].count("v"))
		x = float(emis_hold_dict["c"].count("x"))
		prob_c = float(((1+c)/(5+len(emis_hold_dict["c"]))))
		prob_d = float(((1+d)/(5+len(emis_hold_dict["c"]))))
		prob_f = float(((1+f)/(5+len(emis_hold_dict["c"]))))
		prob_v = float(((1+v)/(5+len(emis_hold_dict["c"]))))
		prob_x = float(((1+x)/(5+len(emis_hold_dict["c"]))))
		emis_count["c"]["c"] = prob_c
		emis_count["c"]["d"] = prob_d
		emis_count["c"]["f"] = prob_f
		emis_count["c"]["v"] = prob_v
		emis_count["c"]["x"] = prob_x
		
	if (letter == "d"):
		c = float(emis_hold_dict["d"].count("c"))
		d = float(emis_hold_dict["d"].count("d"))
		e = float(emis_hold_dict["d"].count("e"))
		f = float(emis_hold_dict["d"].count("f"))
		s = float(emis_hold_dict["d"].count("s"))
		x = float(emis_hold_dict["d"].count("x"))
		prob_c = float(((1+c)/(6+len(emis_hold_dict["d"]))))
		prob_d = float(((1+d)/(6+len(emis_hold_dict["d"]))))
		prob_e = float(((1+e)/(6+len(emis_hold_dict["d"]))))
		prob_f = float(((1+f)/(6+len(emis_hold_dict["d"]))))
		prob_s = float(((1+s)/(6+len(emis_hold_dict["d"]))))
		prob_x = float(((1+x)/(6+len(emis_hold_dict["d"]))))
		emis_count["d"]["c"] = prob_c
		emis_count["d"]["d"] = prob_d
		emis_count["d"]["e"] = prob_e
		emis_count["d"]["f"] = prob_f
		emis_count["d"]["s"] = prob_s
		emis_count["d"]["x"] = prob_x
		
	if (letter == "e"):
		d = float(emis_hold_dict["e"].count("d"))
		e = float(emis_hold_dict["e"].count("e"))
		r = float(emis_hold_dict["e"].count("r"))
		w = float(emis_hold_dict["e"].count("w"))
		prob_d = float(((1+d)/(4+len(emis_hold_dict["e"]))))
		prob_e = float(((1+e)/(4+len(emis_hold_dict["e"]))))
		prob_r = float(((1+r)/(4+len(emis_hold_dict["e"]))))
		prob_w = float(((1+w)/(4+len(emis_hold_dict["e"]))))
		emis_count["e"]["d"] = prob_d
		emis_count["e"]["e"] = prob_e
		emis_count["e"]["r"] = prob_r
		emis_count["e"]["w"] = prob_w
		
	if (letter == "f"):
		c = float(emis_hold_dict["f"].count("c"))
		d = float(emis_hold_dict["f"].count("d"))
		f = float(emis_hold_dict["f"].count("f"))
		g = float(emis_hold_dict["f"].count("g"))
		r = float(emis_hold_dict["f"].count("r"))
		t = float(emis_hold_dict["f"].count("t"))
		v = float(emis_hold_dict["f"].count("v"))
		prob_c = float(((1+c)/(7+len(emis_hold_dict["f"]))))
		prob_d = float(((1+d)/(7+len(emis_hold_dict["f"]))))
		prob_f = float(((1+f)/(7+len(emis_hold_dict["f"]))))
		prob_g = float(((1+g)/(7+len(emis_hold_dict["f"]))))
		prob_r = float(((1+r)/(7+len(emis_hold_dict["f"]))))
		prob_t = float(((1+t)/(7+len(emis_hold_dict["f"]))))
		prob_v = float(((1+v)/(7+len(emis_hold_dict["f"]))))
		emis_count["f"]["c"] = prob_c
		emis_count["f"]["d"] = prob_d
		emis_count["f"]["f"] = prob_f
		emis_count["f"]["g"] = prob_g
		emis_count["f"]["r"] = prob_r
		emis_count["f"]["t"] = prob_t
		emis_count["f"]["v"] = prob_v
		
	if (letter == "g"):
		b = float(emis_hold_dict["g"].count("b"))
		f = float(emis_hold_dict["g"].count("f"))
		g = float(emis_hold_dict["g"].count("g"))
		h = float(emis_hold_dict["g"].count("h"))
		t = float(emis_hold_dict["g"].count("t"))
		v = float(emis_hold_dict["g"].count("v"))
		prob_b = float(((1+b)/(6+len(emis_hold_dict["g"]))))
		prob_f = float(((1+f)/(6+len(emis_hold_dict["g"]))))
		prob_g = float(((1+g)/(6+len(emis_hold_dict["g"]))))
		prob_h = float(((1+h)/(6+len(emis_hold_dict["g"]))))
		prob_t = float(((1+t)/(6+len(emis_hold_dict["g"]))))
		prob_v = float(((1+v)/(6+len(emis_hold_dict["g"]))))
		emis_count["g"]["b"] = prob_b
		emis_count["g"]["f"] = prob_f
		emis_count["g"]["g"] = prob_g
		emis_count["g"]["h"] = prob_h
		emis_count["g"]["t"] = prob_t
		emis_count["g"]["v"] = prob_v
		
	if (letter == "h"):
		b = float(emis_hold_dict["h"].count("b"))
		g = float(emis_hold_dict["h"].count("g"))
		h = float(emis_hold_dict["h"].count("h"))
		j = float(emis_hold_dict["h"].count("j"))
		n = float(emis_hold_dict["h"].count("n"))
		x = float(emis_hold_dict["h"].count("x"))
		prob_b = float(((1+b)/(6+len(emis_hold_dict["h"]))))
		prob_g = float(((1+g)/(6+len(emis_hold_dict["h"]))))
		prob_h = float(((1+h)/(6+len(emis_hold_dict["h"]))))
		prob_j = float(((1+j)/(6+len(emis_hold_dict["h"]))))
		prob_n = float(((1+n)/(6+len(emis_hold_dict["h"]))))
		prob_x = float(((1+x)/(6+len(emis_hold_dict["h"]))))
		emis_count["h"]["b"] = prob_b
		emis_count["h"]["g"] = prob_g
		emis_count["h"]["h"] = prob_h
		emis_count["h"]["j"] = prob_j
		emis_count["h"]["n"] = prob_n
		emis_count["h"]["x"] = prob_x
		
	if (letter == "i"):
		i = float(emis_hold_dict["i"].count("i"))
		j = float(emis_hold_dict["i"].count("j"))
		k = float(emis_hold_dict["i"].count("k"))
		o = float(emis_hold_dict["i"].count("o"))
		u = float(emis_hold_dict["i"].count("u"))
		prob_i = float(((1+i)/(5+len(emis_hold_dict["i"]))))
		prob_j = float(((1+j)/(5+len(emis_hold_dict["i"]))))
		prob_k = float(((1+k)/(5+len(emis_hold_dict["i"]))))
		prob_o = float(((1+o)/(5+len(emis_hold_dict["i"]))))
		prob_u = float(((1+u)/(5+len(emis_hold_dict["i"]))))
		emis_count["i"]["i"] = prob_i
		emis_count["i"]["j"] = prob_j
		emis_count["i"]["k"] = prob_k
		emis_count["i"]["o"] = prob_o
		emis_count["i"]["u"] = prob_u
		
	if (letter == "j"):
		h = float(emis_hold_dict["j"].count("h"))
		j = float(emis_hold_dict["j"].count("j"))
		k = float(emis_hold_dict["j"].count("k"))
		m = float(emis_hold_dict["j"].count("m"))
		n = float(emis_hold_dict["j"].count("n"))
		u = float(emis_hold_dict["j"].count("u"))
		prob_h = float(((1+h)/(6+len(emis_hold_dict["j"]))))
		prob_j = float(((1+j)/(6+len(emis_hold_dict["j"]))))
		prob_k = float(((1+k)/(6+len(emis_hold_dict["j"]))))
		prob_m = float(((1+m)/(6+len(emis_hold_dict["j"]))))
		prob_n = float(((1+n)/(6+len(emis_hold_dict["j"]))))
		prob_u = float(((1+u)/(6+len(emis_hold_dict["j"]))))
		emis_count["j"]["h"] = prob_h
		emis_count["j"]["j"] = prob_j
		emis_count["j"]["k"] = prob_k
		emis_count["j"]["m"] = prob_m
		emis_count["j"]["n"] = prob_n
		emis_count["j"]["u"] = prob_u
		
	if (letter == "k"):
		i = float(emis_hold_dict["k"].count("i"))
		j = float(emis_hold_dict["k"].count("j"))
		k = float(emis_hold_dict["k"].count("k"))
		l = float(emis_hold_dict["k"].count("l"))
		m = float(emis_hold_dict["k"].count("m"))
		prob_i = float(((1+i)/(5+len(emis_hold_dict["k"]))))
		prob_j = float(((1+j)/(5+len(emis_hold_dict["k"]))))
		prob_k = float(((1+k)/(5+len(emis_hold_dict["k"]))))
		prob_l = float(((1+l)/(5+len(emis_hold_dict["k"]))))
		prob_m = float(((1+m)/(5+len(emis_hold_dict["k"]))))
		emis_count["k"]["i"] = prob_i
		emis_count["k"]["j"] = prob_j
		emis_count["k"]["k"] = prob_k
		emis_count["k"]["l"] = prob_l
		emis_count["k"]["m"] = prob_m
		
	if (letter == "l"):
		k = float(emis_hold_dict["l"].count("k"))
		l = float(emis_hold_dict["l"].count("l"))
		o = float(emis_hold_dict["l"].count("o"))
		p = float(emis_hold_dict["l"].count("p"))
		prob_k = float(((1+k)/(4+len(emis_hold_dict["l"]))))
		prob_l = float(((1+l)/(4+len(emis_hold_dict["l"]))))
		prob_o = float(((1+o)/(4+len(emis_hold_dict["l"]))))
		prob_p = float(((1+p)/(4+len(emis_hold_dict["l"]))))
		emis_count["l"]["k"] = prob_k
		emis_count["l"]["l"] = prob_l
		emis_count["l"]["o"] = prob_o
		emis_count["l"]["p"] = prob_p
		
	if (letter == "m"):
		j = float(emis_hold_dict["m"].count("j"))
		k = float(emis_hold_dict["m"].count("k"))
		m = float(emis_hold_dict["m"].count("m"))
		n = float(emis_hold_dict["m"].count("n"))
		prob_j = float(((1+j)/(4+len(emis_hold_dict["m"]))))
		prob_k = float(((1+k)/(4+len(emis_hold_dict["m"]))))
		prob_m = float(((1+m)/(4+len(emis_hold_dict["m"]))))
		prob_n = float(((1+n)/(4+len(emis_hold_dict["m"]))))
		emis_count["m"]["j"] = prob_j
		emis_count["m"]["k"] = prob_k
		emis_count["m"]["m"] = prob_m
		emis_count["m"]["n"] = prob_n
		
	if (letter == "n"):
		b = float(emis_hold_dict["n"].count("b"))
		h = float(emis_hold_dict["n"].count("h"))
		j = float(emis_hold_dict["n"].count("j"))
		m = float(emis_hold_dict["n"].count("m"))
		n = float(emis_hold_dict["n"].count("n"))
		prob_b = float(((1+b)/(5+len(emis_hold_dict["n"]))))
		prob_h = float(((1+h)/(5+len(emis_hold_dict["n"]))))
		prob_j = float(((1+j)/(5+len(emis_hold_dict["n"]))))
		prob_m = float(((1+m)/(5+len(emis_hold_dict["n"]))))
		prob_n = float(((1+n)/(5+len(emis_hold_dict["n"]))))
		emis_count["n"]["b"] = prob_b
		emis_count["n"]["h"] = prob_h
		emis_count["n"]["j"] = prob_j
		emis_count["n"]["m"] = prob_m
		emis_count["n"]["n"] = prob_n
		
	if (letter == "o"):
		i = float(emis_hold_dict["o"].count("i"))
		k = float(emis_hold_dict["o"].count("k"))
		l = float(emis_hold_dict["o"].count("l"))
		o = float(emis_hold_dict["o"].count("o"))
		p = float(emis_hold_dict["o"].count("p"))
		prob_i = float(((1+i)/(5+len(emis_hold_dict["o"]))))
		prob_k = float(((1+k)/(5+len(emis_hold_dict["o"]))))
		prob_l = float(((1+l)/(5+len(emis_hold_dict["o"]))))
		prob_o = float(((1+o)/(5+len(emis_hold_dict["o"]))))
		prob_p = float(((1+p)/(5+len(emis_hold_dict["o"]))))
		emis_count["o"]["i"] = prob_i
		emis_count["o"]["k"] = prob_k
		emis_count["o"]["l"] = prob_l
		emis_count["o"]["o"] = prob_o
		emis_count["o"]["p"] = prob_p
		
	if (letter == "p"):
		l = float(emis_hold_dict["p"].count("l"))
		o = float(emis_hold_dict["p"].count("o"))
		p = float(emis_hold_dict["p"].count("p"))
		prob_l = float(((1+l)/(3+len(emis_hold_dict["p"]))))
		prob_o = float(((1+o)/(3+len(emis_hold_dict["p"]))))
		prob_p = float(((1+p)/(3+len(emis_hold_dict["p"]))))
		emis_count["p"]["l"] = prob_l
		emis_count["p"]["o"] = prob_o
		emis_count["p"]["p"] = prob_p
		
	if (letter == "q"):
		a = float(emis_hold_dict["q"].count("a"))
		q = float(emis_hold_dict["q"].count("q"))
		w = float(emis_hold_dict["q"].count("w"))
		prob_a = float(((1+a)/(3+len(emis_hold_dict["q"]))))
		prob_q = float(((1+q)/(3+len(emis_hold_dict["q"]))))
		prob_w = float(((1+w)/(3+len(emis_hold_dict["q"]))))
		emis_count["q"]["a"] = prob_a
		emis_count["q"]["q"] = prob_q
		emis_count["q"]["w"] = prob_w
		
	if (letter == "r"):
		d = float(emis_hold_dict["r"].count("d"))
		e = float(emis_hold_dict["r"].count("e"))
		f = float(emis_hold_dict["r"].count("f"))
		r = float(emis_hold_dict["r"].count("h"))
		t = float(emis_hold_dict["r"].count("t"))
		prob_d = float(((1+d)/(5+len(emis_hold_dict["r"]))))
		prob_e = float(((1+e)/(5+len(emis_hold_dict["r"]))))
		prob_f = float(((1+f)/(5+len(emis_hold_dict["r"]))))
		prob_r = float(((1+r)/(5+len(emis_hold_dict["r"]))))
		prob_t = float(((1+t)/(5+len(emis_hold_dict["r"]))))
		emis_count["r"]["d"] = prob_d
		emis_count["r"]["e"] = prob_e
		emis_count["r"]["f"] = prob_f
		emis_count["r"]["r"] = prob_r
		emis_count["r"]["t"] = prob_t
		
	if (letter == "s"):
		a = float(emis_hold_dict["s"].count("a"))
		d = float(emis_hold_dict["s"].count("d"))
		s = float(emis_hold_dict["s"].count("s"))
		w = float(emis_hold_dict["s"].count("w"))
		x = float(emis_hold_dict["s"].count("x"))
		z = float(emis_hold_dict["s"].count("z"))
		prob_a = float(((1+a)/(6+len(emis_hold_dict["s"]))))
		prob_d = float(((1+d)/(6+len(emis_hold_dict["s"]))))
		prob_s = float(((1+s)/(6+len(emis_hold_dict["s"]))))
		prob_w = float(((1+w)/(6+len(emis_hold_dict["s"]))))
		prob_x = float(((1+x)/(6+len(emis_hold_dict["s"]))))
		prob_z = float(((1+z)/(6+len(emis_hold_dict["s"]))))
		emis_count["s"]["a"] = prob_a
		emis_count["s"]["d"] = prob_d
		emis_count["s"]["s"] = prob_s
		emis_count["s"]["w"] = prob_w
		emis_count["s"]["x"] = prob_x
		emis_count["s"]["z"] = prob_z
		
	if (letter == "t"):
		f = float(emis_hold_dict["t"].count("f"))
		g = float(emis_hold_dict["t"].count("g"))
		r = float(emis_hold_dict["t"].count("r"))
		t = float(emis_hold_dict["t"].count("t"))
		y = float(emis_hold_dict["t"].count("y"))
		prob_f = float(((1+f)/(5+len(emis_hold_dict["t"]))))
		prob_g = float(((1+g)/(5+len(emis_hold_dict["t"]))))
		prob_r = float(((1+r)/(5+len(emis_hold_dict["t"]))))
		prob_t = float(((1+t)/(5+len(emis_hold_dict["t"]))))
		prob_y = float(((1+y)/(5+len(emis_hold_dict["t"]))))
		emis_count["t"]["f"] = prob_f
		emis_count["t"]["g"] = prob_g
		emis_count["t"]["r"] = prob_r
		emis_count["t"]["t"] = prob_t
		emis_count["t"]["y"] = prob_y
		
	if (letter == "u"):
		h = float(emis_hold_dict["u"].count("h"))
		i = float(emis_hold_dict["u"].count("i"))
		j = float(emis_hold_dict["u"].count("j"))
		u = float(emis_hold_dict["u"].count("u"))
		y = float(emis_hold_dict["u"].count("y"))
		prob_h = float(((1+h)/(5+len(emis_hold_dict["u"]))))
		prob_i = float(((1+i)/(5+len(emis_hold_dict["u"]))))
		prob_j = float(((1+j)/(5+len(emis_hold_dict["u"]))))
		prob_u = float(((1+u)/(5+len(emis_hold_dict["u"]))))
		prob_y = float(((1+y)/(5+len(emis_hold_dict["u"]))))
		emis_count["u"]["h"] = prob_h
		emis_count["u"]["i"] = prob_i
		emis_count["u"]["j"] = prob_j
		emis_count["u"]["u"] = prob_u
		emis_count["u"]["y"] = prob_y
		
	if (letter == "v"):
		b = float(emis_hold_dict["v"].count("b"))
		c = float(emis_hold_dict["v"].count("c"))
		f = float(emis_hold_dict["v"].count("f"))
		g = float(emis_hold_dict["v"].count("g"))
		v = float(emis_hold_dict["v"].count("v"))
		prob_b = float(((1+b)/(5+len(emis_hold_dict["v"]))))
		prob_c = float(((1+c)/(5+len(emis_hold_dict["v"]))))
		prob_f = float(((1+f)/(5+len(emis_hold_dict["v"]))))
		prob_g = float(((1+g)/(5+len(emis_hold_dict["v"]))))
		prob_v = float(((1+v)/(5+len(emis_hold_dict["v"]))))
		emis_count["v"]["b"] = prob_b
		emis_count["v"]["c"] = prob_c
		emis_count["v"]["f"] = prob_f
		emis_count["v"]["g"] = prob_g
		emis_count["v"]["v"] = prob_v
		
	if (letter == "w"):
		a = float(emis_hold_dict["w"].count("a"))
		e = float(emis_hold_dict["w"].count("e"))
		q = float(emis_hold_dict["w"].count("q"))
		s = float(emis_hold_dict["w"].count("s"))
		w = float(emis_hold_dict["w"].count("w"))
		prob_a = float(((1+a)/(5+len(emis_hold_dict["w"]))))
		prob_e = float(((1+e)/(5+len(emis_hold_dict["w"]))))
		prob_q = float(((1+q)/(5+len(emis_hold_dict["w"]))))
		prob_s = float(((1+s)/(5+len(emis_hold_dict["w"]))))
		prob_w = float(((1+w)/(5+len(emis_hold_dict["w"]))))
		emis_count["w"]["a"] = prob_a
		emis_count["w"]["e"] = prob_e
		emis_count["w"]["q"] = prob_q
		emis_count["w"]["s"] = prob_s
		emis_count["w"]["w"] = prob_w
		
	if (letter == "x"):
		c = float(emis_hold_dict["x"].count("c"))
		d = float(emis_hold_dict["x"].count("d"))
		s = float(emis_hold_dict["x"].count("s"))
		x = float(emis_hold_dict["x"].count("x"))
		z = float(emis_hold_dict["x"].count("z"))
		prob_c = float(((1+c)/(5+len(emis_hold_dict["x"]))))
		prob_d = float(((1+d)/(5+len(emis_hold_dict["x"]))))
		prob_s = float(((1+s)/(5+len(emis_hold_dict["x"]))))
		prob_x = float(((1+x)/(5+len(emis_hold_dict["x"]))))
		prob_z = float(((1+z)/(5+len(emis_hold_dict["x"]))))
		emis_count["x"]["c"] = prob_c
		emis_count["x"]["d"] = prob_d
		emis_count["x"]["s"] = prob_s
		emis_count["x"]["x"] = prob_x
		emis_count["x"]["z"] = prob_z
		
	if (letter == "y"):
		g = float(emis_hold_dict["y"].count("g"))
		h = float(emis_hold_dict["y"].count("h"))
		t = float(emis_hold_dict["y"].count("t"))
		u = float(emis_hold_dict["y"].count("u"))
		y = float(emis_hold_dict["y"].count("y"))
		prob_g = float(((1+g)/(5+len(emis_hold_dict["y"]))))
		prob_h = float(((1+h)/(5+len(emis_hold_dict["y"]))))
		prob_t = float(((1+t)/(5+len(emis_hold_dict["y"]))))
		prob_u = float(((1+u)/(5+len(emis_hold_dict["y"]))))
		prob_y = float(((1+y)/(5+len(emis_hold_dict["y"]))))
		emis_count["y"]["g"] = prob_g
		emis_count["y"]["h"] = prob_h
		emis_count["y"]["t"] = prob_t
		emis_count["y"]["u"] = prob_u
		emis_count["y"]["y"] = prob_y
		
	if (letter == "z"):
		a = float(emis_hold_dict["z"].count("a"))
		s = float(emis_hold_dict["z"].count("s"))
		x = float(emis_hold_dict["z"].count("x"))
		z = float(emis_hold_dict["z"].count("z"))
		prob_a = float(((1+a)/(4+len(emis_hold_dict["z"]))))
		prob_s = float(((1+s)/(4+len(emis_hold_dict["z"]))))
		prob_x = float(((1+x)/(4+len(emis_hold_dict["z"]))))
		prob_z = float(((1+z)/(4+len(emis_hold_dict["z"]))))
		emis_count["z"]["a"] = prob_a
		emis_count["z"]["s"] = prob_s
		emis_count["z"]["x"] = prob_x
		emis_count["z"]["z"] = prob_z
	if (letter == "_"):
		emis_count["_"]["_"] = 1.0
	
for elt in list(letters):
	count_emis(elt)
	
'''print ("emission for a")
print (*emis_count["a"], sep="\n") #WORKS

print ("emission for h")
print(*emis_count["h"], sep="\n")'''
'''for elt in list(letters):            #works, prints every probability in a
	print("\n")
	for i in emis_count[elt]:
		print(emis_count[elt][i])'''

#following wikipedia psuedo
def viterbi(obs, states1, start_p, trans_p, emit_p, states2):
	output = {}
	path = []
	
	#do the intial distribution
	for y in list(states1):
		if obs[0] not in emit_p[y]:
			output[y] = 0
		else:
			output[y] = math.log(start_p[y]) + math.log(emit_p[y][obs[0]])
	key, maxv = maxvalue(output)
	path.append(key)
	#for t+1
	for i in obs[1:]:
		for y in list(states1):
			if i not in emit_p[y]:
				output[y] = 0
			else:
				output[y] = math.log(emit_p[y][i]) + math.log(trans_p[key][y]) + maxv 
		key, maxv = maxvalue(output)
		path.append(key)
			
	
	#print(len(path))
	#print(len(obs))   they are the same length, that is good
	
	
	#this is not the problem
	#for i in path:     
		#print(i)
	
	num1 = 0
	num2 = 0
	denom1= 0
	denom2 = 0
	for i in xrange(0, len(path)):
		if path[i] is states2[i]:
			num1 += 1
			denom1 += 1
		else:
			denom1 += 1
		if states2[i] is obs[i]:
			num2 += 1
			denom2 +=1
		else:
			denom2 += 1
			
	error = 1 - float(num1)/(denom1)
	orig_error = 1 - float(num2)/(denom2)
	
	#print(error)
	#print(orig_error)
	
	return (path, error, orig_error)


	


def maxvalue(inputs):      
	temp_val = 999999999
	for j in inputs:
		if abs(inputs[j]) < abs(temp_val) and abs(inputs[j]) > 0:
			temp_key = j
			temp_val = inputs[j]
	return (temp_key, temp_val)
	

def print_old():
	path, error, orig = viterbi(evidence, letters, initial_dict, counting_dict, emis_count, states)
	for i in path:
		print(i)
	print(error)
	print(orig)

def print_test():
	path, error, orig = viterbi(evidence_test, letters, initial_dict, counting_dict, emis_count, states_test)
	for i in path:
		print(i)
	print(error)
	print(orig)



def write_test():
	path, error, orig = viterbi(evidence_test, letters, initial_dict, counting_dict, emis_count, states_test)
	with open('outputPART2.txt', 'w') as f:
		for i in path:
			f.writelines(i)
			f.writelines("\n")
		f.writelines("\n")
		f.writelines("viterbi error is \n")
		f.write(repr(error))
		f.writelines("\n")
		f.writelines("origonal error is \n")
		f.write(repr(orig))
		f.close()
	
write_test()
	
	
	
	
	
	
