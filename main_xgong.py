from env_xgong import *
import time
import heapq


class Node:
    def __init__(self, env, ptr, g, h):
        self.env = env
        self.ptr = ptr
        self.g = g
        self.h = h
        self.f = g + h

    def __lt__(self, other):
        return self.f < other.f

    def __int__(self):
        return env_into_int(self.env)


def env_into_int(env):
    env_ = env.flatten(order='C')
    str_ = ''
    for i in range(len(env_)):
        str_ += str(env_[i]).zfill(2)
    str_ = int(str_)
    return str_


def A_remake_xgong(env, inv, des_env):
    # A算法
    # (1) 把起始节点S放入Open表，记f(S)=h(S)，令Closed为空表。
    step = 0
    open_list = []
    closed_list = []
    path = []
    open_list_f = []
    open_list_env = []
    closed_list_env = []

    cur_env = Node(env, None, step, h_function(env, inv, des_env))
    open_list.append(cur_env)
    open_list_f.append(cur_env.f)
    open_list_env.append(env_into_int(cur_env.env))

    # (2) 若Open表为空表，则算法失败。
    while 1:
        if len(open_list) == 0:
            print("Fail to find a solution!")
            return 1

        step += 0  # g(n)选取与课件不一致
        # print(step, len(open_list))

        # (3) 选取Open表中具有最小f值的节点为最佳节点BestNode，并把它放入Closed表。
        min_env = open_list_f.index(min(open_list_f))
        best_node = open_list[min_env]
        closed_list.append(open_list[min_env])
        closed_list_env.append(open_list_env[min_env])
        del open_list[min_env]
        del open_list_f[min_env]
        del open_list_env[min_env]

        # (4) 若BestNode为一目标节点，则成功得到一解。
        if env_into_int(best_node.env) == env_into_int(des_env[inv]):
            # print("Find a ", inv, "- type solution!")
            print('open: ', len(open_list), 'closed: ', len(closed_list))
            while best_node:
                path.append(best_node.env)
                best_node = best_node.ptr
            # for i in range(len(path)):
            # print(path[- i - 1])
            return 0, (path[::-1])[1:]

        # (5) 若BestNode不是目标节点，则扩展之，产生后继节点Successor。
        success_list = success(best_node.env)

        # (6) 对每个Successor进行下列过程：
        for i in range(len(success_list)):
            successor = np.copy(success_list[i])
            env_str = env_into_int(successor)

            # (a) 建立从Successor返回BestNode的指针。
            # (b) 计算g(Successor)=g(best_node)+c(Successor, best_node) 。
            success_node = Node(successor, best_node, step, h_function(successor, inv, des_env))

            # (c) 如果Successor在Open表中，则称Open表中该节点为Old。
            is_in_list = False
            ret = False

            # (d) 比较新旧路径代价。如果g(Successor)<g(Old)，则用Successor替换Old节点。
            if env_str in set(open_list_env):
                is_in_list = True
                j = open_list_env.index(env_into_int(successor))
                if success_node < open_list[j]:
                    open_list[j] = success_node
                else:
                    ret = True

            # (e) 若与Old节点的代价低或一样，则停止扩展节点。
            # (f) 若Successor不在Open表中，则看其是否在Closed表中。
            if not is_in_list:
                if env_str in set(closed_list_env):
                    is_in_list = True
                    j = closed_list_env.index(env_into_int(successor))
                    if success_node < closed_list[j]:
                        closed_list[j] = success_node
                    else:
                        ret = True

            # (h) 若Successor既不在Open表中，又不在Closed表中，则把它放入Open表中，然后转向(7)。
            # (7) 计算该节点f值。
            if not is_in_list and not ret:
                open_list.append(success_node)
                open_list_f.append(success_node.f)
                open_list_env.append(env_into_int(success_node.env))


