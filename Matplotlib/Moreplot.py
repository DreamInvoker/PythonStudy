import matplotlib.pyplot as plt
import numpy as np
import matplotlib

a = np.arange(10)

# 修改字体 font.family 字体的名称 font.style 字体风格（正常或斜体italic）
# font.size 字体大小 整数字号或者large x-small
# SimHei
# 这里是全局的改动,会把坐标刻度也更改了
matplotlib.rcParams['font.family'] = 'YouYuan'

# ply.ployt(x,y.format_string, **)
# format_string 由颜色字符、风格字符、标记字符组成

plt.plot(a, a * 1.5, 'go-', a, a * 2.5, 'rx', a, a * 3.5, '*', a, a * 4.5, 'b-.')
# 在有中文输出的地方，增加一个属性：fontproperties
plt.ylabel('纵轴（值）', fontproperties='SimHei', fontsize='30')
plt.xlabel('横轴（值）')
plt.title('标题', fontproperties='SimHei')
# plt.text(2,5,r'$\mu=100$',fontsize=10)
plt.annotate(r'$\mu=100$', xy=(2, 5), xytext=(2,15),arrowprops=dict(facecolor='black',shrink=0.1,width=2))
plt.show()
