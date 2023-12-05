import random as rd
import time as tm
import os

from bomb_pkg.bomb_class import *
from bomb_pkg.dot_pic import *
from bomb_pkg.excep_func import *

print('플레이하는 환경이 Window 인가요 Mac 인가요?')
print("Window 면 'W' 를, Mac 이면 'M' 을 입력해주세요")
MW = input()

while (MW not in 'Mm') and (MW not in 'Ww') :
    print("'W' 또는 'M' 을 입력해주세요")
    MW = input()

if MW in 'Ww' :
    Cl = 'cls' # Window
elif MW in 'Mm' :
    Cl = 'clear' # Mac


while True :
    # ---------- 시작 세팅 ----------
    os.system(Cl)
    print('폭탄게임에 오신 걸 환영합니다!')
    while True :
        try:
            print("폭탄게임을 하려고 하는 분들의 이름을 ','(쉼표)로 구분하여 적어주세요")
            print('최소 2명에서 최대 4명까지 가능합니다!')
            name_list = input().split(',')
            os.system(Cl)

            tw_fo_name(name_list)
            dif_name(name_list)
            no_empty_name(name_list)

        except Exception as e:
            print('Error :', e)
            continue

        print(f'{len(name_list)}분의 이름이 {name_list} 가 맞으신가요?')
        print("맞으시다면 'yes', 아니라면 'no'를 입력해주세요")
        check_name = input()
        os.system(Cl)

        while (check_name != 'yes') and (check_name != 'no') :
            print('yes 또는 no 를 입력해주세요')
            check_name = input()
            os.system(Cl)

        if check_name == 'yes' :
            break
        elif check_name == 'no' :
            continue

    if len(name_list) == 2 :
        plyer1, plyer2 = Bomb_game(name_list[0]), Bomb_game(name_list[1])
        plyer_list = [plyer1, plyer2]
        main_board = main_set2
        plyer1.ply, plyer1.x, plyer1.y = 1, 64, 43
        plyer2.ply, plyer2.x, plyer2.y = 2, 1, 1

    elif len(name_list) == 3 :
        plyer1, plyer2, plyer3 = Bomb_game(name_list[0]), Bomb_game(name_list[1]), Bomb_game(name_list[2])
        plyer_list = [plyer1, plyer2, plyer3]
        main_board = main_set3
        plyer1.ply, plyer1.x, plyer1.y = 1, 64, 43
        plyer2.ply, plyer2.x, plyer2.y = 2, 1, 43
        plyer3.ply, plyer3.x, plyer3.y = 3, 1, 1

    elif len(name_list) == 4 :
        plyer1, plyer2, plyer3, plyer4 = Bomb_game(name_list[0]), Bomb_game(name_list[1]), Bomb_game(name_list[2]), Bomb_game(name_list[3])
        plyer_list = [plyer1, plyer2, plyer3, plyer4]
        main_board = main_set4
        plyer1.ply, plyer1.x, plyer1.y = 1, 64, 43
        plyer2.ply, plyer2.x, plyer2.y = 2, 1, 43
        plyer3.ply, plyer3.x, plyer3.y = 3, 1, 1
        plyer4.ply, plyer4.x, plyer4.y = 4, 64, 1


    print('좋습니다')
    print('그럼 게임을 시작하겠습니다')
    tm.sleep(2)
    os.system(Cl)

    print(main_board)
    print('여기는 우리가 게임을 하게 될 메인보드입니다')
    tm.sleep(2)
    print()
    print('자기턴의 카드를 뽑거나 카드를 사용하는 등 상호작용을 하면')
    print('카드가 표시됩니다')
    tm.sleep(2)

    print('\n이름을 적은 순서대로')
    for idx, name in enumerate(name_list) :
        print(f'Player {idx+1} (은)는 {name} 님')
    print('입니다')
    tm.sleep(3)
    os.system(Cl)

    print(main_board)
    print('먼저 선을 정하겠습니다')
    for _ in range(3) :
        tm.sleep(1)
        print('.')

    first = Bomb_game.choose_first(plyer_list)
    tm.sleep(2)
    print(f'선은 Player {first.ply}, {first} 님 입니다!')
    print('선 플레이어부터 시계방향으로 턴이 진행됩니다')
    plyer_list = plyer_list[plyer_list.index(first):] + plyer_list[:plyer_list.index(first)]
    tm.sleep(3)
    os.system(Cl)


    # ---------- 게임 시작 ----------
    print(main_board)
    Bomb_game.setting_deck(len(plyer_list))
    print('게임을 시작합니다')
    tm.sleep(2)
    while list(filter(lambda x : x.alive, plyer_list)) == plyer_list :
        os.system(Cl)
        print(main_board)
        now_turn = plyer_list[0]
        print(f'Plyer {now_turn.ply}, {now_turn} 님의 턴!')
        tm.sleep(2)

        while now_turn.num > 0 :
            draw_use = None
            getout = True # 탈출 커맨드
            while draw_use != '0' and getout :
                print(f'\n현재 남은 턴 수는 {now_turn.num} 입니다.  {len(Bomb_game.Deck)} 장 남았습니다')
                print("카드를 뽑을거면 '0', 카드를 사용할거면 '1' 을 입력하세요")
                print("(자신이 들고있는 카드를 보고싶으면 'show', 도움이 필요하다면 'help' 를 입력하세요)")
                draw_use = input()
                os.system(Cl)
                print(main_board)

                if draw_use == 'show' :
                    now_turn.show_card()

                elif draw_use == 'help' :
                    Bomb_game.help_word()

                elif draw_use == '1' :
                    use_card = '제거'
                    while use_card == '제거' :
                        os.system(Cl)
                        print(main_board)
                        now_turn.show_card()
                        print("어떤 카드를 사용할 지 선택하세요 (뒤로 가려면 'back'을 입력하세요)")
                        use_card = input()
                        os.system(Cl)
                        print(main_board)

                        while (use_card != 'back') and (use_card not in now_turn.hav_card) :
                            now_turn.show_card()
                            print(f"{use_card} 을(를) 찾을 수 없습니다. 다시 입력해주세요 (뒤로 가려면 'back'을 입력하세요)")
                            use_card = input()
                            os.system(Cl)
                            print(main_board)

                        if use_card == 'back' :
                            break
                        elif use_card == '제거' :
                            print('제거 카드는 직접 사용할 수 없습니다. 다른 카드를 선택하세요')
                            tm.sleep(2)
                            os.system(Cl)
                            print(main_board)
                            continue
                        else :
                            os.system(Cl)
                            now_turn.pri_board(use_card, main_board)
                            print(f'{use_card} 카드를 사용합니다')
                            tm.sleep(2)
                            if use_card == '셔플' :
                                now_turn.shuffle()

                            elif use_card == '투시' :
                                now_turn.xray()

                            elif use_card == '강탈' :
                                if list(filter(lambda x : x.hav_card, plyer_list[1:]))[0].hav_card == [] :
                                    print('카드를 가지고 있는 상대가 아무도 없습니다..')
                                else :
                                    while True :
                                        print(f'{list(map(lambda x : x.name, plyer_list[1:]))} 중에서')
                                        print('누구의 카드를 빼앗을 지 선택하세요')
                                        stolen = input()
                                        os.system(Cl)
                                        now_turn.pri_board('강탈', main_board)

                                        while stolen not in list(map(lambda x : x.name, plyer_list[1:])) :
                                            print(f'{list(map(lambda x : x.name, plyer_list[1:]))} 중에서 골라주세요')
                                            stolen = input()
                                            os.system(Cl)
                                            now_turn.pri_board('강탈', main_board)

                                        if list(filter(lambda x : x.name == stolen, plyer_list[1:]))[0].hav_card == [] :
                                            print(f'{stolen} 님은 가지고 있는 카드가 없습니다')
                                            print('다른 분을 선택해주세요')
                                            continue
                                        else :
                                            break

                                    now_turn.steal(*list(filter(lambda x : x.name == stolen, plyer_list[1:])))
                                    tm.sleep(3)

                            elif use_card == '스킵' :
                                now_turn.skip()
                                getout = False

                            elif use_card == '밑장빼기' :
                                os.system(Cl)
                                card = now_turn.underdraw()
                                now_turn.pri_board(card, main_board)
                                print(f'{card} 카드를 뽑으셨습니다!')
                                tm.sleep(3)

                            elif use_card == '프라이팬x1' :
                                print(f'{list(map(lambda x : x.name, plyer_list))} 중에서')
                                print('누구에게 사용할 지 선택하세요')
                                gang = input()
                                os.system(Cl)
                                print(main_board)

                                while gang not in list(map(lambda x : x.name, plyer_list)) :
                                    print(f'{list(map(lambda x : x.name, plyer_list))} 중에서 골라주세요')
                                    gang = input()
                                    os.system(Cl)
                                    print(main_board)

                                now_turn.frypan(*list(filter(lambda x : x.name == gang, plyer_list)), 1)
                                getout = False

                            elif use_card == '프라이팬x3' :
                                print(f'{list(map(lambda x : x.name, plyer_list))} 중에서')
                                print('누구에게 사용할 지 선택하세요')
                                gang = input()
                                os.system(Cl)
                                print(main_board)

                                while gang not in list(map(lambda x : x.name, plyer_list)) :
                                    print(f'{list(map(lambda x : x.name, plyer_list))} 중에서 골라주세요')
                                    gang = input()
                                    os.system(Cl)
                                    print(main_board)

                                now_turn.frypan(*list(filter(lambda x : x.name == gang, plyer_list)), 3)
                                getout = False

                            os.system(Cl)
                            print(main_board)

            if draw_use == '0' :
                card = now_turn.draw_card()
                os.system(Cl)
                now_turn.pri_board(card, main_board)
                print(f'{card} 카드를 뽑으셨습니다!')
                tm.sleep(3)

                if card == '폭탄' :
                    now_turn.num = 0
                    now_turn.frynum = 0
                    if '제거' in now_turn.hav_card :
                        os.system(Cl)
                        now_turn.pri_board('제거', main_board)
                        now_turn.remove()
                        tm.sleep(2)
                        os.system(Cl)
                        print(main_board)

                    else :
                        now_turn.bomb()
                        tm.sleep(3)
                        break

                os.system(Cl)
                print(main_board)

            if now_turn.num == 0 : # 턴을 다 소모했을 경우
                now_turn.turn = False
                if list(filter(lambda x : x.frynum != 0, plyer_list)) :
                    get_fried = list(filter(lambda x : x.frynum != 0, plyer_list))[0]
                    get_fried.turn = True
                    plyer_list = plyer_list[plyer_list.index(get_fried):] + plyer_list[:plyer_list.index(get_fried)]
                else :
                    plyer_list[1].turn = True
                    plyer_list[1].num = 1
                    plyer_list.append(plyer_list.pop(0))

    os.system(Cl)
    print()
    print('='*50)
    print(f'축하합니다! {list(map(lambda x : x.name, filter(lambda x : x.alive, plyer_list)))} 님은 살아남으셨습니다!!')
    print('='*50)
    print()

    print("다시 하시려면 'yes', 그만하시려면 'no' 를 입력해주세요")
    restart = input()
    os.system(Cl)

    while (restart != 'yes') and (restart != 'no') :
        print("다시 하시려면 'yes', 그만하시려면 'no' 를 입력해주세요")
        restart = input()

    if restart == 'yes' :
        continue
    elif restart == 'no' :
        print('플레이 해 주셔서 감사합니다!')
        break

