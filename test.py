from game_of_life.game import get_next_state

tests = [
  {
    "state": [
      [0, 0, 0],
      [1, 1, 1],
      [0, 0, 0]
    ],
    "next": [
      [0, 1, 0],
      [0, 1, 0],
      [0, 1, 0]
    ]
  },
  {
    "state": [
      [0, 1, 0, 0],
      [0, 0, 1, 0],
      [1, 1, 1, 0],
      [0, 0, 0, 0],
    ],
    "next": [
      [0, 0, 0, 0],
      [1, 0, 1, 0],
      [0, 1, 1, 0],
      [0, 1, 0, 0],
    ]
  },
]

error: bool = False
for test in tests:
    next = get_next_state(test["state"])
    if next != test["next"]:
        print("Error for matrix ", test["state"])
        print("Expected", test["next"])
        print("Got ", next)
        error = True

print('\033[92m✓ OK' if not error else '\033[91m❌KO')
