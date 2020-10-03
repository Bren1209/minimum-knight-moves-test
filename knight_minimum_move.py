import collections

# Function to return minimum amount of moves for knight to reach its target destination
# Parameters: Source location (srcX, srcY), Target destination (destX, destY).

def totalMoves(srcX, srcY, destX, destY):

  # Figure out possible movements from current knight position (relative to knight) in "blocks" (x, y)
  possible_moves = [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]

  # Declare queue var for level-by-level search, starting at source location (srcX, srcY)
  q = collections.deque([(srcX, srcY)])

  # Determe whether a location on the board has been visited, starting at source location (0, 0)
  visited = set()
  visited.add((srcX, srcY))

  # Set destination/source pos to absolute value to prevent error (the outcome would be the same with negative integers)
  srcX = abs(srcX)
  srcY = abs(srcY)
  destX = abs(destX)
  destY = abs(destY)

  # Ensure source position and target position is within 8x8 board
  if srcX > 8:
    return 'Source position X exceeds board size (8 x 8).'
  elif srcY > 8:
    return 'Source position Y exceeds board size (8 x 8).'
  elif destX > 8:
    return 'Destination position X exceeds board size (8 x 8).'
  elif destY > 8:
    return 'Destination position Y exceeds board size (8 x 8).'

  distance_travelled = 0

  # Continue search using while loop
  while q:

    for _ in range(len(q)):
      # Get current position from queue
      current_pos_x, current_pos_y = q.popleft()

      # Return number of steps if current position matches the given target
      if current_pos_x == destX and current_pos_y == destY:
        return f'Minimum amount of steps needed to reach target location: {distance_travelled}'

      # Set new position by cycling through all possible moves
      for move in possible_moves:
        new_pos_x = current_pos_x + move[0]
        new_pos_y = current_pos_y + move[1]

      # Check if position has been visited before and set constraints for moving too far in opposite direction
        if (new_pos_x, new_pos_y) not in visited and -2 <= new_pos_x <= (destX + 2) and -2 <= new_pos_y <= (destY + 2):
          new_position = (new_pos_x, new_pos_y)
          # Add new position to queue and mark as visited
          q.append(new_position)
          visited.add(new_position)


    distance_travelled += 1

# Get input from user:
srcX = int(input('Set starting position X: '))
srcY = int(input('Set starting position Y: '))
destX = int(input('Set destination position X: '))
destY = int(input('Set destination position Y: '))

print(totalMoves(srcX, srcY, destX, destY))