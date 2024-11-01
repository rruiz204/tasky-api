from strawberry.extensions import SchemaExtension
from prometheus.metrics.graphql_requests_total import GraphqlRequestTotalMetric

class MetricExtension(SchemaExtension):
  def on_operation(self):
    yield
    
    # Graphql Request Total Metric
    """ graphql_request_total_metric = GraphqlRequestTotalMetric(self.execution_context.query)
    graphql_request_total_metric.get_labels()
    graphql_request_total_metric.increase() """
    
    
