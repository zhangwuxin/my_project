# -*- coding: utf-8 -*-
import tensorflow as tf
# message = tf.constant("welcome")
# with tf.compat.v1.Session() as sess:
#     print(sess.run(message).decode())
#first_pro
sess = tf.InteractiveSession()
v_1 = tf.constant([1,2,3,5])
v_2 = tf.constant([2,1,5,3])
v_add = tf.add(v_1,v_2)
print(v_add.eval(()))
sess.close()
#TensorFlow 常亮，变量，占位符
t_1 = tf.constant(4)
t_2 = tf.constant([4,3,2])
tf.zeros([2,3],tf.int32)
