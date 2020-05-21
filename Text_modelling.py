import gensim.models.word2vec as w2v

def train_model(input_file_name, model_file_name):
    #模型训练，生成词向量
    sentences = w2v.LineSentence(input_file_name)
    model = w2v.Word2Vec(sentences, size=20, window=5, min_count=5, workers=4)
    model.save(model_file_name)

input_file_name = 'content_bias.txt' # Input Words
model_file_name = 'wPred_model.txt' # Output Model
train_model(input_file_name, model_file_name)

# Compute and evaluate similarity and probability
model = w2v.Word2Vec.load(model_file_name)
# print (model.similarity('eval','@'))
# for k in model.similar_by_word('eval'):
#     print (str(k[1])+"\t# "+k[0].decode('utf-8'))
import numpy as np
from gensim.models.word2vec import Word2Vec
import matplotlib.pyplot as plt
#import sklearn.manifold.TSNE as tsne

modelpath = 'wPred_model.txt' # 词向量模型
model = Word2Vec.load(modelpath)
sentenceFilePath = 'test.txt' # 可视化词的词典
labelFilePath = 'word.txt' # 可视化词对应显示名称

visualizeVecs = []
with open(sentenceFilePath, 'r') as f:
    for line in f:
        word = line.strip()
        vec = model[word]
        visualizeVecs.append(vec)

visualizeWords = []
with open(labelFilePath, 'r') as f:
    for line in f:
        word = line.strip()
        visualizeWords.append(word)

visualizeVecs = np.array(visualizeVecs).astype(np.float64)
#Y = tsne(visualizeVecs, 2, 200, 20.0);
## Plot.scatter(Y[:,0], Y[:,1], 20,labels);
## ChineseFont1 = FontProperties(‘SimHei‘)
#for i in xrange(len(visualizeWords)):
#    # if i<len(visualizeWords)/2:
#    #     color=‘green‘
#    # else:
#    #     color=‘red‘
#    color = 'red'
#    plt.text(Y[i, 0], Y[i, 1], visualizeWords[i],bbox=dict(facecolor=color, alpha=0.1))
#plt.xlim((np.min(Y[:, 0]), np.max(Y[:, 0])))
#plt.ylim((np.min(Y[:, 1]), np.max(Y[:, 1])))
#plt.show()


# vis_norm = np.sqrt(np.sum(temp**2, axis=1, keepdims=True))
# temp = temp / vis_norm
temp = (visualizeVecs - np.mean(visualizeVecs, axis=0))
covariance = 1.0 / visualizeVecs.shape[0] * temp.T.dot(temp)
U, S, V = np.linalg.svd(covariance)
coord = temp.dot(U[:, 0:2])
for i in range(len(visualizeWords)):
    print (i)
    print (coord[i, 0])
    print (coord[i, 1])
    color = 'red'
    plt.text(coord[i, 0], coord[i, 1], visualizeWords[i], bbox=dict(facecolor=color, alpha=0.1),
             fontsize=12)  # fontproperties = ChineseFont1
plt.xlim((np.min(coord[:, 0])-5, np.max(coord[:, 0])+5))
plt.ylim((np.min(coord[:, 1])-5, np.max(coord[:, 1])+5))
plt.savefig('pub_data/distrubution.png', format='png',dpi = 1000,bbox_inches='tight')
plt.show()
