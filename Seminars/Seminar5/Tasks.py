from random import randint


def last_wins(heap_value: int, step_value: int) -> None: # M - 1 % N Last player wins
    count = 0
    curr_player_turn = 0
    flag = True
    while True:
        count += 1
        if heap_value <= step_value:
           print(f"Computer takes {heap_value} candies. Computer wins") 
           break

        if count == 1:
            turn = heap_value % (step_value + 1)
            if turn == 0:
                turn = randint(1,step_value)
                flag = False

            heap_value -= turn
            print(f"Computer takes {turn} candies. Remained {heap_value} candies")
        else:
            if heap_value % (step_value + 1) != 0:
                flag = True
                print("Computer changes its strategy")
            turn = step_value + 1 - curr_player_turn  if flag else randint(1,step_value)
            heap_value -= turn
            print(f"Computer takes {turn} candies. Remained {heap_value} candies")
        count += 1

        print("Enter candies quantity")
        curr_player_turn = int(input())
        heap_value -= curr_player_turn

        if heap_value == 0:
            print("You win!")
            break
        else:
            print(f"Player takes {curr_player_turn} candies. Remained {heap_value} candies")


last_wins(20,3)
