import numpy as np


# 目标状态的矩阵表示
def des_env(M, N):
    env = np.arange(M * N)
    env = env.reshape((M, N))
    env = env + 1
    env[-1][-1] = 0
    env_ = np.copy(env)
    where_one = np.argwhere(env_ == 1)[0]
    where_two = np.argwhere(env_ == 2)[0]
    env_[where_one[0]][where_one[1]] = 2
    env_[where_two[0]][where_two[1]] = 1
    env = np.vstack([[env], [env_]])
    return env


# # 目标状态的向量表示
# def state(M, N):
#     first_state = np.arange(1, M * N)
#     second_state = np.copy(first_state)
#     second_state[0] = 2
#     second_state[1] = 1
#     state = np.vstack([first_state, second_state])
#     return state


# 环境初始化
def init_env(M, N):
    env = np.arange(M * N)
    np.random.shuffle(env)
    env = env.reshape(M, N)
    return env


# 计算逆序数，判断目标状态
def invert_env(env):
    inv = 0
    m, n = env.shape[0], env.shape[1]
    zero_row = np.argwhere(env == 0)[0][0]
    flatten = env.flatten()
    flatten = flatten[flatten != 0]
    for i in range(m * n - 2):
        for j in range(i, m * n - 1):
            if flatten[j] < flatten[i]:
                inv += 1
    if n % 2 == 1:
        return inv % 2
    else:
        return (zero_row + inv) % 2


# P函数
def p_function(env, des_env, d):
    sum_p = 0
    for i in range(env.shape[0]):
        for j in range(env.shape[1]):
            cur_num = env[i][j]
            if cur_num != 0:
                des = np.argwhere(des_env[d] == cur_num)[0]
                sum_p += abs(i - des[0]) + abs(j - des[1])
    return sum_p


# S函数
# def s_function(env, des_env, d, state):
#     sum_s = 0
#     env_ = np.copy(env)
#     for i in range(1, env.shape[0], 2):
#         env_[i] = env_[i][::-1]
#     env_temp = env_.flatten()
#     des_env_ = np.copy(des_env)
#     for i in range(1, des_env.shape[0], 2):
#         des_env_[d][i] = des_env_[d][i][::-1]
#     des_temp = des_env_[d].flatten()
#     # print(env_temp, des_temp)
#     des_zero = np.argwhere(des_temp == 0)[0]
#     if env_temp[des_zero] != 0:
#         sum_s += 1
#     env_temp = np.delete(env_temp, des_zero)
#     env_temp = env_temp[env_temp != 0]
#     first = env_temp[0]
#     if d == 0:
#         st_b = state[first - 1:]
#         st_f = state[: first - 1]
#     else:
#         if first == 1:
#             st_b = state[1:]
#             st_f = [2]
#         elif first == 2:
#             st_b = state
#             st_f = []
#         else:
#             st_b = state[first - 1:]
#             st_f = state[: first - 1]
#     st = np.hstack([st_b, st_f]).astype(int)
#     for i in range(env_temp.shape[0] - 1):
#         for j in range(i, env_temp.shape[0]):
#             i_where = np.argwhere(st == env_temp[i])[0]
#             j_where = np.argwhere(st == env_temp[j])[0]
#             if i_where > j_where:
#                 sum_s += 2
#     return sum_s


# H函数
def h_function(env, d, des_env):
    # print(state)
    # print(s_function(env, des_env, d, state))
    # return 1 * p_function(env, des_env, d) + 0 * s_function(env, des_env, d, state)
    return p_function(env, des_env, d)


# 交换矩阵中两个元素的位置
def change_env(env, index, index_):
    new_env = np.copy(env)
    temp = new_env[index[0]][index[1]]
    new_env[index[0]][index[1]] = new_env[index_[0]][index_[1]]
    new_env[index_[0]][index_[1]] = temp
    return new_env


def change_env_(env, index, index_):
    temp = env[index[0]][index[1]]
    env[index[0]][index[1]] = env[index_[0]][index_[1]]
    env[index_[0]][index_[1]] = temp


