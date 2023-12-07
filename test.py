import matplotlib.pyplot as plt

def draw_bar_chart(macro_values, human_values):
    fig, ax = plt.subplots()

    fig, ax = plt.subplots()
    bp = ax.boxplot([macro_values, human_values], patch_artist=True)

    # 매크로와 사람 두 그룹을 구분하여 각각 다른 색상을 설정합니다.
    colors = ['lightblue', 'orange']
    for patch, color in zip(bp['boxes'], colors):
        patch.set_facecolor(color)

    # 그래프에 레이블을 추가합니다.
    ax.set_xticklabels(['Macro', 'Human'])
    plt.show()

# 매크로와 사람의 상대적 전파값 (임의의 값)
macro_values = [0.26,0.288,0.272,0.275,0.285,0.295,0.255,0.3,0.2978]
human_values = [0.191,0.12,0.161,0.188,0.20,0.17]

draw_bar_chart(macro_values, human_values)