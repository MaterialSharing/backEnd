# from random import random
import random

# 获取闭区间内的随机数
rand_int = random.randint(1, 10)
print("@rand_int:", rand_int)
rand_int = random.randrange(1, 10 + 1)
print("@rand_int:", rand_int)
# 获取0-2^k次幂内的整数(左闭右开)0...(111..1)
rand_bits = random.getrandbits(2)
print("@rand_bits:", rand_bits, type(rand_bits))
# 从给定的序列(集合)中随机选中一个元素
rand_choice = random.choice(['a', 'b', 'c', 'd'])
print("@rand_choice:", rand_choice)
# 从给定的序列中返回子集
rand_choices = random.choices(population=['a', 'b', 'c', 'd'], k=3)
print("@rand_choices:", rand_choices)
# rand_shuffle = random.shuffle(['a', 'b', 'c', 'd'])# 不恰当当用法,返回None;被随机排序的对象会发生改变!
seq_mutable= ['a', 'b', 'c', 'd']
seq_mutable_bak=seq_mutable.copy()
random.shuffle(seq_mutable)

print("@rand_shuffle:", seq_mutable,'<-',seq_mutable_bak)
rand_sample_immutable = random.sample(population=('a', 'b', 'c', 'd'), k=3)
print("@rand_sample_immutable:", rand_sample_immutable,'<-',('a', 'b', 'c', 'd'))
population=('a', 'b', 'c', 'd')
seq_sample = random.sample(population, k=len(population))
print("@rand_sample_immutable2:", seq_sample, '<-', population)
