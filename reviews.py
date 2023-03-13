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
            print(n)
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