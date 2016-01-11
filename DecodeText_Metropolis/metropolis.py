import numpy
import random
import matplotlib.pyplot as plt
from copy import deepcopy
import math

def generateTransitionMatrix(filename):
	f = open(filename, 'r'); 
	text = f.read();

	formattedText='';

	for ch in text:
		if(ch == '\n' or ch == '.' or ch == ','):
			formattedText+=' ';
		elif(isLetter(ch)):
			formattedText+=ch;

	formattedText = formattedText.lower();

	M = numpy.zeros((28,28), dtype = numpy.float);
	#N = numpy.zeros((28,28), dtype = numpy.int);

	for i in range (0, len(formattedText) - 1 ):
		if(formattedText[i] == ' '):
			ind1 = 27;
		if(formattedText[i+1] == ' '):
			ind2 = 27;
		if (formattedText[i] != ' '):
			ind1 = ord(formattedText[i]) - 96;
		if (formattedText[i+1] != ' '):
			ind2 = ord(formattedText[i+1]) - 96; 
		M[ind1][ind2]+=1;

	count = 0;

	for i in range (1, 28):
		for j in range (1,28):
			count+=M[i][j];
		for k in range(1,28):
			M[i][k]/=count;
		count = 0;

	#numpy.savetxt('transitionMatrix_probabilites.txt', M, fmt='%.4f');

	for i in range (1, 28):
		for j in range (1,28):
			if(M[i][j] == 0):
				M[i][j] = -12;
			else:
				M[i][j]= math.log(M[i][j]);

	numpy.savetxt('transitionMatrix_log_of_prob.txt', M, fmt='%.4f');	


def isLetter(ch):
	if ((ch >= 'A' and  ch <= 'Z') or (ch >= 'a' and  ch<='z') or ch == ' '):
		return True;
	else:
		return False;

def decipherText(M, encText):
	f = numpy.zeros(28, dtype = numpy.int);
	for i in range(1,28):
		f[i] = i;
	#while ():
		
	r=1;
	steps = 2500;
	p_list = [];
	f_list = [];
	rnd = 0.0;
	while (r<=steps):
		decrypt_f = decrypt(encText, f);
		p1 = calculateP(decrypt_f, f, M);
		f_star = transpose(f);
		decrypt_f_star = decrypt(encText, f_star);
		p2 = calculateP(decrypt_f_star, f_star, M);
		if(p2>p1):
			f = deepcopy(f_star);
			p = p2;
		else:
			rnd = (float(random.randint(0,10)))/10;
			while(rnd == 0):
				rnd = (float(random.randint(0,10)))/10;
			if(rnd <= math.exp(p2-p1)):
				f = deepcopy(f_star);
				p = p2;
		#if(r%2000 == 0):
		#	print decrypt(encText, f);
		#	print '\n';
		#	print f;
		#	print p2,p1,math.exp(p2-p1),rnd, r;
		r+=1;			
		#print p2,p1,math.exp(p2-p1),rnd, r;
		p = p1;
		p_list.append(p);
		f_list.append(f);
		if (r==2500):
			break;

		#print p;	

	

	#print decrypt(encText, f);
	return (p, decrypt(encText, f), p_list);


def calculateP(decrypt_f, f, M):
	p = 0.0;
	for i in range (0, len(decrypt_f)-1):
		if(decrypt_f[i] == ' '):
			ind1 = 27;
		if(decrypt_f[i+1] == ' '):
			ind2 = 27;
		if (decrypt_f[i] != ' '):
			ind1 = ord(decrypt_f[i]) - 96;
		if (decrypt_f[i+1] != ' '):
			ind2 = ord(decrypt_f[i+1]) - 96; 
		p+= (M[ind1, ind2]);
	#print p;
	return p;

def decrypt(encText, f):
	decTxt = '';
	for i in range(0,len(encText)):
		if(encText[i] == ' '):
			ind1 = 27;
			decTxt+=' ';

		if (encText[i] != ' '):
			ind1 = ord(encText[i]) - 96;
			decTxt+=chr(f[ind1]+96);

	return decTxt;

