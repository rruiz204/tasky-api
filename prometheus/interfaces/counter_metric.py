from abc import ABC, abstractmethod

class CounterMetric(ABC):

  @abstractmethod
  def get_labels(self, query: str):
    pass

  @abstractmethod
  def increase(self):
    pass