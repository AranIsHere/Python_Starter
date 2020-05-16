favorite_language = "python "
# 暂时性删除
print(favorite_language.rstrip())
# 永久性删除，变量值回传
favorite_language = favorite_language.rstrip()


favorite_language2 = " java "
# 头部空白删除
favorite_language2 = favorite_language2.lstrip()
# 尾部空白删除
favorite_language2 = favorite_language2.rstrip()
# 两端空白
favorite_language2 = favorite_language2.strip()
print(favorite_language2)

