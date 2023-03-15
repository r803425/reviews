# 寫個留言分析的程式
# 讀取檔案
# 顯示幾筆資料(1行1筆)
# 每1000筆資料，顯示進度1次
# 印出第1、2筆資料
# 計算全部資料平均長度
# 篩選資料長度 < 100的資料
# 篩選包含good的資料
# 上傳到github

data = []
n = 0
with open('reviews.txt', 'r') as f:
    for line in f:
        n += 1
        data.append(line.strip())
        if n % 100000 == 0:
            print(len(data))
print('檔案讀取完了，總共有', len(data), '筆資料')
print(data[0])
print(data[1])
print('-----------------')

sum = 0
for d in data:
    sum += len(d)
print('平均長度為 : ', sum/len(data))
print('-----------------')

checklen = []
for d in data:
    if len(d) < 100:
        checklen.append(d)
print('總共有', len(checklen), '筆資料，長度 < 100')
print(checklen[0])
print(checklen[1])
print('-----------------')

checkgood = []
for d in data:
    if 'good' in d:
        checkgood.append(d)
print('總共有', len(checkgood), '筆資料，包含good')
print(checkgood[0])
print('-----------------')

checkgood = [d for d in data if 'good' in d] # 快寫法，等於上面4行
print('總共有', len(checkgood), '筆資料，包含good')
print(checkgood[0])
print('-----------------')

checkgood = [1 for d in data if 'good' in d] # .append(1)
print('總共有', len(checkgood), '筆資料，包含good')
print(checkgood)
print(checkgood[0])
print('-----------------')

# checkbad = [d for d in data if 'bad' in d] # d 改成 'bad' in d => True/Faslse
checkbad = ['bad' in d for d in data] # if 條件非必要，可以不寫
print(checkbad)
print(checkbad[0])
print('-----------------')

checkbad = []
for d in data:
    checkbad.append('bad' in d)
print(checkbad)
print(checkbad[0])
print('-----------------')


# 文字計數
wordcount = {}
for d in data:
    words = d.split() #.split()參數留空，默認空白鍵
    for word in words:
        if word in wordcount:
            wordcount[word] += 1
        else:
            wordcount[word] = 1

for word in wordcount:
    if wordcount[word] > 1000000:
        print(word, wordcount[word])

print(len(wordcount))
print(wordcount['Ryan'])

while True:
    word = input('請輸入你要查詢的單字(輸入q/Q離開)')
    if word == 'q' or word == 'Q':
        break
    if word in wordcount:
        print(word, '出現次數為 : ', wordcount[word])
    else:
        print('此單字沒出現過')

print('感謝使用')