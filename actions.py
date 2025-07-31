def show_action_prompts(location, game_state, character):
    prompts = []
    if game_state["alec_learn"] is False or game_state["mixed_audio1"] is False or game_state["mixed_audio2"] is False or game_state["picked_up_box"] is False:
        prompts.append("Type 'quests' to see your quests to complete.")
    if getattr(location, "name", "") == "Audio Rack" and (not game_state["mixed_audio1"] or not game_state["mixed_audio2"]):
        prompts.append("Type 'mix' to mix the sound at the desk.")
    if getattr(location, "name", "") == "Cole's Car" and not game_state["picked_up_box"]:
        prompts.append("Type 'pickup box' to grab the box out of Cole's car.")
    if character is not None:
        prompts.append(f"Type 'talk' to interact with {character.name}.")
    for p in prompts:
        print(p)
