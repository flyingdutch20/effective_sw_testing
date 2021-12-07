from dataclasses import dataclass

@dataclass
class PlanningPoker:
    estimates: {}

    def return_extremes(self):
        #handle null list, empty list and list with 1 element
        lowest = None
        highest = None
        try:
            assert len(self.estimates) > 1
            for estimate in self.estimates.items():
                if highest is None or estimate[1] > highest[1]:
                    highest = estimate
                if lowest is None or estimate[1] < lowest[1]:
                    lowest = estimate
        except Exception as error:
            raise error
        return [lowest[0], highest[0]]