def C_remake_xgong(env, inv, des_env):
    # A算法
    # (1) 把起始节点S放入Open表，记f(S)=h(S)，令Closed为空表。
    step = 0
    open_list = []
    closed_list = []
    path = []
    open_list_env = []
    closed_list_env = []

    cur_env = Node(env, None, step, h_function(env, inv, des_env))
    open_list.append(cur_env)
    open_list_env.append(env_into_int(cur_env.env))

    # (2) 若Open表为空表，则算法失败。
    while 1:
        if len(open_list) == 0:
            print("Fail to find a solution!")
            return 1

        step += 0  # g(n)选取与课件不一致
        # print(step, len(open_list))

        # (3) 选取Open表中具有最小f值的节点为最佳节点BestNode，并把它放入Closed表。
        heapq.heapify(open_list)
        best_node = open_list[0]
        closed_list.append(best_node)
        closed_list_env.append(int(best_node))
        open_list.remove(best_node)
        open_list_env.remove(int(best_node))

        # (4) 若BestNode为一目标节点，则成功得到一解。
        if env_into_int(best_node.env) == env_into_int(des_env[inv]):
            print('open: ', len(open_list), 'closed: ', len(closed_list))
            while best_node:
                path.append(best_node.env)
                best_node = best_node.ptr
            return 0, (path[::-1])[1:]

        # (5) 若BestNode不是目标节点，则扩展之，产生后继节点Successor。
        success_list = success(best_node.env)

        # (6) 对每个Successor进行下列过程：
        for i in range(len(success_list)):
            successor = np.copy(success_list[i])
            env_str = env_into_int(successor)

            # (a) 建立从Successor返回BestNode的指针。
            # (b) 计算g(Successor)=g(best_node)+c(Successor, best_node) 。
            success_node = Node(successor, best_node, step, h_function(successor, inv, des_env))

            # (c) 如果Successor在Open表中，则称Open表中该节点为Old。
            is_in_list = False
            ret = False

            # (d) 比较新旧路径代价。如果g(Successor)<g(Old)，则用Successor替换Old节点。
            if env_str in open_list_env:
                is_in_list = True
                j = open_list_env.index(env_str)
                if success_node.g < open_list[j].g:
                    open_list[j] = success_node
                else:
                    ret = True

            # (e) 若与Old节点的代价低或一样，则停止扩展节点。
            # (f) 若Successor不在Open表中，则看其是否在Closed表中。
            if not is_in_list:
                if env_str in closed_list_env:
                    is_in_list = True
                    j = closed_list_env.index(env_str)
                    if success_node.g < closed_list[j].g:
                        closed_list[j] = success_node
                    else:
                        ret = True

            # (h) 若Successor既不在Open表中，又不在Closed表中，则把它放入Open表中，然后转向(7)。
            # (7) 计算该节点f值。
            if not is_in_list and not ret:
                open_list.append(success_node)
                open_list_env.append(env_str)


def B_remake_xgong(env_, inv_):
    [row, column] = env_.shape
    if row == 2 and column == 2:
        return []

    path = []
    env = np.copy(env_)
    if inv_ == 1:
        if env[0][0] != 0 and env[0][1] != 0:
            change_env_(env, [0, 0], [0, 1])
        else:
            change_env_(env, [1, 0], [1, 1])
    for i in range(1, (row - 2) * column + 1):
        if 0 < i % column < column - 1:
            des_row, des_column = int((i - 1) / column), int((i - 1) % column)
            env, path = move(env, i, des_row, des_column, path)
        elif i % column == 0:
            des_row, des_column = int((i - 1) / column), int((i - 1) % column) - 1
            env, path = move(env, i, des_row, des_column, path)
            if env[des_row][-1] == i - 1:
                env, path = move_zero(env, i / column - 1, path)
                env, path = move_zero(env, i / column - 1, path)
                des_row, des_column = int((i - 1) / column), int((i - 1) % column) - 1
                env, path = move(env, i, des_row, des_column, path)
            des_row, des_column = int((i - 1) / column) + 1, int((i - 1) % column) - 1
            env, path = move(env, i - 1, des_row, des_column, path)
            env, path = move_zero(env, i / column - 1, path)

    env_u = env[0:-2]
    env_b = env[-2:]
    min_temp = np.min(env_b[env_b != 0]) - 1
    env_b = env_b - min_temp
    env_b[env_b < 0] = 0

    des = np.arange(env_b.shape[0] * env_b.shape[1]).reshape((env_b.shape[0], env_b.shape[1])) + 1
    des[-1][-1] = 0
    des = np.array([des])

    _, p = A_remake_xgong(env_b, 0, des)
    for i in range(len(p)):
        p[i] += min_temp
        p[i][p[i] == min_temp] = 0
        p[i] = np.vstack([env_u, p[i]])
    path += p
    return path


