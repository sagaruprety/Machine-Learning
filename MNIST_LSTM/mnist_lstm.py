import csv
import tensorflow as tf
import numpy as np

lstm_size  = 400
#num_layers = 4
n_input = 28
n_steps = 28
n_classes = 10
training_epochs = 40
training_iters = 100000
batch_size = 100
learning_rate = 0.001
x = tf.placeholder("float", [None, n_input, n_steps])
y = tf.placeholder("float", [None, n_classes])

def rnn(x):
 	x = tf.transpose(x, [1,0,2])
	x = tf.reshape(x, [-1, n_input])
	x = tf.split(0, n_steps, x)
	lstm = tf.nn.rnn_cell.BasicLSTMCell(lstm_size, forget_bias = 1.0, state_is_tuple=True)
	output, state = tf.nn.rnn(lstm, x, dtype=tf.float32)
	w_out = tf.Variable(tf.random_normal([lstm_size, n_classes]))
	b_out = tf.Variable(tf.random_normal([n_classes]))
	return (tf.matmul(output[-1], w_out) + b_out)

pred = rnn(x)
cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(pred, y))
optimize = tf.train.AdamOptimizer(learning_rate = learning_rate).minimize(cost)

init  = tf.initialize_all_variables()
pred_var = tf.Variable(pred, name="pred_var")
saver = tf.train.Saver({"digit_recognition_model": pred_var})
#config=tf.ConfigProto(inter_op_parallelism_threads=4, intra_op_parallelism_threads=4)
with tf.Session() as sess:
	sess.run(init)
	with open('train_digit.csv', 'r') as f1:
		reader = csv.reader(f1)
		next(reader, None)
		train = np.array(list(reader))
	with open('test_digit.csv', 'r') as f2:
		reader = csv.reader(f2)
		next(reader, None)
		test = np.array(list(reader))
	training_set_size = len(train)
	print 'training set size ', training_set_size
	num_batches = training_set_size/batch_size
	for epoch in range(training_epochs):
		step  = 0
		avg_cost = 0.
		for i in range(num_batches):
			batch_x = train[step:step+batch_size,1:].reshape(batch_size, 28, 28)
			batch_y = np.zeros((batch_size,10))
			c = 0
			while c < batch_size:
			 	batch_y[c][int(train[step+c][0])] = 1
			 	c+=1
			_, cst = sess.run([optimize,cost], feed_dict = {x:batch_x, y:batch_y})
			step+=batch_size
			avg_cost+= cst
		if (step%batch_size==0):
			print "epoch, cost", (epoch, avg_cost/step)
		perm = np.arange(training_set_size)
		np.random.shuffle(perm)
		train = train[perm]
	print("Optimization Finished!")
	with open('cross_validation.csv') as f3:
		cv_set = np.array(list(csv.reader(f3)))
	cv_x = cv_set[:,1:].reshape(len(cv_set), 28, 28)
	accuracy = tf.reduce_mean(tf.cast(tf.equal(tf.argmax(pred, 1), cv_set[:,0]), "float"))
	print accuracy.eval({x:cv_x})

	predict  = tf.argmax(pred, 1)
	prediction_values =  predict.eval({x:test.reshape(len(test), 28, 28)})
	f = open('submission.csv', 'wb')
	s = 1;
	for l in prediction_values:
		f.write(str(s)+','+str(l)+'\n')
		s+=1
	f.close()
