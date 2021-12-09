with open("text_04.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content]

numbers_to_call = content[0].split(",")
called_nums = []

boards = [[content[x + y + 1].split() for y in range(5)] for x in range(1, len(content), 6)]
winner = None

# PART 1
# for num in numbers_to_call:
#     called_nums.append(num)
#     for board in boards:
#         if any(all(v in called_nums for v in line) for line in board) or \
#                 any(all(v in called_nums for v in line) for line in [[board[x][y] for x in range(5)] for y in range(5)]):
#             winner = board
#             break
#     if winner is not None:
#         break

# PART 2
boards_won = []
for num in numbers_to_call:
    called_nums.append(num)
    for board in boards:
        if any(all(v in called_nums for v in line) for line in board) or \
                any(all(v in called_nums for v in line) for line in [[board[x][y] for x in range(5)] for y in range(5)]):
            if board not in boards_won:
                boards_won.append(board)
    if len(boards) == len(boards_won):
        winner = boards_won[-1]
        break


print(sum([int(x) for y in winner for x in y if x not in called_nums]) * int(called_nums[-1]))
