import numpy as np

# 目标状态的矩阵表示
des_env = np.array([[[1, 2, 3],
                     [8, 0, 4],
                     [7, 6, 5]],
                    [[2, 1, 3],
                     [8, 0, 4],
                     [7, 6, 5]]])
# 目标状态各数字的位置
index = np.array([[[1, 1], [0, 0], [0, 1],
                   [0, 2], [1, 2], [2, 2],
                   [2, 1], [2, 0], [1, 0]],
                  [[1, 1], [0, 1], [0, 0],
                   [0, 2], [1, 2], [2, 2],
                   [2, 1], [2, 0], [1, 0]]])
# 目标状态的向量表示
state = np.array([[[1, 2, 3, 4, 5, 6, 7, 8],
                   [2, 3, 4, 5, 6, 7, 8, 1],
                   [3, 4, 5, 6, 7, 8, 1, 2],
                   [4, 5, 6, 7, 8, 1, 2, 3],
                   [5, 6, 7, 8, 1, 2, 3, 4],
                   [6, 7, 8, 1, 2, 3, 4, 5],
                   [7, 8, 1, 2, 3, 4, 5, 6],
                   [8, 1, 2, 3, 4, 5, 6, 7]],
                  [[1, 3, 4, 5, 6, 7, 8, 2],
                   [2, 1, 3, 4, 5, 6, 7, 8],
                   [3, 4, 5, 6, 7, 8, 2, 1],
                   [4, 5, 6, 7, 8, 2, 1, 3],
                   [5, 6, 7, 8, 2, 1, 3, 4],
                   [6, 7, 8, 2, 1, 3, 4, 5],
                   [7, 8, 2, 1, 3, 4, 5, 6],
                   [8, 2, 1, 3, 4, 5, 6, 7]]])


# 环境初始化
def init_env():
    env = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8])
    np.random.shuffle(env)
    env = env.reshape(3, 3)
    return env


# 计算逆序数，判断目标状态
def invert_env(env):
    inv = 0
    flatten = env.reshape(9)
    flatten = flatten[flatten != 0]
    for i in range(7):
        for j in range(i, 8):
            if flatten[j] < flatten[i]:
                inv += 1
    return (inv + 1) % 2


# P函数
def p_function(env, d):
    sum_p = 0
    for i in range(env.shape[0]):
        for j in range(env.shape[1]):
            cur_num = env[i][j]
            if cur_num != 0:
                des = index[d][cur_num]
                sum_p += abs(i - des[0]) + abs(j - des[1])
    return sum_p


# 将矩阵转换为向量
def straighten(env, mode):
    stra = np.zeros(9)
    if mode == 0:
        stra[0] = np.copy(env[0][0])
        stra[1] = np.copy(env[0][1])
        stra[2] = np.copy(env[0][2])
        stra[3] = np.copy(env[1][2])
        stra[4] = np.copy(env[2][2])
        stra[5] = np.copy(env[2][1])
        stra[6] = np.copy(env[2][0])
        stra[7] = np.copy(env[1][0])
        stra[8] = np.copy(env[1][1])
    else:
        stra[0] = np.copy(env[0][0])
        stra[1] = np.copy(env[1][0])
        stra[2] = np.copy(env[2][0])
        stra[3] = np.copy(env[2][1])
        stra[4] = np.copy(env[2][2])
        stra[5] = np.copy(env[1][2])
        stra[6] = np.copy(env[0][2])
        stra[7] = np.copy(env[0][1])
        stra[8] = np.copy(env[1][1])
    return stra


# S函数
def s_function(env, d, mode):
    sum_s = 0
    env_temp = straighten(env, mode)
    if env_temp[8] != 0:
        sum_s += 1
    env_temp = np.delete(env_temp, 8)
    env_temp = env_temp[env_temp != 0]
    first = env_temp[0]
    for i in range(env_temp.shape[0] - 1):
        for j in range(i, env_temp.shape[0]):
            i_where = np.argwhere(state[d][int(first - 1)] == env_temp[i])[0]
            j_where = np.argwhere(state[d][int(first - 1)] == env_temp[j])[0]
            if i_where > j_where:
                sum_s += 2
    return sum_s


# H函数
def h_function(env, d):
    # return 1000
    return 1 * p_function(env, d) + 3 * s_function(env, d, 0)


# 交换矩阵中两个元素的位置
def change_env(env, index, index_):
    new_env = np.copy(env)
    temp = np.copy(new_env[index[0]][index[1]])
    new_env[index[0]][index[1]] = new_env[index_[0]][index_[1]]
    new_env[index_[0]][index_[1]] = temp
    return new_env


# 扩展节点
def success(env):
    success_list = []
    zero_index = np.argwhere(env == 0)[0]
    if np.all(zero_index == np.array([0, 0])):
        success_env = change_env(env, zero_index, np.array([0, 1]))
        success_list.append(success_env)
        success_env = change_env(env, zero_index, np.array([1, 0]))
        success_list.append(success_env)
    elif np.all(zero_index == np.array([0, 1])):
        success_env = change_env(env, zero_index, np.array([0, 0]))
        success_list.append(success_env)
        success_env = change_env(env, zero_index, np.array([0, 2]))
        success_list.append(success_env)
        success_env = change_env(env, zero_index, np.array([1, 1]))
        success_list.append(success_env)
    elif np.all(zero_index == np.array([0, 2])):
        success_env = change_env(env, zero_index, np.array([0, 1]))
        success_list.append(success_env)
        success_env = change_env(env, zero_index, np.array([1, 2]))
        success_list.append(success_env)
    elif np.all(zero_index == np.array([1, 0])):
        success_env = change_env(env, zero_index, np.array([0, 0]))
        success_list.append(success_env)
        success_env = change_env(env, zero_index, np.array([1, 1]))
        success_list.append(success_env)
        success_env = change_env(env, zero_index, np.array([2, 0]))
        success_list.append(success_env)
    elif np.all(zero_index == np.array([1, 1])):
        success_env = change_env(env, zero_index, np.array([0, 1]))
        success_list.append(success_env)
        success_env = change_env(env, zero_index, np.array([1, 0]))
        success_list.append(success_env)
        success_env = change_env(env, zero_index, np.array([1, 2]))
        success_list.append(success_env)
        success_env = change_env(env, zero_index, np.array([2, 1]))
        success_list.append(success_env)
    elif np.all(zero_index == np.array([1, 2])):
        success_env = change_env(env, zero_index, np.array([0, 2]))
        success_list.append(success_env)
        success_env = change_env(env, zero_index, np.array([1, 1]))
        success_list.append(success_env)
        success_env = change_env(env, zero_index, np.array([2, 2]))
        success_list.append(success_env)
    elif np.all(zero_index == np.array([2, 0])):
        success_env = change_env(env, zero_index, np.array([1, 0]))
        success_list.append(success_env)
        success_env = change_env(env, zero_index, np.array([2, 1]))
        success_list.append(success_env)
    elif np.all(zero_index == np.array([2, 1])):
        success_env = change_env(env, zero_index, np.array([1, 1]))
        success_list.append(success_env)
        success_env = change_env(env, zero_index, np.array([2, 0]))
        success_list.append(success_env)
        success_env = change_env(env, zero_index, np.array([2, 2]))
        success_list.append(success_env)
    elif np.all(zero_index == np.array([2, 2])):
        success_env = change_env(env, zero_index, np.array([1, 2]))
        success_list.append(success_env)
        success_env = change_env(env, zero_index, np.array([2, 1]))
        success_list.append(success_env)
    return success_list
