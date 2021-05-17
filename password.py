password = input('パスワードを入力してください:')
pass_list = list(password)
len_pass = len(password)
test_upper = test_lower = test_digit = test_punc = 0

if len_pass >= 6 and len_pass <=16 :
    for i in pass_list :
        if i.isupper() :
            test_upper = 1
        elif i.islower() :
            test_lower = 1
        elif i.isdigit() :
            test_digit = 1
        if i == '$' or i == '#' or i == '@':
            test_punc = 1
    if test_upper == 1 and test_lower == 1 and test_digit == 1 and test_punc == 1:
        print('正解')
    else :
        print('入力したのパスワードが違います、原因は：')
        if test_upper == 0 :
            print('    大文字は必要です')
        if test_lower == 0 :
            print('    小文字は必要です')
        if test_digit == 0 :
            print('    数字は必要です')
        if test_punc == 0 :
            print('    特定の記号は必要です')
else :
    print('文字数は6以上16以下にしてください')
