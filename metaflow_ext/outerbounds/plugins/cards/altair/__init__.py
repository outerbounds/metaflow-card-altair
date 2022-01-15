import os, json
from metaflow.cards import MetaflowCard
from metaflow.plugins.cards.card_modules import chevron

class AltairCard(MetaflowCard):
    type = "altair"

    def _read_template(self):
        root = os.path.join(os.path.dirname(__file__), 'altair')
        tmpl = {}
        for key, fname in [('card', 'card.html')]:            
            with open(os.path.join(root, fname)) as f:
                tmpl[key] = f.read()
        return tmpl

    def render(self, task):
        tmpl = self._read_template()
        chart_html = task.data.chart
        tmpl['chart'] = chart_html
        return chevron.render(tmpl['card'], tmpl)

CARDS = [AltairCard]