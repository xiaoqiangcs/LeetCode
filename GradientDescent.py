import numpy as np
import random
class GradientDecent(object):
    def get_line_data(self, sample_num=100):
        """
        y = 3*x1 + 4*x2
        :return:
        """
        x1 = np.linspace(0, 9, sample_num)
        x2 = np.linspace(4, 13, sample_num)
        x_train = np.concatenate(([x1],[x2]),axis=0).T
        y_train = np.dot(x_train,np.array([3,4]).T) #y列向量
        return x_train, y_train
    def bgd(self, x_train, y_train, step_size=0.01, max_iter_count=1000):
        sample_num, dim = x_train.shape
        y = y_train.flatten()
        w = np.ones((dim,),dtype=np.float)
        loss = 10
        iter_count = 0
        while iter_count < max_iter_count:
            loss = 0
            error = np.zeros((dim,),dtype=np.float32)
            for index in range(sample_num):
                predict_y = np.dot(w.T,x_train[index])
                for j in range(dim):
                    error[j]+=(predict_y-y_train[index])*x_train[index][j]
            for j in range(dim):
                w[j]-=step_size*error[j]/sample_num
            for index in range(sample_num):
                predict_y = np.dot(w.T,x_train[index])
                error = (1 / (sample_num* dim))*np.power((predict_y-y_train[index]),2)
                loss += error
            print("iter_count: ", iter_count, "the loss:", loss)
            iter_count += 1
        return w
    def sgd(self, x_train, y_train, step_size=0.01, max_iter_count=10):
        """
        随机梯度下降
        :param x_train:样本
        :param y: 结果value
        :param step_size: 每一接迭代的步长
        :param max_iter_count: 最大的迭代次数
        :param batch_size: 随机选取的相对于总样本的大小
        :return:
        """
        sample_num, dim = x_train.shape
        y = y_train.flatten()
        w = np.ones((dim,),dtype=np.float)
        loss = 10
        iter_count = 0
        while iter_count < max_iter_count:
            loss = 0
            error = np.zeros((dim,),dtype=np.float32)
            for index in range(sample_num):
                predict_y = np.dot(w.T,x_train[index])
                for j in range(dim):
                    error[j]+=(predict_y-y_train[index])*x_train[index][j]
                    w[j]-=step_size*error[j]/sample_num
            for index in range(sample_num):
                predict_y = np.dot(w.T,x_train[index])
                error = (1 / (sample_num* dim))*np.power((predict_y-y_train[index]),2)
                loss += error
            print("iter_count: ", iter_count, "the loss:", loss)
            iter_count += 1
        return w
    def MBGB(self, x_train, y_train, step_size=0.01, max_iter_count=10000, batch_size=0.2):
        """
        MBGD（Mini-batch gradient descent）小批量梯度下降：每次迭代使用b组样本
        :param samples:
        :param y:
        :param step_size:
        :param max_iter_count:
        :param batch_size:
        :return:
        """
        sample_num, dim = x_train.shape
        y = y_train.flatten()
        w = np.ones((dim,),dtype=np.float)
        loss = 10
        iter_count = 0
        while iter_count < max_iter_count:
            loss = 0
            error = np.zeros((dim,), dtype=np.float32)
            inde = random.sample(range(sample_num),
                              int(np.ceil(sample_num * batch_size)))
            batch_sample = x_train[inde]
            batch_y = y_train[inde]
            for index in range(len(inde)):
                predict_y = np.dot(w.T, batch_sample[index])
                for j in range(dim):
                    error[j]+=(predict_y-batch_y[index])*batch_sample[index][j]
            for j in range(dim):
                w[j]-=step_size*error[j]/sample_num
            for index in range(len(batch_sample)):
                predict_y = np.dot(w.T,batch_sample[index])
                error = (1 / (sample_num* dim))*np.power((predict_y-batch_y[index]),2)
                loss += error
            print("iter_count: ", iter_count, "the loss:", loss)
            iter_count += 1
        return w
if __name__ == '__main__':
    Test = GradientDecent()
    samples, y = Test.get_line_data()
    w = Test.MBGB(samples, y)
    print(w)  # 会很接近[3, 4]