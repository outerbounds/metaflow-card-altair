from metaflow.cards import MetaflowCard

class AltairCard(MetaflowCard):
    type = "altair"

    def render(self, task):
        return task.data.chart

CARDS = [AltairCard]