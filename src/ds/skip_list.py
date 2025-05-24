import dataclasses
import random
from typing import List, Optional


@dataclasses.dataclass
class SkipListElement:

    value: int
    right: Optional["SkipListElement"] = None
    down: Optional["SkipListElement"] = None


@dataclasses.dataclass
class SkipListLayer:

    head: SkipListElement


@dataclasses.dataclass
class SkipList:

    probability: float = 0.5
    layers: List[SkipListLayer] = dataclasses.field(default_factory=list)

    @property
    def values_by_layer(self) -> List[List[int]]:
        values_by_layer: List[List[int]] = []
        for layer in self.layers:
            values = []
            current: Optional[SkipListElement] = layer.head
            while current is not None:
                values.append(current.value)
                current = current.right
            values_by_layer.append(values)
        return values_by_layer

    @property
    def downmost_layer(self) -> SkipListLayer:
        return self.layers[0]

    @property
    def upmost_layer(self) -> SkipListLayer:
        return self.layers[len(self.layers) - 1]

    def search(self, value: int) -> bool:
        if value < self.downmost_layer.head.value:
            return False

        current: Optional[SkipListElement] = self.upmost_layer.head

        while current is not None:
            if current.value == value:
                return True

            if current.right is not None and value >= current.right.value:
                current = current.right
            else:
                current = current.down

        return False

    def random_layer_index(self) -> int:
        n = 0
        while random.random() >= self.probability:
            n += 1
        return n

    def insert(self, value: int) -> None:
        if len(self.layers) == 0:
            element = SkipListElement(value)
            layer = SkipListLayer(element)
            self.layers.append(layer)
            return

        if value <= self.downmost_layer.head.value:
            element = SkipListElement(value, right=self.downmost_layer.head)
            self.downmost_layer.head = element

            previous = element
            for layer in self.layers[1:]:
                element = SkipListElement(value, right=layer.head.right, down=previous)
                layer.head = element
                previous = element
            return

        layer_index = self.random_layer_index()
        while layer_index > len(self.layers) - 1:
            new_head = SkipListElement(self.downmost_layer.head.value)
            new_layer = SkipListLayer(new_head)
            new_head.down = self.upmost_layer.head
            self.layers.append(new_layer)

        update_stack: List[SkipListElement] = []
        current: Optional[SkipListElement] = self.upmost_layer.head
        for layer in reversed(self.layers):
            while current is not None:
                if current.right is not None and value > current.right.value:
                    current = current.right
                else:
                    update_stack.append(current)
                    current = current.down

        down: Optional[SkipListElement] = None
        for _ in range(layer_index + 1):
            update = update_stack.pop()
            new_node = SkipListElement(value, right=update.right, down=down)
            update.right = new_node
            down = new_node

    def delete(self, value: int) -> bool:
        if len(self.layers) == 0:
            return False

        if value < self.downmost_layer.head.value:
            return False

        if value == self.downmost_layer.head.value:
            if self.downmost_layer.head.right is None:
                self.layers.clear()
                return True

            for layer in reversed(self.layers):
                if layer.head.right is None:
                    self.layers.pop()
                else:
                    layer.head = layer.head.right

            previous = self.downmost_layer.head
            for layer in self.layers[1:]:
                layer.head = SkipListElement(
                    value=previous.value, right=layer.head, down=previous
                )
                previous = layer.head

            return True

        current: Optional[SkipListElement] = self.upmost_layer.head
        found = False

        while current is not None:
            if current.right is None:
                current = current.down
                continue

            if current.right.value < value:
                current = current.right
                continue

            if current.right.value == value:
                current.right = current.right.right
                current = current.down
                found = True
            else:
                current = current.down

        while len(self.layers) > 1 and self.upmost_layer.head.right is None:
            self.layers.pop()

        return found
