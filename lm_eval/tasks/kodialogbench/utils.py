import random


def doc_to_text_response_selection_korean_sns_and_korean_dialogue_summary(doc):
    participants = set(turn['participantID'] for turn in doc['dialogue'])
    participants.add(doc['speaker'])
    participants = list(participants)
    random.shuffle(participants)
    participants_mapping = {s: f"화자{i}" for i, s in enumerate(participants, start=1)}
    
    prompt = "\n".join(
        f"{participants_mapping[turn['participantID']]}: {turn['utterance']}"
        for turn in doc['dialogue']
    )
    prompt += f"\n{participants_mapping[doc['speaker']]}:"
    return prompt


def doc_to_text_response_selection_korean_thematic_daily_dialogue(doc):
    participants = set(int(turn['speaker']['id'][:-1]) for turn in doc['dialogue'])
    participants.add(doc['speaker'])
    participants = list(participants)
    random.shuffle(participants)
    participants_mapping = {s: f"화자{i}" for i, s in enumerate(participants, start=1)}
    
    prompt = "\n".join(
        f"{participants_mapping[int(turn['speaker']['id'][:-1])]}: {turn['norm_text']}"
        for turn in doc['dialogue']
    )
    prompt += f"\n{participants_mapping[doc['speaker']]}:"
    return prompt


def doc_to_text_response_selection_korean_emotional_dialogue(doc):
    participants = set(turn['speaker'] for turn in doc['dialogue'])
    participants.add(doc['speaker'])
    participants = list(participants)
    random.shuffle(participants)
    participants_mapping = {s: f"화자{i}" for i, s in enumerate(participants, start=1)}
    
    prompt = "\n".join(
        f"{participants_mapping[turn['speaker']]}: {turn['text']}"
        for turn in doc['dialogue']
    )
    prompt += f"\n{participants_mapping[doc['speaker']]}:"
    return prompt


def doc_to_text_response_selection_persona_chat_korean(doc):
    participants = [0, 1]
    random.shuffle(participants)
    participants_mapping = {s: f"화자{i}" for i, s in enumerate(participants, start=1)}

    prompt = f"{participants_mapping[len(doc['dialogue']) % 2]}의 페르소나:\n"
    prompt += "\n".join(f"- {row}" for row in doc['personality'])
    prompt += "\n"
    
    prompt += "\n".join(
        f"{participants_mapping[idx % 2]}: {turn}"
        for idx, turn in enumerate(doc['dialogue'])
    )
    prompt += f"\n{participants_mapping[len(doc['dialogue']) % 2]}:"
    return prompt


def doc_to_text_response_selection_daily_dialog_korean(doc):
    participants = [0, 1]
    random.shuffle(participants)
    participants_mapping = {s: f"화자{i}" for i, s in enumerate(participants, start=1)}

    prompt = "\n".join(
        f"{participants_mapping[idx % 2]}: {turn}"
        for idx, turn in enumerate(doc['dialogue'])
    )
    prompt += f"\n{participants_mapping[len(doc['dialogue']) % 2]}:"
    return prompt


def doc_to_text_response_selection_empathetic_dialogues_korean(doc):
    participants = set(turn['speaker'] for turn in doc['dialogue'])
    participants.add(doc['speaker'])
    participants = list(participants)
    random.shuffle(participants)
    participants_mapping = {s: f"화자{i}" for i, s in enumerate(participants, start=1)}

    prompt = "\n".join(
        f"{participants_mapping[turn['speaker']]}: {turn['text']}"
        for turn in doc['dialogue']
    )
    prompt += f"\n{participants_mapping[doc['speaker']]}:"
    return prompt


def doc_to_text_response_selection_socialdial_korean(doc):
    participants = [0, 1]
    random.shuffle(participants)
    participants_mapping = {s: f"화자{i}" for i, s in enumerate(participants, start=1)}

    prompt = "\n".join(
        f"{participants_mapping[idx % 2]}: {turn}"
        for idx, turn in enumerate(doc['dialogue'])
    )
    prompt += f"\n{participants_mapping[len(doc['dialogue']) % 2]}:"
    return prompt


def doc_to_choice_response_selection(doc):
    return [doc['positive'], *doc['random_candidates']]
