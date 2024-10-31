from typing import List, Type
from prometheus.interfaces.counter_metric import CounterMetric
from prometheus.metrics.graphql_requests_total import GraphqlRequestTotalMetric
from prometheus_fastapi_instrumentator import Instrumentator

class MetricManager:
  def __init__(self, confirm: str) -> None:
    self.confirm = confirm == "Enable"

    self.counters_by_extensions: List[Type[CounterMetric]] = [GraphqlRequestTotalMetric]

  def add_metrics_to_middleware(self, instrumentator: Instrumentator):
    if (not self.confirm): return
    pass

  def run_metrics_by_extensions(self, query: str):
    if (not self.confirm): return
    self.run_counters(self.counters_by_extensions, query=query)

  def run_counters(self, counters: List[Type[CounterMetric]], query: str):
    for counter in counters:
      ctr = counter(query=query)
      ctr.increase()