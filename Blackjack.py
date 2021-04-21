import random
import numpy as np
from sys import exit

playing_cards = {
    "♠A": 1, "♠2": 2, "♠3": 3, "♠4": 4, "♠5": 5, "♠6": 6, "♠7": 7,
    "♠8": 8, "♠9": 9, "♠10": 10, "♠J": 10, "♠Q": 10, "♠K": 10,
    "♥A": 1, "♥2": 2, "♥3": 3, "♥4": 4, "♥5": 5, "♥6": 6, "♥7": 7,
    "♥8": 8, "♥9": 9, "♥10": 10, "♥J": 10, "♥Q": 10, "♥K": 10,
    "♣A": 1, "♣2": 2, "♣3": 3, "♣4": 4, "♣5": 5, "♣6": 6, "♣7": 7,
    "♣8": 8, "♣9": 9, "♣10": 10, "♣J": 10, "♣Q": 10, "♣K": 10,
    "♦A": 1, "♦2": 2, "♦3": 3, "♦4": 4, "♦5": 5, "♦6": 6, "♦7": 7,
    "♦8": 8, "♦9": 9, "♦10": 10, "♦J": 10, "♦Q": 10, "♦K": 10
}

poker_num = 1
poker_names = list(playing_cards.keys())
poker_list = poker_names * poker_num

game_round = 1
A_list = ["♠A", "♥A", "♣A", "♦A"]
total_score = np.array([0, 0])


def random_poker(random_pokerlist):
    random.shuffle(random_pokerlist)

'''
def get_one_poker(input_poker_list):  # 發牌與叫牌
    if game_round == 1:
        return [input_poker_list.pop(random.randint(0, len(input_poker_list) - 1)),
                input_poker_list.pop(random.randint(0, len(input_poker_list) - 1))]
    else:
        return input_poker_list.pop(random.randint(0, len(input_poker_list) - 1))
'''

def get_one_poker(input_poker_list):
    return input_poker_list.pop(random.randint(0, len(input_poker_list)-1))



def init_get_poker(input_poker_list):
    return [input_poker_list.pop(random.randint(0, len(input_poker_list)-1)),
            input_poker_list.pop(random.randint(0, len(input_poker_list)-1))]


def win_or_lose(player_score, pc_score):  # 勝負判斷
    if player_score > 21 and pc_score > 21:
        print('勝負平局')
        return np.array([0, 0])
    elif player_score <= 21 and pc_score > 21:
        print('電腦點數大於21點,玩家獲勝')
        return np.array([1, 0])
    elif pc_score <= 21 and player_score > 21:
        print('玩家點數大於21點,電腦獲勝')
        return np.array([0, 1])
    else:
        if player_score > pc_score:
            print('玩家點數大於電腦,玩家獲勝')
            return np.array([1, 0])
        elif player_score < pc_score:
            print('玩家點數小於電腦,電腦獲勝')
            return np.array([0, 1])
        else:
            print('玩家點數與電腦相等,平局')
            return np.array([0, 0])


def score_count(hand_poker):
    score = 0
    for i in hand_poker:
        score += playing_cards.get(i)

    # 判斷有沒有A
    for i in hand_poker:
        if i in A_list:
            if score + 10 <= 21:
                score = score + 10
            else:
                break

    return score


def get_poker():
    if_continue = input("是否叫牌(Y/N):")
    if if_continue.upper() == 'Y':
        return True
    elif if_continue.upper() == 'N':
        return False
    else:
        print('輸入錯誤,請重新輸入')
        get_poker()


def continue_or_over(total_player, total_pc):
    if_countinue = input('是否繼續下一局(Y/N):')
    if if_countinue.upper() == 'Y':
        if len(poker_list) < 15:
            print("不好意思，剩餘撲克數過少，只有{}張，遊戲結束".format(len(poker_list)))
            print("")
            print('遊戲比分為=>玩家:電腦>>{}:{}'.format(total_player, total_pc))
            if total_player > total_pc:
                print('玩家獲勝')
            elif total_player < total_pc:
                print('電腦獲勝')
            else:
                print('總分平局')
            exit(1)
        else:
            return True
    elif if_countinue.upper() == 'N':
        print('玩家結束遊戲')
        print("")
        print('遊戲比分為=>玩家:電腦>>{}:{}'.format(total_player, total_pc))
        if total_player > total_pc:
            print('玩家獲勝')
        elif total_player < total_pc:
            print('電腦獲勝')
        else:
            print('總分平局')
        exit(1)
    else:
        print('輸入錯誤,請重新輸入')
        continue_or_over()


def round(input_poker_list):
    player_hand_poker = []
    pc_hand_poker = []

    player_get_poker = init_get_poker(input_poker_list)
    pc_get_poker = init_get_poker(input_poker_list)

    print('玩家手牌為:{}和{}'.format(player_get_poker[0], player_get_poker[1]))
    print('電腦手牌為:{}和?'.format(pc_get_poker[0]))

    player_score = score_count(player_get_poker)
    pc_score = score_count(pc_get_poker)

    player_hand_poker.extend(player_get_poker)
    pc_hand_poker.extend(pc_get_poker)

    if player_score == 21 or pc_score == 21:
        print('牌面有21點')
        return win_or_lose(player_score, pc_score)
    else:
        while True:
            if_get_player = get_poker()
            if if_get_player == True:
                new_poker = get_one_poker(input_poker_list)
                player_hand_poker.append(new_poker)
                player_score = score_count(player_hand_poker)

                print('玩家目前手牌為:{}'.format(player_hand_poker))

                if player_score > 21:
                    print('玩家手牌超過21點,玩家輸了')
                    print('電腦目前手牌為:{}'.format(pc_hand_poker))
                    return np.array([0, 1])
                else:
                    continue
            else:
                print('玩家停止叫牌')
                new_poker = get_one_poker(input_poker_list)
                pc_hand_poker.append(new_poker)
                pc_score = score_count(pc_get_poker)
            print('電腦目前手牌為{}'.format(pc_hand_poker))
            return win_or_lose(player_score, pc_score)


input('按下"Enter"後,遊戲開始')
while True:
    print('====現在是第{}局遊戲===='.format(game_round))
    random_poker(poker_list)
    curr_score = round(poker_list)
    total_score = np.add(total_score, curr_score)
    print('目前總比分為=>玩家:電腦>>{}:{}'.format(total_score[0], total_score[1]))

    game_round = game_round + 1
    if game_round > 5:
       if total_score[0] > total_score[1]:
           print('遊戲結束玩家獲勝')
       else:
           print('遊戲結束電腦獲勝')
       exit(1)
    continue_or_over(total_score[0], total_score[1])
    print("")
