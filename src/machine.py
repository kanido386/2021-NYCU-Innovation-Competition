from fsm import TocMachine

def create_machine():
  states = ["user", "menu"]
  mood = ["mood", "mood_detailed", "mood_done"]
  states.extend(mood)
  machine = TocMachine(
    # TODO: 用 append 的方式來添加
    states=states,
    # states=["user", "menu", "see_image", "state1", "state2", "youtube", "try_blockchain", "write_message", "read_message", "image"],
    # TODO: 用 append 的方式來添加
    # TODO: message type other than text should put forward
    transitions=[
      {
          "trigger": "advance",
          "source": "user",
          "dest": "menu",
          "conditions": "is_going_to_menu",
      },
      {
          "trigger": "advance",
          "source": "user",
          "dest": "mood",
          "conditions": "is_going_to_mood",
      },
      {
          "trigger": "advance",
          "source": "mood",
          "dest": "mood_detailed",
          "conditions": "is_going_to_mood_detailed",
      },
      {
          "trigger": "advance",
          "source": "mood_detailed",
          "dest": "mood_done",
          "conditions": "is_going_to_mood_done",
      },
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
      #     "dest": "youtube",
      #     "conditions": "is_going_to_youtube",
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
      {"trigger": "go_back", "source": ["mood_done"], "dest": "menu"},
      {"trigger": "go_back", "source": ["mood_detailed"], "dest": "mood"},
      # {"trigger": "go_back", "source": ["menu", "see_image", "state1", "state2", "youtube", "try_blockchain", "write_message", "read_message", "image"], "dest": "user"},
    ],
    initial="user",
    auto_transitions=False,
    show_conditions=True,
  )

  return machine