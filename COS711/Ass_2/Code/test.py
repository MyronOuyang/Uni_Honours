import sobol
import nn
from numpy import loadtxt
import json

dataset = loadtxt('Data/training.csv', delimiter=',')
# model = nn.generate_nn_fo(0.125, 0.625, 0.375)
model = nn.generate_nn_so(0.875, 0.875)

windows = sobol.split_data_windows(dataset)
res = sobol.cross_sampling(windows, model)
print(res)

# first order param testing
# first_order_list = []
# params_list = sobol.sobol_test(8, 3, 0, 1)
# for param in params_list:
#     model = nn.generate_nn_fo(param[0], param[1], param[2])
#     windows = sobol.split_data_windows(dataset)
#     res = sobol.cross_sampling(windows, model)
#     first_order_list.append(res)
# # newlist = sorted(first_order_list, key=lambda k: k['mean_acc'])
# best_index = max(range(len(first_order_list)), key=lambda index: first_order_list[index]['mean_acc'])
# f = open("Data/results/fo.txt", "w+")
# f.write(json.dumps(first_order_list[best_index]))
# f.write(str(params_list[best_index]))
# # for item in newlist:
# #     f.write(json.dumps(item))
# f.close()
# print("Done Writing First Order List")

# # second order param testing
# second_order_list = []
# params_list = sobol.sobol_test(8, 2, 0, 1)
# for param in params_list:
#     model = nn.generate_nn_so(param[0], param[1])
#     windows = sobol.split_data_windows(dataset)
#     res = sobol.cross_sampling(windows, model)
#     second_order_list.append(res)
# # newlist = sorted(second_order_list, key=lambda k: k['mean_acc'])
# best_index = max(range(len(second_order_list)), key=lambda index: second_order_list[index]['mean_acc'])
# f = open("Data/results/so.txt", "w+")
# f.write(json.dumps(second_order_list[best_index]))
# f.write(str(params_list[best_index]))
# # for item in newlist:
# #     f.write(json.dumps(item))
# f.close()
# print("Done Writing Second Order List")


# epoch_list = []
# for i in range(10, 101):
#     windows = sobol.split_data_windows(dataset)
#     res = sobol.cross_sampling(windows, model, i)
#     epoch_list.append(res)
# newlist = sorted(epoch_list, key=lambda k: k['mean_acc'])
# f = open("Data/results/epochs.txt", "w+")
# for item in newlist:
#     f.write(item)
# f.close()
# print("Done Writing Epoch List")
