x=input("请输入用户名：")
if x=="stars":
	p=input("请输入密码：")
else:
	print("不存在此用户名！！")
	input("按enter键退出")
if p=="1412666":
	print("欢迎",x)
	input()
else:
	print("密码错了！！")
	n=input("输入1重新输入密码，其它数则退出：")
if n=="1":
	v=input("请输入密码：")
	if v=="1412666":
		print("欢迎",x)
		input()
	else:
		print("行不行啊@_@|")
		input("按enter键退出")
else:
	input()
