from joints import Joints
class Feet():

    # init method
    def __init__(self, nao):
        
        # jobs for threading
        self.nao = nao
        self.joints = nao.joints
        self.chains = nao.chains
        self.log = nao.log

    def go(self):
        self.nao.go()


    ###################################
    # point
    ###################################
    def pointToes(self, duration=0, offset=0):   
        self.rPointToe(duration, offset)
        self.lPointToe(duration, offset)
        return self;

    def lPointToe(self, duration=0, offset=0):
        duration = self.nao.determineDuration(duration)       
        angle = 52.8 + offset
        self.nao.moveWithDegreesAndDuration(self.joints.LLeg.LAnklePitch, angle, duration)
        return self;
        
    def rPointToe(self, duration=0, offset=0):
        duration = self.nao.determineDuration(duration)  
        angle = 52.8 + offset
        self.nao.moveWithDegreesAndDuration(self.joints.RLeg.RAnklePitch, angle, duration)
        return self;

   
    ###################################
    # raise
    ###################################
    def raiseToes(self, duration=0, offset=0):   
        self.rRaiseToe(duration, offset)
        self.lRaiseToe(duration, offset)
        return self;

    def lRaiseToe(self, duration=0, offset=0):
        duration = self.nao.determineDuration(duration)       
        angle = -68.0 - offset
        self.nao.moveWithDegreesAndDuration(self.joints.LLeg.LAnklePitch, angle, duration)
        return self;
        
    def rRaiseToe(self, duration=0, offset=0):
        duration = self.nao.determineDuration(duration)  
        angle = -68.0 - offset
        self.nao.moveWithDegreesAndDuration(self.joints.RLeg.RAnklePitch, angle, duration)
        return self;


    ###################################
    # out
    ###################################
    def turnOut(self, duration=0, offset=0):   
        self.rTurnOut(duration, offset)
        self.lTurnOut(duration, offset)
        return self;

    def lTurnOut(self, duration=0, offset=0):
        duration = self.nao.determineDuration(duration)       
        angle = 22 + offset
        self.nao.moveWithDegreesAndDuration(self.joints.LLeg.LAnkleRoll, angle, duration)
        return self;
        
    def rTurnOut(self, duration=0, offset=0):
        duration = self.nao.determineDuration(duration)        
        angle = -22 - offset
        self.nao.moveWithDegreesAndDuration(self.joints.RLeg.RAnkleRoll, angle, duration)
        return self;


    ###################################
    # in
    ###################################
    def turnIn(self, duration=0, offset=0):   
        self.rTurnIn(duration, offset)
        self.lTurnIn(duration, offset)
        return self;

    def lTurnIn(self, duration=0, offset=0):
        duration = self.nao.determineDuration(duration)       
        angle = -22.8 - offset
        self.nao.moveWithDegreesAndDuration(self.joints.LLeg.LAnkleRoll, angle, duration)
        return self;
        
    def rTurnIn(self, duration=0, offset=0):
        duration = self.nao.determineDuration(duration)        
        angle = 22.8 + offset
        self.nao.moveWithDegreesAndDuration(self.joints.RLeg.RAnkleRoll, angle, duration)
        return self;


    ###################################
    # center
    ###################################
    def center(self, duration=0, offset=0):   
        self.rCenter(duration, offset)
        self.lCenter(duration, offset)
        return self;

    def lCenter(self, duration=0, offset=0):
        duration = self.nao.determineDuration(duration)       
        self.nao.moveWithDegreesAndDuration(self.joints.LLeg.LAnkleRoll, 0, duration)
        self.nao.moveWithDegreesAndDuration(self.joints.LLeg.LAnklePitch, 0, duration)
        return self;
        
    def rCenter(self, duration=0, offset=0):
        duration = self.nao.determineDuration(duration)        
        self.nao.moveWithDegreesAndDuration(self.joints.RLeg.RAnkleRoll, 0, duration)
        self.nao.moveWithDegreesAndDuration(self.joints.RLeg.RAnklePitch, 0, duration)
        return self;