import re
from typing import Dict, Any
from prometheus_client import Counter

graphql_requests_total = Counter(
  name="graphql_requests_total",
  documentation="Total number of GraphQL requests processed, categorized by query name, operation type (query or mutation), and response status.",
  labelnames=("type", "name")
)

class GraphqlRequestTotalMetric:
  def __init__(self, query: str) -> None:
    self.pattern = r'(\w+)\s*{\s*(\w+)'
    self.labels = {self.get_labels(query)}

  def get_labels(self, query: str) -> Dict[str, Any]:
    match = re.search(self.pattern, query)
    return {"type": match.group(1), "name": match.group(2)}
  
  def increase(self):
    graphql_requests_total.labels(type=self.labels["type"], name=self.labels["name"]).inc()