from fsm import TocMachine

def create_machine():
  states = ["user", "menu"]
  mood = ["mood", "mood_detailed", "mood_done"]
  meal = ["meal", "meal_search", "meal_report", "meal_input", "meal_reward"]
  diary = ["diary", "diary_done"]
  exercise = ["exercise", "exercise_done"]
  sleeping = ["sleeping", "sleeping_up", "sleeping_done"]
  skin = ["skin", "skin_process", "skin_done"]
  report = ["report"]
  entertainment = ["entertainment"]
  youtube = ["youtube", "youtube_send", "youtube_ing", "youtube_done"]
  category = [mood, meal, diary, exercise, sleeping, skin, report, entertainment, youtube]
  for item in category:
    states.extend(item)
  machine = TocMachine(
    # TODO: 用 append 的方式來添加
    states=states,
    # states=["user", "menu", "see_image", "state1", "state2", "youtube", "try_blockchain", "write_message", "read_message", "image"],
    # TODO: 用 append 的方式來添加
    # TODO: message type other than text should put forward
    transitions=[
      { "trigger": "advance", "source": "user", "dest": "menu", "conditions": "is_going_to_menu" },
      # mood
      { "trigger": "advance", "source": "user", "dest": "mood", "conditions": "is_going_to_mood" },
      { "trigger": "advance", "source": "mood", "dest": "mood_detailed", "conditions": "is_going_to_mood_detailed" },
      { "trigger": "advance", "source": "mood_detailed", "dest": "mood_done", "conditions": "is_going_to_mood_done" },
      # meal
      { "trigger": "advance", "source": "user", "dest": "meal", "conditions": "is_going_to_meal" },
      { "trigger": "advance", "source": "meal", "dest": "meal_search", "conditions": "is_going_to_meal_search" },
      { "trigger": "yes", "source": "meal_search", "dest": "meal_report", "conditions": "is_going_to_meal_report" },
      { "trigger": "no", "source": "meal_search", "dest": "meal_input", "conditions": "is_going_to_meal_input" },
      { "trigger": "advance", "source": "meal_input", "dest": "meal_reward", "conditions": "is_going_to_meal_reward" },
      # diary
      { "trigger": "advance", "source": "user", "dest": "diary", "conditions": "is_going_to_diary" },
      { "trigger": "advance", "source": "diary", "dest": "diary_done", "conditions": "is_going_to_diary_done" },
      # exercise
      { "trigger": "advance", "source": "user", "dest": "exercise", "conditions": "is_going_to_exercise" },
      { "trigger": "advance", "source": "exercise", "dest": "exercise_done", "conditions": "is_going_to_exercise_done" },
      # sleeping
      { "trigger": "advance", "source": "user", "dest": "sleeping", "conditions": "is_going_to_sleeping" },
      { "trigger": "advance", "source": "sleeping", "dest": "sleeping_up", "conditions": "is_going_to_sleeping_up" },
      { "trigger": "advance", "source": "sleeping_up", "dest": "sleeping_done", "conditions": "is_going_to_sleeping_done" },
      # skin
      { "trigger": "advance", "source": "user", "dest": "skin", "conditions": "is_going_to_skin" },
      { "trigger": "advance", "source": "skin", "dest": "skin_process", "conditions": "is_going_to_skin_process" },
      { "trigger": "advance", "source": "skin_process", "dest": "skin_done", "conditions": "is_going_to_skin_done" },
      # report
      { "trigger": "advance", "source": "user", "dest": "report", "conditions": "is_going_to_report" },
      # entertainment
      { "trigger": "advance", "source": "user", "dest": "entertainment", "conditions": "is_going_to_entertainment" },
      { "trigger": "advance", "source": "entertainment", "dest": "menu", "conditions": "is_going_to_exit" },
      # youtube
      { "trigger": "advance", "source": "entertainment", "dest": "youtube", "conditions": "is_going_to_youtube" },
      { "trigger": "advance", "source": "youtube", "dest": "youtube_send" },
      { "trigger": "advance", "source": "youtube_send", "dest": "youtube_ing" },
      { "trigger": "advance", "source": "youtube_ing", "dest": "youtube_ing", "conditions": "is_going_to_youtube_ing" },
      { "trigger": "advance", "source": "youtube_ing", "dest": "youtube_done", "conditions": "is_going_to_youtube_done" },
      # {
      #     "trigger": "advance",
      #     "source": "user",
      #     "dest": "image",
      #     "conditions": "is_going_to_image",
      # },
      # {
      #     "trigger": "advance",
      #     "source": "user",
      #     "dest": "see_image",
      #     "conditions": "is_going_to_see_image",
      # },
      # {
      #     "trigger": "advance",
      #     "source": "user",
      #     "dest": "state1",
      #     "conditions": "is_going_to_state1",
      # },
      # {
      #     "trigger": "advance",
      #     "source": "user",
      #     "dest": "state2",
      #     "conditions": "is_going_to_state2",
      # },
      # {
      #     "trigger": "advance",
      #     "source": "user",
      #     "dest": "try_blockchain",
      #     "conditions": "is_going_to_try_blockchain",
      # },
      # {
      #     "trigger": "advance",
      #     "source": "user",
      #     "dest": "write_message",
      #     "conditions": "is_going_to_write_message",
      # },
      # {
      #     "trigger": "advance",
      #     "source": "user",
      #     "dest": "read_message",
      #     "conditions": "is_going_to_read_message",
      # },
      # TODO: 用 append 的方式來添加
      # TODO: message type other than text should put forward
      {"trigger": "go_back", "source": ["menu"], "dest": "user"},
      {"trigger": "go_back", "source": ["report", "skin_done", "sleeping_done", "exercise_done", "diary_done", "mood_done", "meal_report", "meal_reward"], "dest": "menu"},
      {"trigger": "go_back", "source": ["mood_detailed"], "dest": "mood"},
      {"trigger": "go_back", "source": ["youtube_done"], "dest": "entertainment"},
      # {"trigger": "go_back", "source": ["menu", "see_image", "state1", "state2", "youtube", "try_blockchain", "write_message", "read_message", "image"], "dest": "user"},
    ],
    initial="user",
    auto_transitions=False,
    show_conditions=True,
  )

  return machine