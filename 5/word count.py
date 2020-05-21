# 读取一个文本，并且统计文本中单词的出现次数
def read_file():
    # 在windows环境中的编码问题，指定utf-8
    with open('addressed_data/aboutme1.txt', 'r', encoding='utf-8') as f:
        word = []  # 空列表用来存储文本中的单词

        # readlins为分行读取文本，且返回的是一个列表，每行的数据作为列表中的一个元素：
        for word_str in f.readlines():  # 如：["In this article, you will learn about Python closures, understand ",...]
            # 因为原文中每个单词都是用空格 或者逗号加空格分开的，去除原文中的逗号
            word_str = word_str.replace(',', '')
            # strip去除每行字符串数据两边的空白字符
            word_str = word_str.strip()
            # 对单行字符串通过空格进行分割，返回一个列表
            word_list = word_str.split(' ')
            # 将分割后的列表内容，添加到word空列表中
            word.extend(word_list)
        return word


def clear_account(lists):
    # 定义空字典，用来存放单词和对应的出现次数
    count_dict = {}
    # count_dict是这种形式{'': None, 'LEARN': None, 'CODING': None, 'FROM': None......}
    count_dict = count_dict.fromkeys(lists)  # 现在的lists是一个没有去重，包含所有单词的列表
    # 取出字典中的key，放到word_list1（去重后的列表中）
    word_list1 = list(count_dict.keys())

    # 然后统计单词出现的次数,并将它存入count_dict字典中
    for i in word_list1:
        # lists为没有去重的那个列表，即包含所有重复单词的列表，使用count得到单词出现次数，作为value
        count_dict[i] = lists.count(i)
    return count_dict


def sort_dict(count_dict):
    # 删除字典中''单词
    del [count_dict['']]
    # 排序,按values进行排序，如果是按key进行排序用sorted(wokey.items(),key=lambda d:d[0],reverse=True)

    # 使用lambda匿名函数用value排序,返回列表[('the', 45), ('function', 38)...这种形式]
    my_dict = sorted(count_dict.items(), key=lambda d: d[1], reverse=True)  # 临时参数d[1]是用value排序
    # 将列表转成字典<class 'dict'>
    my_dict = dict(my_dict)

    return my_dict


def main(my_dict):
    # 输出前10个
    i = 0
    # .items返回一个包含所有（键，值）元祖的列表
    for x, y in my_dict.items():
        if i < 10:
            # print('the word is "', '{}'.format(x), '"', ' and its amount is "', '{}'.format(y), '"')
            print('单词"%s",出现次数为 %s' % (x, y))
            i += 1
            continue
        else:
            break


main(sort_dict(clear_account(read_file())))