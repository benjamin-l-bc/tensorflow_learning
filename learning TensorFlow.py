import tensorflow as tf
w1=tf.Variable(tf.random_normal([2,3]))
w2=tf.Variable(tf.random_normal([3,1]))
x=tf.constant([[2.0,1.0]])
a=tf.matmul(x,w1)
y=tf.matmul(a,w2)
sess=tf.Session()
sess.run(tf.global_variables_initializer())
print(sess.run(y))