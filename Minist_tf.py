# -*- coding: utf-8 -*-
"""
Created on Sat Apr  7 22:12:46 2018

@author: v-beshi
"""

from tensorflow.examples.tutorials.mnist import input_data
input_node=784
output_node=10

layer1_node=500
batch_size=100
learning_rate_base=0.8
learning_rate_decay=0.99
regularization_rate=0.0001
training_steps=30000
moving_average_decay=0.99

def inference(input_tensor,avg_class,weights1,biases1):
    