# 扩展节点
def success(env):
    success_list = []
    zero_index = np.argwhere(env == 0)[0]
    # 首行
    if zero_index[0] == 0:
        # 左上角
        if zero_index[1] == 0:
            success_env = change_env(env, zero_index, np.array([0, 1]))
            success_list.append(success_env)
            success_env = change_env(env, zero_index, np.array([1, 0]))
            success_list.append(success_env)
        # 右上角
        elif zero_index[1] == env.shape[1] - 1:
            success_env = change_env(env, zero_index, np.array([0, env.shape[1] - 2]))
            success_list.append(success_env)
            success_env = change_env(env, zero_index, np.array([1, env.shape[1] - 1]))
            success_list.append(success_env)
        else:
            success_env = change_env(env, zero_index, np.array([0, zero_index[1] - 1]))
            success_list.append(success_env)
            success_env = change_env(env, zero_index, np.array([0, zero_index[1] + 1]))
            success_list.append(success_env)
            success_env = change_env(env, zero_index, np.array([1, zero_index[1]]))
            success_list.append(success_env)
    # 末行
    elif zero_index[0] == env.shape[0] - 1:
        # 左下角
        if zero_index[1] == 0:
            success_env = change_env(env, zero_index, np.array([env.shape[0] - 2, 0]))
            success_list.append(success_env)
            success_env = change_env(env, zero_index, np.array([env.shape[0] - 1, 1]))
            success_list.append(success_env)
        # 右下角
        elif zero_index[1] == env.shape[1] - 1:
            success_env = change_env(env, zero_index, np.array([env.shape[0] - 2, env.shape[1] - 1]))
            success_list.append(success_env)
            success_env = change_env(env, zero_index, np.array([env.shape[0] - 1, env.shape[1] - 2]))
            success_list.append(success_env)
        else:
            success_env = change_env(env, zero_index, np.array([env.shape[0] - 2, zero_index[1]]))
            success_list.append(success_env)
            success_env = change_env(env, zero_index, np.array([env.shape[0] - 1, zero_index[1] - 1]))
            success_list.append(success_env)
            success_env = change_env(env, zero_index, np.array([env.shape[0] - 1, zero_index[1] + 1]))
            success_list.append(success_env)
    else:
        # 首列
        if zero_index[1] == 0:
            success_env = change_env(env, zero_index, np.array([zero_index[0] - 1, 0]))
            success_list.append(success_env)
            success_env = change_env(env, zero_index, np.array([zero_index[0], 1]))
            success_list.append(success_env)
            success_env = change_env(env, zero_index, np.array([zero_index[0] + 1, 0]))
            success_list.append(success_env)
        # 末列
        elif zero_index[1] == env.shape[1] - 1:
            success_env = change_env(env, zero_index, np.array([zero_index[0] - 1, env.shape[1] - 1]))
            success_list.append(success_env)
            success_env = change_env(env, zero_index, np.array([zero_index[0], env.shape[1] - 2]))
            success_list.append(success_env)
            success_env = change_env(env, zero_index, np.array([zero_index[0] + 1, env.shape[1] - 1]))
            success_list.append(success_env)
        # 中心
        else:
            success_env = change_env(env, zero_index, np.array([zero_index[0] - 1, zero_index[1]]))
            success_list.append(success_env)
            success_env = change_env(env, zero_index, np.array([zero_index[0], zero_index[1] - 1]))
            success_list.append(success_env)
            success_env = change_env(env, zero_index, np.array([zero_index[0], zero_index[1] + 1]))
            success_list.append(success_env)
            success_env = change_env(env, zero_index, np.array([zero_index[0] + 1, zero_index[1]]))
            success_list.append(success_env)
    return success_list