def transpose(f):

	n1 = 1;
	n2 = 1;
	f_star = numpy.zeros(28,dtype=int);

	for i in range(1,28):
		f_star[i] = f[i];

	while(n1==n2):
		n1 = random.randint(1,26);
		n2 = random.randint(1,26);

	temp  = f_star[n1];
	f_star[n1] = f_star[n2];
	f_star[n2] = temp;
	#print f
	#print f_star; 
	return f_star;


def generateCiphers(normaltxt):

	formattedText='';

	for ch in normaltxt:
		if(ch == '\n' or ch == '.' or ch == ','):
			formattedText+=' ';
		elif(isLetter(ch)):
			formattedText+=ch;

	formattedText = formattedText.lower();
	#print formattedText;

	f = numpy.zeros(28, dtype = int);
	for i in range(1,27):
		f[i] = i+1;
	f[26] = 1;
	encryptedText = '';
	for i in range(0, len(formattedText)):
		if (formattedText[i] == ' '):
			encryptedText+= ' ';
		else:
			ind = ord(formattedText[i]) - 96
			encryptedText+= chr(f[ind] + 96);	
	#print encryptedText;
	return encryptedText;



def main():
	#generateTransitionMatrix('Austen.txt');	

	M = numpy.zeros((27,27), dtype = numpy.float);
	M = numpy.loadtxt('transitionMatrix_log_of_prob.txt');
	#print M;
	#decipherText(M,'liw pskmwcl ynlwrdwsy wdkkj kh kguxws lauel dq civsgwe fucjwre lzom pgw twzk uwhxvvxvh lzom pgw lxzsp momwvp x mak ajmosp sak ol mk aebnaxvpavew rxpg kon konz mavvwzs xmizwssxvh mw rxpg pgw lnjjwsp uwjxwl ol konz azzohavew konz eovewxp avy konz swjlxsg yxsyaxv ol pgw lwwjxvhs ol opgwzs rwzw sneg as po lozm pgw hzonvyrozd ol yxsaiizouapxov ov rgxeg sneewwyxvh wtwvps gatw unxjp so xmmotaujw a yxsjxdw avy x gay vop dvorv kon a movpg uwlozw x lwjp pgap kon rwzw pgw jasp mav xv pgw rozjy rgom x eonjy wtwz uw izwtaxjwy ov po mazzk');
	encryptedText_default = 'lzom pgw twzk uwhxvvxvh lzom pgw lxzsp momwvp x mak ajmosp sak ol mk aebnaxvpavew rxpg kon konz mavvwzs xmizwssxvh mw rxpg pgw lnjjwsp uwjxwl ol konz azzohavew konz eovewxp avy konz swjlxsg yxsyaxv ol pgw lwwjxvhs ol opgwzs rwzw sneg as po lozm pgw hzonvyrozd ol yxsaiizouapxov ov rgxeg sneewwyxvh wtwvps gatw unxjp so xmmotaujw a yxsjxdw avy x gay vop dvorv kon a movpg uwlozw x lwjp pgap kon rwzw pgw jasp mav xv pgw rozjy rgom x eonjy wtwz uw izwtaxjwy ov po mazzk';
	normaltxt = 'one should first of all hear about the Lord. When one has perfectly and scrutinizingly heard, one must glorify His acts and deeds, and thus it will become possible to remember constantly the transcendental nature of the Lord. Hearing about and glorifying the Lord are identical with the transcendental nature of the Lord, and by so doing, one will be always in the association of the Lord Science';
	encryptedText = generateCiphers(normaltxt);
	best_p = -999999;
	best_p_list = [];
	best_decryption = '';
	for i in range(0,12):
		(p, decryptedTxt, p_list) = decipherText(M, encryptedText);
		print p, decryptedTxt;
		if(p>best_p):
			best_p = p;
			best_p_list = p_list;
			best_decryption = decryptedTxt;


	print '\n And the decrypted Text is : \n';
	print best_decryption;
	print len(encryptedText_default)
	print len(normaltxt)
	plt.plot(list(range(1,2500)),best_p_list);
	plt.ylabel('P');
	plt.xlabel('steps');
	plt.show();

if __name__ == '__main__':
	main();

