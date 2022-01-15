import math, random
from metaflow import step, FlowSpec, card

class UPlotFlow(FlowSpec):

    @card(type='uplot_timeseries')
    @step
    def start(self):
        import pandas
        index = pandas.date_range("2022-01-01", periods=60, freq="Min")
        series = {
            'first': self._fake_series(len(index), 0.1),
            'second': self._fake_series(len(index), 1)
        }
        self.timeseries = pandas.DataFrame(series, index=index)
        self.next(self.end)

    def _fake_series(self, n, g):
        return [(random.random() - 0.5) * 0.1 + math.sin(x * g) for x in range(n)]

    @step
    def end(self):
        pass

if __name__ == '__main__':
    UPlotFlow()