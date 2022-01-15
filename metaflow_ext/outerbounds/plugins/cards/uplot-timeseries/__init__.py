import os, json
from metaflow.cards import MetaflowCard
from metaflow.plugins.cards.card_modules import chevron

COLORS = [
    '#7e1e9c',
    '#15b01a',
    '#0343df',
    '#ff81c0',
    '#653700',
    '#e50000'
]

class UPlotTimeseriesCard(MetaflowCard):
    type = "uplot_timeseries"

    def _read_template(self):
        root = os.path.join(os.path.dirname(__file__), 'uplot')
        tmpl = {}
        for key, fname in [('card', 'card.html'),
                           ('uplot', 'uPlot.iife.min.js'),
                           ('css', 'uPlot.min.css')]:            
            with open(os.path.join(root, fname)) as f:
                tmpl[key] = f.read()
        return tmpl

    def render(self, task):
        tmpl = self._read_template()
        df = task.data.timeseries
        data = [[ts.timestamp() for ts in df.index]]
        for col in df:
            data.append(list(df[col].values))
        config = [{}] + [
            {'show': True,
             'stroke': COLORS[i],
             'label': col,
             'width': 1} for i, col in enumerate(df)]
        tmpl['data'] = json.dumps(data)
        tmpl['config'] = json.dumps(config)
        return chevron.render(tmpl['card'], tmpl)

CARDS = [UPlotTimeseriesCard]