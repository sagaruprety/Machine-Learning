# Written by Sagar Uprety
#
# Written in Python 2.7
# Requires python libraries like numpy, matplotlib,etc.
#
# Applies metropolis algorithm to an encoded text, which is essentially a substitution cipher. 
# This work is based on a paper by Persi Diaconis, the world renowned statistician.
# Here is a link to the paper: http://math.uchicago.edu/~shmuel/Network-course-readings/MCMCRev.pdf
#
# NOTE : If you don't get the correct result during the first run of the code, kindly run it a second time,
# as the code performs a random walk, so the accuracy is slightly uncertain.
# However, the second time running of the code should provide 99% accuracy.


import numpy
import random
import matplotlib.pyplot as plt
from copy import deepcopy
import math

# This code generates the transition matrix according to the Project Gutenberg's The Complete Works of Jane Austen.
# The text is taken from www.gutenberg.org.
# The text is processed by converting all alphabets to lower case and replacing all non-alpha characters 
# other than space, with a space.
#
# Then a first order transition matrix of order 27X27 is constructed where the (i,j)th element contains the number of times 
# in this given text the character (either an alphabet or a space in this case) denoted by the jth column appears after the i
# character represented by the ith row.
# Since this text forms a very large corpus, we can assume that this matrix
# gives us the first order transitions for the English Language. 
#
# However instead of storing the frequency of occurence each character, we store the log of probabilities

def generateTransitionMatrix(filename):

	print '\n....Generating the transition matrix....\n';
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

	for i in range (1, 28):
		for j in range (1,28):
			if(M[i][j] == 0):
				M[i][j] = -12;
			else:
				M[i][j]= math.log(M[i][j]);

	numpy.savetxt('transitionMatrix_log_of_prob.txt', M, fmt='%.4f');	


# This function determines whether the character is a letter or not.
def isLetter(ch):
	if ((ch >= 'A' and  ch <= 'Z') or (ch >= 'a' and  ch<='z') or ch == ' '):
		return True;
	else:
		return False;
# This function applies the metropolis algoritm to decipher the encoded text.
def decipherText(M, encText):
	f = numpy.zeros(28, dtype = numpy.int);
	for i in range(1,28):
		f[i] = i;		
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
		r+=1;			
		p = p1;
		p_list.append(p);
		f_list.append(f);
		if (r==2500):
			break;

	return (p, decrypt(encText, f), p_list);

# This function calculates the plausibility of a given function (how much is the 
# predicted mapping closer to the original mapping )
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
	
	return p;

# This function decrypts the encoded text according to our predicted mapping
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

# This function performs random transposition of two values of our prediction function
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

# This is the function to encoded any given text of English language
def generateCiphers(normaltxt):

	formattedText='';

	for ch in normaltxt:
		if(ch == '\n' or ch == '.' or ch == ','):
			formattedText+=' ';
		elif(isLetter(ch)):
			formattedText+=ch;

	formattedText = formattedText.lower();

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
	return encryptedText;



def main():

	# Uncomment the line below which calls the generateTransitionMatrix function, if you are using this code
	# for the first time and haven't generated a matrix yet.
	# Subsequently, comment it. Otherwise the matrix will be generated everytime.

	#generateTransitionMatrix('Austen.txt');	

	print '\n!!!!Transition matrix generated, proceeding with the Metropolis algorithm!!!!';

	M = numpy.zeros((27,27), dtype = numpy.float);
	M = numpy.loadtxt('transitionMatrix_log_of_prob.txt');
	# place the text which you want to encode in normaltxt.
	normaltxt = 'one should first of all hear about the Lord. When one has perfectly and scrutinizingly heard, one must glorify His acts and deeds, and thus it will become possible to remember constantly the transcendental nature of the Lord. Hearing about and glorifying the Lord are identical with the transcendental nature of the Lord, and by so doing, one will be always in the association of the Lord.';
	# The generateCiphers function will generate a subsitution cipher for the normaltxt by replacing each letter
	# with the letter after it in the English Alphabet. And letter 'z' will be replaced by 'a'. Spaces will remain at the same place.
	encryptedText = generateCiphers(normaltxt);
	best_p = -999999;
	best_p_list = [];
	best_decryption = '';
	print '\n The normal text is : \n';
	print normaltxt;
	print '\n The encoded version of above text is : \n';
	print encryptedText;
	# Alternatively, if you already have a substitution cipher, you can pass it directly to the decipherText function below.
	
	# We run several rounds of the algorithm, to get the best results. 

	print '\n....This may take almost a minute....\n'
	for i in range(0,15):
		(p, decryptedTxt, p_list) = decipherText(M, encryptedText);
		#print p, decryptedTxt;
		if(p>best_p):
			best_p = p;
			best_p_list = p_list;
			best_decryption = decryptedTxt;


	print '\n And the decrypted Text is : \n';
	print best_decryption;
	print '\n---If you did not get the correct result, just run it once more and you will get it---\n'
	print '\n---Kindly close the graph window to terminate the process---\n'
	# Plotting the values of plausibility parameter versus the number of steps (2500).
	plt.plot(list(range(1,2500)),best_p_list);
	plt.ylabel('P');
	plt.xlabel('steps');
	plt.show();

if __name__ == '__main__':
	main();

