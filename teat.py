"""
该代码仅供测试，不作为代码主体使用
具体运行逻辑如下
"""


import checkers


def main():
    game = checkers.Game(loop_mode=True)
    game.setup()



    while True:  # 主游戏循环
        if game.turn == checkers.RED:
            game.player_turn()  # 不再传递参数
        else:
            game.player_turn()  # 不再传递参数

        game.update()

        if game.endit:
            break

if __name__ == "__main__":
    main()