def counter(env_):
    path = []
    zx, zy = np.argwhere(env_ == 0)[0]
    env = np.copy(env_)
    if zx == 0 and zy == 0:
        env = change_env(env_, [0, 0], [0, 1])
        path.append(env_)
    elif zx == 0 and zy == 1:
        env = change_env(env_, [0, 1], [1, 1])
        path.append(env_)
    elif zx == 1 and zy == 0:
        env = change_env(env_, [1, 0], [0, 0])
        path.append(env_)
    else:
        env = change_env(env_, [1, 1], [1, 0])
        path.append(env_)
    return path, env


def D_remake_xgong(env_, inv_):
    [row, column] = env_.shape
    if row == 2 and column == 2:
        q = []
        while not (env_[1][0] == np.max(env_) and env_[1][1] == 0):
            q_, env_ = counter(env_)
            q += q_
        q_, env_ = counter(env_)
        q += q_
        return q

    path = []
    env = np.copy(env_)
    if inv_ == 1:
        if env[0][0] != 0 and env[0][1] != 0:
            change_env_(env, [0, 0], [0, 1])
        else:
            change_env_(env, [1, 0], [1, 1])
    for i in range(1, (row - 2) * column + 1):
        if 0 < i % column < column - 1:
            des_row, des_column = int((i - 1) / column), int((i - 1) % column)
            env, path = move(env, i, des_row, des_column, path)
        elif i % column == 0:
            des_row, des_column = int((i - 1) / column), int((i - 1) % column) - 1
            env, path = move(env, i, des_row, des_column, path)
            if env[des_row][-1] == i - 1 or env[des_row + 1][-1] == i - 1:
                env, path = move_zero(env, i / column - 1, path)
                env, path = move_zero(env, i / column - 1, path)
                des_row, des_column = int((i - 1) / column), int((i - 1) % column) - 1
                env, path = move(env, i, des_row, des_column, path)
            des_row, des_column = int((i - 1) / column) + 1, int((i - 1) % column) - 1
            env, path = move(env, i - 1, des_row, des_column, path)
            env, path = move_zero(env, i / column - 1, path)

    env_u = env[0:-2]
    env_b = env[-2:]
    min_temp = np.min(env_b[env_b != 0]) - 1
    env_b = env_b - min_temp

    for i in range(2):
        for j in range(column):
            if 0 < env_b[i][j] <= column:
                env_b[i][j] = env_b[i][j] * 2 - 1
            elif env_b[i][j] > column:
                env_b[i][j] = (env_b[i][j] - column) * 2

    env_b[env_b < 0] = 0

    p = D_remake_xgong(env_b.T, 0)
    p = [x.T for x in p]

    for k in p:
        for i in range(2):
            for j in range(column):
                if k[i][j] % 2 == 0 and k[i][j] != 0:
                    k[i][j] = k[i][j] / 2 + column
                elif k[i][j] % 2 == 1:
                    k[i][j] = (k[i][j] + 1) / 2

    for i in range(len(p)):
        p[i] += min_temp
        p[i][p[i] == min_temp] = 0
        p[i] = np.vstack([env_u, p[i]])

    path += p
    return path


if __name__ == '__main__':
    # np.random.seed(42)
    time_0 = time.time()
    M, N = 5, 5
    env = init_env(M, N)
    # env = np.array([[1, 19, 5, 3, 8],
    #                 [15, 4, 21, 24, 10],
    #                 [12, 20, 16, 14, 23],
    #                 [18, 9, 6, 11, 7],
    #                 [0, 13, 17, 2, 22]])
    des_env = des_env(M, N)
    if invert_env(env) == invert_env(des_env[0]):
        inv = 0
    else:
        inv = 1
    print(env)
    print("inv:", inv)
    # _, path = C_remake_xgong(env, inv, des_env)
    path = D_remake_xgong(env, inv)
    print(len(path))
    time_1 = time.time()
    print(time_1 - time_0)
