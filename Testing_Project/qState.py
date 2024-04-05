from typing import List

class timedState:
    def __init__(self, state: int, localTime: int, specTime: int):
        self.state = state
        self.localTime = localTime
        self.specTime = specTime  # Assuming specTime is a constant

class qState:
    def __init__(self):
        self.minTimeOut = float('inf')  # Positive infinity for min timeout
        self.stateSet = []
        self.sequence = []

    def size(self) -> int:
        return len(self.stateSet)

    def addSet(self, state: timedState):
        self.stateSet.append(state)

    def setMinTimeOut(self):
        selected = False
        for state in self.stateSet:
            if state.specTime >= 0:
                difference = state.specTime - state.localTime
                if difference < 0:
                    pass  # Handle negative time difference (if needed)
                if difference < self.minTimeOut:
                    selected = True
                    self.minTimeOut = difference
        if selected:
            pass  # Do something if a minimum timeout was found (optional)
        else:
            self.minTimeOut = 0

    def returnMinTimeOut(self) -> int:
        return self.minTimeOut

    def sort(self):
        # Implement bubble sort (can be replaced with more efficient algorithms)
        not_in_order = True
        current_index = 0
        while not_in_order:
            next_index = current_index + 1
            if next_index < len(self.stateSet):
                if self.stateSet[current_index].state > self.stateSet[next_index].state:
                    temp = self.stateSet[current_index]
                    self.stateSet[current_index] = self.stateSet[next_index]
                    self.stateSet[next_index] = temp
                    current_index = 0
                else:
                    current_index += 1
            else:
                not_in_order = False

    def elemAt(self, index: int) -> timedState:
        return self.stateSet[index]

    def SetSequence(self, sequence: List[int]):
        self.sequence = sequence

    def GetSequence(self) -> List[int]:
        return self.sequence

    def exists(self, elements: List[int], value: int) -> bool:
        return value in elements

    def timeDifference(self) -> float:
        unique_times = []
        for state in self.stateSet:
            if state.specTime >= 0 and state.localTime not in unique_times:
                unique_times.append(state.localTime)
        if len(unique_times) == 1:
            return 0
        difference = sum(unique_times)
        return difference * difference
