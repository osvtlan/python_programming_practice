import random


class SomeModel:
    def predict(self, note: str) -> float:
        return round(random.uniform(0.0, 1.0), 1)


def predict_message_mood(note, model, bad_thresholds=0.3, good_thresholds=0.8):
    prediction = model.predict(note)
    if prediction < bad_thresholds:
        return "неуд"
    elif prediction > good_thresholds:
        return "отл"
    else:
        return "норм"


if __name__ == '__name__':
    model = SomeModel()
    predict_message_mood("Чапаев и пустота", model)
