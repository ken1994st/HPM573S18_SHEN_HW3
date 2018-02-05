class Node:
    def __init__(self, name, cost, utility):
        self.name = name
        self.cost = cost
        self.utility = utility

    def get_expected_cost(self):
        raise NotImplementedError("This is an abstract method and needs to be implemented in derived classes.")

    def expected_health_utility(self):
        raise NotImplementedError("This is an abstract method and needs to be implemented in derived classes.")

# two chanceNode

class ChanceNode(Node):
    def __init__(self, name, cost, utility, probs, future_nodes):
        Node.__init__(self, name, cost, utility)
        self.probs = probs
        self.future_nodes = future_nodes

    def get_expected_cost(self):
        exp_cost = self.cost # the expected cost of this node including the cost of visiting this node
        i = 0 # index to iterate over probabilities
        for thisNode in self.future_nodes:
            exp_cost += self.probs[i] * thisNode.get_expected_cost()
            i += 1

        return exp_cost

    def expected_health_utility(self):
        exp_utility = self.utility
        x = 0
        for healthNode in self.future_nodes:
            exp_utility += self.probs[x] * healthNode.expected_health_utility()
            x += 1

        return exp_utility


class TerminalNode(Node):
    def __init__(self, name, cost, utility):
        Node.__init__(self, name, cost, utility)

    def get_expected_cost(self):
        return self.cost

    def expected_health_utility(self):
        return self.utility

class DecisionNode(Node):
    def __init__(self, name, cost, utility, future_nodes):
        Node.__init__(self, name, cost, utility)
        self.future_nodes = future_nodes  #list of future node objects

    def get_expected_cost(self):
        """return the expected cost of associated future nodes"""
        outcomes = dict() # dictionary to store expected cost of future nodes
        for thisNode in self.future_nodes:
            outcomes[thisNode.name] = thisNode.get_expected_cost()

        return outcomes

    def expected_health_utility(self):
        healthoutcomes = dict()
        for healthNode in self.future_nodes:
            healthoutcomes[healthNode.name] = healthNode.expected_health_utility()

        return healthoutcomes

#creating terminal node T1

T1 = TerminalNode('T1', 10, 0.9)
T2 = TerminalNode('T2', 20, 0.8)
T3 = TerminalNode('T3', 30, 0.7)
T4 = TerminalNode('T4', 40, 0.6)
T5 = TerminalNode('T5', 50, 0.5)


C2FutureNodes = [T1, T2]
C2 = ChanceNode('C2', 35, 0, [0.7, 0.3], C2FutureNodes)

C1FutureNodes = [C2, T3]
C1 = ChanceNode('C1', 25, 0, [0.2, 0.8], C1FutureNodes)

C3FutureNodes =[T4, T5]
C3 = ChanceNode('C3', 45, 0, [0.1, 0.9], C3FutureNodes)

D1FutureNodes =[C1, C3]
D1 = DecisionNode('D1', 0, 0,  D1FutureNodes)

print(D1.get_expected_cost(), D1.expected_health_utility())

