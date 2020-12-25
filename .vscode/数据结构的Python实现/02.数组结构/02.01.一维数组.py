score = [87, 66, 90, 65, 70]
total_score = 0
for count in range(len(score)):
    print('第{}位学生的分数：{}'.format(count + 1, score[count]))
    total_score += score[count]
print('--------------------------------')
print('{}位同学的总分为：{}'.format(len(score), total_score))
