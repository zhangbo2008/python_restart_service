import subprocess

# 使用subprocess执行ls命令，并捕获输出
result = subprocess.run(['lsof', '-i',':5000'], capture_output=True, text=True)
print(1111111111)
# 打印输出结果
print(result.stdout)
aaaaa=result.stdout.split()
for i in range(len(aaaaa)):
   if aaaaa[i]=='python':
     bbbb=aaaaa[i+1]
if bbbb:
  result = subprocess.run(['kill', '-9 '+bbbb])
  print(result)

  # nohup ~/miniconda3/bin/python  backend.py  &

  result = subprocess.run(['nohup', 'python3','backend.py','&'], capture_output=True, text=True)


  print(result)
