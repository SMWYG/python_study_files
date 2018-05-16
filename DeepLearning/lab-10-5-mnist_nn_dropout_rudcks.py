########################################################################################################################
## ▣ 가중치, 편향 파라미터 초기화
##  - weight 는 layer 의 입출력 node 수에 따라 적응적으로 normal distribution 의 variance 를 정해주는 것이 좋다.
##  - Bias 는 아주 작은 상수값으로 초기화 해주는 것이 낫다.
##  - 따라서, weight 초기화 방법 후보로 normal, truncated_normal, xavier, he 방법을 선정하고,
##    bias 초기화 방법 후보로 normal, zero 방법을 선정하였다.
##  - no batch normalization 인 경우 he weight 에 bias 0 으로 초기화 한 경우가 가장 성능이 좋았다.
##  - batch normalization 인 경우에는 no batch normalization 인 경우보다 He 초기값인 경우 약 3~4 % 정도 성능 향상이 있다.
##  ⊙ 초기화 방법
##   1. with constant
##    - tf.Variable(tf.zeros([784, 10])) : 0 으로 초기화
##    - tf.Variable(tf.constant(0.1, [784, 10])) : 0.1 로 초기화
##   2. with normal distribution
##    - tf.Variable(tf.random_normal([784, 10])) : 평균 0, 표준편차 1 인 정규분포 값
##   3. with truncated normal distribution
##    - tf.truncated_normal([784, 10], stddev=0.1) : 평균 0, 표준편차 0.1 인 정규분포에서 샘플링 된 값이 2*stddev 보다 큰 경우 해당 샘플을 버리고 다시 샘플링하는 방법.
##   4. with Xavier initialization
##    - tf.get_variable('w1', shape=[784, 10], initializer=tf.contrib.layers.xavier_initializer())
##   5. with He initialization
##    - tf.get_variable('w1', shape=[784, 10], initializer=tf.contrib.layers.variance_scaling_initializer())
##
## ▣ tf.nn.conv2d(
##   input,                  : 4-D 입력 값 [batch, in_height, in_width, in_channels]
##   filter,                 : 4-D 필터 값 [filter_height, filter_width, in_channels, out_channels]
##   strides,                : 길이 4의 1-D 텐서. (4차원 입력이어서 각 차원마다 스트라이드 값을 설정), 기본적으로 strides = [1, stride, stride, 1] 로 설정한다.
##   padding,                : 'SAME' or 'VALID' 둘 중의 하나의 값을 가진다. (스트라이드가 1x1 인 경우에만 동작.)
##   use_cudnn_on_gpu=None,  : GPU 사용에 대한 bool 값.
##   data_format=None,       : 'NHWC' : [batch, height, width, channels], 'NCHW' : [batch, channels, height, width]
##   name=None               : 연산에 대한 이름 설정.
##   )
##  1. 2-D matrix 형태로 필터를 납작하게 만든다. (filter_height * filter_width * in_channels, output_channels]
##  2. 가상 텐서 형태로 형상화하기 위해 입력 텐서로부터 이미지 패치들을 추출한다. [batch, out_height, out_width, filter_height * filter_width * in_channels]
##  3. 각 패치에 대해 필터 행렬과 이미지 패치 벡터를 오른쪽으로 행렬곱 연산을 수행한다.
##
## ▣ tf.nn.max_pool(
##   value,             : 4-D 텐서 형태 [batch, height, width, channels], type : tf.float32
##   ksize,             : 입력 값의 각 차원에 대한 윈도우 크기.
##   strides,           : 입력 값의 각 차원에 대한 sliding 윈도우 크기.
##   padding,           : 'SAME' :  output size => input size, 'VALID' : output size => ksize - 1
##   data_format='NHWC' : 'NHWC' : [batch, height, width, channels], 'NCHW' : [batch, channels, height, width]
##   name=None          : 연산에 대한 이름 설정.
##   )
##  1. 입력 값에 대해 윈도우 크기 내에서의 가장 큰 값을 골라서 차원을 축소 시키는 함수.
##
## ▣ 경사 감소법
##  1. SGD : 이전 가중치 매개 변수에 대한 손실 함수 기울기는 수치 미분을 사용해 구하고 기울기의 학습률만큼 이동하도록 구현하는 최적화 알고리즘.
##           wi ← wi ? η(∂E / ∂wi), η : 학습률
##   - tf.train.GradientDescentOptimizer(learning_rate=0.1).minimize(cost)
##  2. Momentum
##   - tf.train.MomentumOptimizer
##  3. AdaGrad
##   - tf.train.AdagradOptimizer
##  4. ADAM
##   - tf.train.AdamOptimizer
##  5. Adadelta
##   - tf.train.AdadeltaOptimizer
##  6. RMSprop
##   - tf.train.RMSPropOptimizer
##  7. Etc
##   - tf.train.AdagradDAOptimizer
##   - tf.train.FtrlOptimizer
##   - tf.train.ProximalGradientDescentOptimizer
##   - tf.train.ProximalAdagradOptimizer
########################################################################################################################

import tensorflow as tf
import random
import matplotlib.pyplot as plt
import numpy as np

# mnist 데이터를 받아오기 위해 import
from tensorflow.examples.tutorials.mnist import input_data
def plotImage(image):
    """image array를 plot으로 보여주는 함수
    Args:
        image (2-D or 3-D array): (H, W) or (H, W, C)
    """
    image = np.squeeze(image)
    shape = image.shape

    if len(shape) == 2:
        plt.imshow(image, cmap="gray")
    else:
        plt.imshow(image)
    plt.show()

tf.set_random_seed(777)  # reproducibility

mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)
# Check out https://www.tensorflow.org/get_started/mnist/beginners for
# more information about the mnist dataset

# parameters
learning_rate = 0.001
training_epochs = 1
batch_size = 100

# input place holders
# mnist 이미지  width, height 크기가 (28,28)이기때문에 28x28인 784가 dimension이 된다.
X = tf.placeholder(tf.float32, [None, 784])
# one hot encoding되어 있기 때문에 차원의 수는 10이 된다.
Y = tf.placeholder(tf.float32, [None, 10])

# dropout 비율
# dropout (keep_prob) rate  0.7 on training, but should be 1 for testing
keep_prob = tf.placeholder(tf.float32)

# weights & bias for nn layers
# http://stackoverflow.com/questions/33640581/how-to-do-xavier-initialization-on-tensorflow

# Layer 1
W1 = tf.get_variable("W1", shape=[784, 512],
                     initializer=tf.contrib.layers.xavier_initializer())
b1 = tf.Variable(tf.random_normal([512]))
L1 = tf.nn.relu(tf.matmul(X, W1) + b1)
L1 = tf.nn.dropout(L1, keep_prob=keep_prob)

# Layer 2
W2 = tf.get_variable("W2", shape=[512, 512],
                     initializer=tf.contrib.layers.xavier_initializer())
b2 = tf.Variable(tf.random_normal([512]))
L2 = tf.nn.relu(tf.matmul(L1, W2) + b2)
L2 = tf.nn.dropout(L2, keep_prob=keep_prob)

# Layer 3
W3 = tf.get_variable("W3", shape=[512, 512],
                     initializer=tf.contrib.layers.xavier_initializer())
b3 = tf.Variable(tf.random_normal([512]))
L3 = tf.nn.relu(tf.matmul(L2, W3) + b3)
L3 = tf.nn.dropout(L3, keep_prob=keep_prob)

# Layer 4
W4 = tf.get_variable("W4", shape=[512, 512],
                     initializer=tf.contrib.layers.xavier_initializer())
b4 = tf.Variable(tf.random_normal([512]))
L4 = tf.nn.relu(tf.matmul(L3, W4) + b4)
L4 = tf.nn.dropout(L4, keep_prob=keep_prob)

# Layer 5
W5 = tf.get_variable("W5", shape=[512, 10],
                     initializer=tf.contrib.layers.xavier_initializer())
b5 = tf.Variable(tf.random_normal([10]))
hypothesis = tf.matmul(L4, W5) + b5

# define cost/loss & optimizer
# (reduce)차원을 줄이면서 mean 값(batch당 1개의 output으로) 출력
cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=hypothesis, labels=Y))
optimizer = tf.train.AdamOptimizer(learning_rate=learning_rate).minimize(cost)

# initialize
sess = tf.Session()
sess.run(tf.global_variables_initializer())

# train my model
for epoch in range(training_epochs):
    avg_cost = 0

    # 총 배치학습 = 총데이터수/배치사이즈
    total_batch = int(mnist.train.num_examples / batch_size)
    for i in range(total_batch):

        # image(vector)와 label 분류
        batch_xs, batch_ys = mnist.train.next_batch(batch_size)

        # mnist 이미지 3장 확인 해보기
        # if epoch == 0 and i < 3:
        #     plotImage(batch_xs[random.randint(0, batch_size - 1)].reshape(-1, 28, 28))

        # hypothesis shape 확인 해보기
        # feed_dict2 = {X: batch_xs, keep_prob: 0.7}
        # print(sess.run([hypothesis], feed_dict=feed_dict2)[0].shape)

        feed_dict = {X: batch_xs, Y: batch_ys, keep_prob: 0.7}
        c, _ = sess.run([cost, optimizer], feed_dict=feed_dict)
        # print(c)
        avg_cost += c / total_batch

    print('Epoch:', '%04d' % (epoch + 1), 'cost =', '{:.9f}'.format(avg_cost))

print('Learning Finished!')

# Test model and check accuracy
correct_prediction = tf.equal(tf.argmax(hypothesis, 1), tf.argmax(Y, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

# correct_prediction 디버깅 코드
# print( sess.run(correct_prediction, feed_dict={X:mnist.test.images, Y: mnist.test.labels, keep_prob:1}) )
# output: [ True  True  True ...,  True  True  True]

# 10,000개 테스트 데이터에 대한 Accuracy
print('Accuracy:', sess.run(accuracy, feed_dict={
      X: mnist.test.images, Y: mnist.test.labels, keep_prob: 1}))

# Get one and predict
r = random.randint(0, mnist.test.num_examples - 1)
print("Label: ", sess.run(tf.argmax(mnist.test.labels[r:r + 1], 1)))
print("Prediction: ", sess.run(
    tf.argmax(hypothesis, 1), feed_dict={X: mnist.test.images[r:r + 1], keep_prob: 1}))


'''
Epoch: 0001 cost = 0.447322626
Epoch: 0002 cost = 0.157285590
Epoch: 0003 cost = 0.121884535
Epoch: 0004 cost = 0.098128681
Epoch: 0005 cost = 0.082901778
Epoch: 0006 cost = 0.075337573
Epoch: 0007 cost = 0.069752543
Epoch: 0008 cost = 0.060884363
Epoch: 0009 cost = 0.055276413
Epoch: 0010 cost = 0.054631256
Epoch: 0011 cost = 0.049675195
Epoch: 0012 cost = 0.049125314
Epoch: 0013 cost = 0.047231930
Epoch: 0014 cost = 0.041290121
Epoch: 0015 cost = 0.043621063
Learning Finished!
Accuracy: 0.9804
'''





