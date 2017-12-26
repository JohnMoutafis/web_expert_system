from pyknow import Fact, Rule, KnowledgeEngine, L


class TrafficLight(Fact):
    """
    Traffic light info
    """
    pass


class CrossStreet(KnowledgeEngine):
    """
    Decide if our robot is safe to cross the road.
    """
    @Rule(TrafficLight(color='green'))
    def green_light(self):
        self.response = 'Cross the road'

    @Rule(TrafficLight(color='red'))
    def red_light(self):
        self.response = 'Don\'t cross the road'

    @Rule('light' << TrafficLight(color=L('yellow') | L('blinking_yellow')))
    def caution(self, light):
        self.response = 'You can cross, but be careful!'


robot = CrossStreet()
