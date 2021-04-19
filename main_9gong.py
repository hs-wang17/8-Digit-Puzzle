from env_9gong import *
import time


class Node:
    def __init__(self, env, ptr, g, h):
        self.env = env
        self.ptr = ptr
        self.g = g
        self.h = h
        self.f = g + h


def A_remake_9gong(env, inv, open_list, closed_list, path):
    # A算法
    # (1) 把起始节点S放入Open表，记f(S)=h(S)，令Closed为空表。
    step = 0
    cur_env = Node(env, None, step, h_function(env, inv))
    open_list.append(cur_env)

    # (2) 若Open表为空表，则算法失败。
    while 1:
        if len(open_list) == 0:
            # print("Fail to find a solution!")
            return 1, []

        step += 0   # g(n)选取与课件不一致
        # print(step, len(open_list))

        # (3) 选取Open表中具有最小f值的节点为最佳节点BestNode，并把它放入Closed表。
        best_node = Node(None, None, step, 1e5)
        for i in range(0, len(open_list)):
            if open_list[i].f < best_node.f:
                best_node = open_list[i]
        open_list.remove(best_node)
        closed_list.append(best_node)

        # (4) 若BestNode为一目标节点，则成功得到一解。
        if np.all(best_node.env == des_env[inv]):
            # print("Find a ", inv, "- type solution!")
            print(len(open_list), len(closed_list))
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

            # (a) 建立从Successor返回BestNode的指针。
            # (b) 计算g(Successor)=g(best_node)+c(Successor, best_node) 。
            success_node = Node(successor, best_node, step, h_function(successor, inv))

            # (c) 如果Successor在Open表中，则称Open表中该节点为Old。
            is_in_list = False
            ret = False
            for j in range(len(open_list)):

                # (d) 比较新旧路径代价。如果g(Successor)<g(Old)，则用Successor替换Old节点。
                if np.all(open_list[j].env == successor):
                    is_in_list = True
                    if success_node.g < open_list[j].g:
                        open_list.remove(open_list[j])
                        open_list.append(success_node)
                    else:
                        ret = True

            # (e) 若与Old节点的代价低或一样，则停止扩展节点。
            # (f) 若Successor不在Open表中，则看其是否在Closed表中。
            if not is_in_list:
                for j in range(len(closed_list)):

                    # (g) 若Successor在Closed表中，则转向(c)。
                    if np.all(closed_list[j].env == successor):
                        is_in_list = True
                        if success_node.g < closed_list[j].g:
                            closed_list.remove(closed_list[j])
                            closed_list.append(success_node)
                        else:
                            ret = True

            # (h) 若Successor既不在Open表中，又不在Closed表中，则把它放入Open表中，然后转向(7)。
            # (7) 计算该节点f值。
            if not is_in_list and not ret:
                open_list.append(success_node)


if __name__ == '__main__':
    np.random.seed(43)
    time_0 = time.time()
    env = init_env()
    # env = np.array([[1, 2, 3],
    #                 [4, 0, 5],
    #                 [8, 7, 6]])
    inv = invert_env(env)
    print(env, inv)
    open_list = []
    closed_list = []
    path = []
    _, path = A_remake_9gong(env, inv, open_list, closed_list, path)
    print(len(path))
    time_1 = time.time()
    print(time_1 - time_0)
