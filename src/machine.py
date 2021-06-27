from fsm import TocMachine

def create_machine():
  machine = TocMachine(
    states=["user", "state1", "state2", "youtube", "try_blockchain"],
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
      {"trigger": "go_back", "source": ["state1", "state2", "youtube", "try_blockchain"], "dest": "user"},
    ],
    initial="user",
    auto_transitions=False,
    show_conditions=True,
  )

  return machine