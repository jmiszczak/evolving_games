import mesa 
import mesa.time as mt
import numpy.random as rnd

class MoneyAgent(mesa.Agent):
    """An agent with initial amount of money"""
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.wealth = 1

    def step(self):
        """Execute one step"""
        if self.wealth == 0 :
            pass
        else :
            other = self.random.choice(self.model.schedule.agents)
            other.wealth += 1
            self.wealth -= 1

class MoneyModel(mesa.Model):
    def __init__(self, N):
        self.num_agents = N
        self.schedule = mt.RandomActivation(self)
        # create and add agents
        for i in range(self.num_agents):
            a = MoneyAgent(i, self)
            self.schedule.add(a)

    def step(self):
        """Execute one step for all agents"""
        self.schedule.step()