# 规则移动方法
def move(env, num, des_x, des_y, p):
    path = []
    env_ = np.copy(env)
    x, y = np.argwhere(env_ == num)[0][0], np.argwhere(env_ == num)[0][1]
    zx, zy = np.argwhere(env_ == 0)[0][0], np.argwhere(env_ == 0)[0][1]
    dx, dy = int(x - des_x), int(y - des_y)
    zdx, zdy = int(zx - x), int(zy - y)
    while dx != 0 or dy != 0:
        if dx == 0:
            if zdx == 0:
                if zdy < 0:
                    if dy > 0:
                        env_ = change_env(env_, [zx, zy], [zx, zy + 1])
                    else:
                        env_ = change_env(env_, [zx, zy], [zx + 1, zy])
                        path.append(env_)
                        zx += 1
                        env_ = change_env(env_, [zx, zy], [zx, zy + 1])
                        path.append(env_)
                        zy += 1
                        env_ = change_env(env_, [zx, zy], [zx, zy + 1])
                        path.append(env_)
                        zy += 1
                        env_ = change_env(env_, [zx, zy], [zx - 1, zy])
                else:  # zdy > 0
                    if dy > 0:
                        env_ = change_env(env_, [zx, zy], [zx + 1, zy])
                    else:
                        env_ = change_env(env_, [zx, zy], [zx, zy - 1])
            elif zdx < 0:
                env_ = change_env(env_, [zx, zy], [zx + 1, zy])
            else:  # zdx > 0
                if y < env_.shape[1] - 1:
                    if zdy < -1:
                        env_ = change_env(env_, [zx, zy], [zx, zy + 1])
                    elif zdy == -1:
                        env_ = change_env(env_, [zx, zy], [zx - 1, zy])
                    else:
                        env_ = change_env(env_, [zx, zy], [zx, zy - 1])
                else:  # y == env_.shape[1] - 1
                    if zdy == 0:
                        env_ = change_env(env_, [zx, zy], [zx, zy - 1])
                    elif zdy < -1:
                        env_ = change_env(env_, [zx, zy], [zx, zy + 1])
                    else:
                        env_ = change_env(env_, [zx, zy], [zx - 1, zy])
        else:   # dx > 0
            if dy == 0:
                if zdx == 0:
                    if zdy > 1:
                        env_ = change_env(env_, [zx, zy], [zx, zy - 1])
                    elif zdy == 1:
                        env_ = change_env(env_, [zx, zy], [zx - 1, zy])
                        path.append(env_)
                        zx -= 1
                        env_ = change_env(env_, [zx, zy], [zx, zy - 1])
                    elif zdy < -1:
                        env_ = change_env(env_, [zx, zy], [zx, zy + 1])
                    else:  # zdy == -1
                        if zx < env_.shape[0] - 1:
                            env_ = change_env(env_, [zx, zy], [zx + 1, zy])
                            path.append(env_)
                            zx += 1
                            env_ = change_env(env_, [zx, zy], [zx, zy + 1])
                            path.append(env_)
                            zy += 1
                            env_ = change_env(env_, [zx, zy], [zx, zy + 1])
                            path.append(env_)
                            zy += 1
                            env_ = change_env(env_, [zx, zy], [zx - 1, zy])
                            path.append(env_)
                            zx -= 1
                            env_ = change_env(env_, [zx, zy], [zx, zy - 1])
                        else:  # zx == env_.shape[0] - 1
                            env_ = change_env(env_, [zx, zy], [zx - 1, zy])
                            path.append(env_)
                            zx -= 1
                            env_ = change_env(env_, [zx, zy], [zx, zy + 1])
                            path.append(env_)
                            zy += 1
                            env_ = change_env(env_, [zx, zy], [zx, zy + 1])
                            path.append(env_)
                            zy += 1
                            env_ = change_env(env_, [zx, zy], [zx + 1, zy])
                            path.append(env_)
                            zx += 1
                            env_ = change_env(env_, [zx, zy], [zx, zy - 1])
                elif zdx > 0:
                    if zdy == 0:
                        env_ = change_env(env_, [zx, zy], [zx, zy + 1])
                    else:
                        env_ = change_env(env_, [zx, zy], [zx - 1, zy])
                else:  # zdx < 0:
                    env_ = change_env(env_, [zx, zy], [zx + 1, zy])
            elif dy > 0:
                if zdx == 0:
                    if zdy > 1:
                        env_ = change_env(env_, [zx, zy], [zx, zy - 1])
                    elif zdy == 1:
                        if zx < env_.shape[0] - 1:
                            env_ = change_env(env_, [zx, zy], [zx + 1, zy])
                            path.append(env_)
                            zx += 1
                            env_ = change_env(env_, [zx, zy], [zx, zy - 1])
                            path.append(env_)
                            zy -= 1
                            env_ = change_env(env_, [zx, zy], [zx, zy - 1])
                            path.append(env_)
                            zy -= 1
                            env_ = change_env(env_, [zx, zy], [zx - 1, zy])
                            path.append(env_)
                            zx -= 1
                            env_ = change_env(env_, [zx, zy], [zx, zy + 1])
                        else:  # zx == env_.shape[0] - 1
                            env_ = change_env(env_, [zx, zy], [zx - 1, zy])
                            path.append(env_)
                            zx -= 1
                            env_ = change_env(env_, [zx, zy], [zx, zy - 1])
                            path.append(env_)
                            zy -= 1
                            env_ = change_env(env_, [zx, zy], [zx, zy - 1])
                            path.append(env_)
                            zy -= 1
                            env_ = change_env(env_, [zx, zy], [zx + 1, zy])
                            path.append(env_)
                            zx += 1
                            env_ = change_env(env_, [zx, zy], [zx, zy + 1])
                    else:  # zdy < 0
                        env_ = change_env(env_, [zx, zy], [zx, zy + 1])
                elif zdx > 0:
                    if zdy == 0:
                        if zy == env.shape[1] - 1:
                            env_ = change_env(env_, [zx, zy], [zx, zy - 1])
                        else:
                            env_ = change_env(env_, [zx, zy], [zx, zy + 1])
                    else:
                        env_ = change_env(env_, [zx, zy], [zx - 1, zy])
                else:  # zdx < 0:
                    env_ = change_env(env_, [zx, zy], [zx + 1, zy])
            else:  # dy < 0
                if zdx == 0:
                    if zdy < -1:
                        env_ = change_env(env_, [zx, zy], [zx, zy + 1])
                    elif zdy == -1:
                        if zx < env_.shape[0] - 1:
                            env_ = change_env(env_, [zx, zy], [zx + 1, zy])
                            path.append(env_)
                            zx += 1
                            env_ = change_env(env_, [zx, zy], [zx, zy + 1])
                            path.append(env_)
                            zy += 1
                            env_ = change_env(env_, [zx, zy], [zx, zy + 1])
                            path.append(env_)
                            zy += 1
                            env_ = change_env(env_, [zx, zy], [zx - 1, zy])
                            path.append(env_)
                            zx -= 1
                            env_ = change_env(env_, [zx, zy], [zx, zy - 1])
                        else:  # zx == env_.shape[0] - 1
                            env_ = change_env(env_, [zx, zy], [zx - 1, zy])
                            path.append(env_)
                            zx -= 1
                            env_ = change_env(env_, [zx, zy], [zx, zy + 1])
                            path.append(env_)
                            zy += 1
                            env_ = change_env(env_, [zx, zy], [zx, zy + 1])
                            path.append(env_)
                            zy += 1
                            env_ = change_env(env_, [zx, zy], [zx + 1, zy])
                            path.append(env_)
                            zx += 1
                            env_ = change_env(env_, [zx, zy], [zx, zy - 1])
                    else:  # zdy > 0
                        env_ = change_env(env_, [zx, zy], [zx, zy - 1])
                elif zdx > 0:
                    if zdy == 0:
                        env_ = change_env(env_, [zx, zy], [zx, zy + 1])
                    else:
                        env_ = change_env(env_, [zx, zy], [zx - 1, zy])
                else:  # zdx < 0:
                    env_ = change_env(env_, [zx, zy], [zx + 1, zy])

        x, y = np.argwhere(env_ == num)[0][0], np.argwhere(env_ == num)[0][1]
        zx, zy = np.argwhere(env_ == 0)[0][0], np.argwhere(env_ == 0)[0][1]
        dx, dy = int(x - des_x), int(y - des_y)
        zdx, zdy = int(zx - x), int(zy - y)
        path.append(env_)
    return env_, p + path


# 规则移动方法-移动0元素
def move_zero(env, row, p):
    path = []
    env_ = np.copy(env)
    zx, zy = np.argwhere(env_ == 0)[0][0], np.argwhere(env_ == 0)[0][1]
    while zx < env_.shape[0] - 1:
        env_ = change_env(env_, [zx, zy], [zx + 1, zy])
        path.append(env_)
        zx += 1
    while zy < env_.shape[1] - 1:
        env_ = change_env(env_, [zx, zy], [zx, zy + 1])
        path.append(env_)
        zy += 1
    while zx > row:
        env_ = change_env(env_, [zx, zy], [zx - 1, zy])
        path.append(env_)
        zx -= 1
    env_ = change_env(env_, [zx, zy], [zx, zy - 1])
    path.append(env_)
    zy -= 1
    env_ = change_env(env_, [zx, zy], [zx + 1, zy])
    path.append(env_)
    zx += 1
    return env_, p + path
