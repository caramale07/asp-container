class Container:
    """
    A water container that can be connected to other containers.
    """


    def __init__(self, amount: float = 0.0):
        self.amount = amount
        self.neighbors = set()
    
    def connect(self, other: 'Container') -> None:

        if self is other:
            return
        
        if self._is_connected_to(other):
            return
        
        self.neighbors.add(other)
        other.neighbors.add(self)
        
        self._redistribute()
    
    def disconnect(self, other: 'Container') -> None:
        self.neighbors.discard(other)
        other.neighbors.discard(self)
    
    def add_water(self, amount: float) -> None:
        self.amount += amount
        self._redistribute()
    
    def _is_connected_to(self, other: 'Container') -> bool:
        visited = set()
        stack = [self]
        
        while stack:
            current = stack.pop()
            if current in visited:
                continue
            if current is other:
                return True
            visited.add(current)
            stack.extend(current.neighbors)
        
        return False
    
    def _redistribute(self) -> None:
        component = []
        visited = set()
        stack = [self]
        
        while stack:
            current = stack.pop()
            if current in visited:
                continue
            visited.add(current)
            component.append(current)
            stack.extend(current.neighbors)
        
        total_water = sum(container.amount for container in component)
        average_water = total_water / len(component)
        
        for container in component:
            container.amount = average_water
    
    def __repr__(self) -> str:
        return f"Container(amount={self.amount}, neighbors={len(self.neighbors)})"




if __name__ == "__main__":
    print("=== Container Tests ===\n")
    
    print("==test1==")
    c1 = Container(10.0)
    c2 = Container(20.0)
    print(f"before: c1={c1.amount}, c2={c2.amount}")
    c1.connect(c2)
    print(f"after:  c1={c1.amount}, c2={c2.amount}")
    assert c1.amount == 15.0 and c2.amount == 15.0, "Should equalize to 15.0"
    print(" PASSED\n")
    
    print("==test2==")
    c1 = Container(30.0)
    c2 = Container(60.0)
    c3 = Container(90.0)
    print(f"before: c1={c1.amount}, c2={c2.amount}, c3={c3.amount}")
    c1.connect(c2)
    c2.connect(c3)
    print(f"after:  c1={c1.amount}, c2={c2.amount}, c3={c3.amount}")
    assert c1.amount == c2.amount == c3.amount == 60.0, "Failed"
    print(" PASSED\n")
    
    print("==test3==")
    c1 = Container(10.0)
    c2 = Container(10.0)
    c1.connect(c2)
    print(f"before: c1={c1.amount}, c2={c2.amount}")
    c1.add_water(20.0)
    print(f"after:  c1={c1.amount}, c2={c2.amount}")
    assert c1.amount == 20.0 and c2.amount == 20.0, "Failed"
    print(" PASSED\n")
    
    print("==test4==")
    c1 = Container(10.0)
    c2 = Container(30.0)
    c1.connect(c2)
    c1.disconnect(c2)
    print(f"before: c1={c1.amount}, c2={c2.amount}")
    c1.add_water(10.0)
    print(f"after:  c1={c1.amount}, c2={c2.amount}")
    assert c1.amount == 30.0 and c2.amount == 20.0, "Failed"
    print(" PASSED\n")
    
    print("==test5==")
    c1 = Container(10.0)
    c2 = Container(20.0)
    c3 = Container(30.0)
    c4 = Container(40.0)
    c5 = Container(50.0)
    c1.connect(c2)
    c2.connect(c3)
    c4.connect(c5)
    print(f"before: c1={c1.amount}, c2={c2.amount}, c3={c3.amount}, c4={c4.amount}, c5={c5.amount}")
    c3.connect(c4)
    print(f"after:  all={c1.amount}")
    assert all(c.amount == 30.0 for c in [c1, c2, c3, c4, c5]), "Failed"
    print(" PASSED\n")
    
    print("==test6==")
    c1 = Container(10.0)
    c2 = Container(20.0)
    c3 = Container(30.0)
    c1.connect(c2)
    c2.connect(c3)
    print(f"before: c1={c1.amount}, c2={c2.amount}, c3={c3.amount}")
    c3.connect(c1)  
    print(f"after:  all={c1.amount}")
    assert c1.amount == c2.amount == c3.amount == 20.0, "Failed"
    print(" PASSED\n")
    

    

