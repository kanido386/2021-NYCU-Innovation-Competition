from fsm import TocMachine

def create_machine():
  machine = TocMachine(
    # TODO: 用 append 的方式來添加
    states=["user", "state1", "state2", "youtube", "try_blockchain", "write_message", "read_message"],
    # TODO: 用 append 的方式來添加
    transitions=[
      {
          "trigger": "advance",
          "source": "user",
          "dest": "state1",
          "conditions": "is_going_to_state1",
      },
      {
          "trigger": "advance",
          "source": "user",
          "dest": "state2",
          "conditions": "is_going_to_state2",
      },
      {
          "trigger": "advance",
          "source": "user",
          "dest": "youtube",
          "conditions": "is_going_to_youtube",
      },
      {
          "trigger": "advance",
          "source": "user",
          "dest": "try_blockchain",
          "conditions": "is_going_to_try_blockchain",
      },
      {
          "trigger": "advance",
          "source": "user",
          "dest": "write_message",
          "conditions": "is_going_to_write_message",
      },
      {
          "trigger": "advance",
          "source": "user",
          "dest": "read_message",
          "conditions": "is_going_to_read_message",
      },
      # TODO: 用 append 的方式來添加
      {"trigger": "go_back", "source": ["state1", "state2", "youtube", "try_blockchain", "write_message", "read_message"], "dest": "user"},
    ],
    initial="user",
    auto_transitions=False,
    show_conditions=True,
  )

  return machine