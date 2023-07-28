code_list = range(500)
batch_size = 80
num_batches = len(code_list) // batch_size
for i in range(0, num_batches+1):
    batch_start = i * batch_size
    batch_end = (i + 1) * batch_size
    code_batch = code_list[batch_start:batch_end]
    print(f"Batch {i+1}:", code_batch)
    #这段代码是先假设一个500长度的代码列表，给出要分出多少段，使用range函数迭代，每次迭代都有起始和终止，使用切片获取数据，打印数据