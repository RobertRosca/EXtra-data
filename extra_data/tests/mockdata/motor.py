from .base import DeviceBase
from .control_common import interlock_keys, triggers_keys

class Motor(DeviceBase):
    control_keys = [
        ('AActualVelocity', 'f8', ()),
        ('AEncoderResolution', 'u4', ()),
        ('AHomingVelocityOffPlcCam', 'f8', ()),
        ('AHomingVelocityToPlcCam', 'f8', ()),
        ('ANCParam', 'u4', ()),
        ('ANomCurrent', 'u4', ()),
        ('AOpenloopCurrent', 'u4', ()),
        ('APeakCurrent', 'u4', ()),
        ('AProfileAcceleration', 'u4', ()),
        ('AQuickStopDecceleration', 'u4', ()),
        ('AStandByCurrent', 'u4', ()),
        ('AStepperResolution', 'u4', ()),
        ('Acontrolword', 'u2', ()),
        ('actualPosition', 'f8', ()),
        ('axisBacklash', 'f8', ()),
        ('busy', 'u1', ()),
        ('calibrateTarget', 'f8', ()),
        ('enableSWLimitHigh', 'u1', ()),
        ('enableSWLimitLow', 'u1', ()),
        ('encoderPosition', 'f8', ()),
        ('epsilon', 'f4', ()),
        ('epsilonActualPosition', 'f8', ()),
        ('epsilonActualVelocity', 'f8', ()),
        ('force', 'u1', ()),
        ('hardwareErrorDescriptor', 'u4', ()),
        ('hardwareStatusBitField', 'u4', ()),
        ('isCCWLimit', 'u1', ()),
        ('isCWLimit', 'u1', ()),
        ('isInterlockLimitHigh', 'u1', ()),
        ('isInterlockLimitLow', 'u1', ()),
        ('isOnTarget', 'u1', ()),
        ('isSWLimitHigh', 'u1', ()),
        ('isSWLimitLow', 'u1', ()),
        ('isSlave', 'u1', ()),
        ('maxUpdateFrequency', 'f4', ()),
        ('mc2/aaxisacc', 'f8', ()),
        ('mc2/aaxiscalibrationvelocitybackward', 'f8', ()),
        ('mc2/aaxiscalibrationvelocityforward', 'f8', ()),
        ('mc2/aaxiscycletime', 'f8', ()),
        ('mc2/aaxisdec', 'f8', ()),
        ('mc2/aaxisdelaytimeveloposition', 'f8', ()),
        ('mc2/aaxisenableposcorrection', 'u1', ()),
        ('mc2/aaxisenbacklashcompensation', 'u1', ()),
        ('mc2/aaxisencoderdirectioninverse', 'u1', ()),
        ('mc2/aaxisencodermask', 'u4', ()),
        ('mc2/aaxisencodermodulovalue', 'f8', ()),
        ('mc2/aaxisencoderoffset', 'f8', ()),
        ('mc2/aaxisencoderscalingfactor', 'f8', ()),
        ('mc2/aaxisendatapersistence', 'u1', ()),
        ('mc2/aaxisenintargettimeout', 'u1', ()),
        ('mc2/aaxisenloopingdistance', 'u1', ()),
        ('mc2/aaxisenpositionlagmonitoring', 'u1', ()),
        ('mc2/aaxisenpositionrangemonitoring', 'u1', ()),
        ('mc2/aaxisentargetpositionmonitoring', 'u1', ()),
        ('mc2/aaxisfastacc', 'f8', ()),
        ('mc2/aaxisfastjerk', 'f8', ()),
        ('mc2/aaxisfaststopsignaltype', 'u4', ()),
        ('mc2/aaxisid', 'f8', ()),
        ('mc2/aaxisintargettimeout', 'f8', ()),
        ('mc2/aaxisjerk', 'f8', ()),
        ('mc2/aaxisjogincrementbackward', 'f8', ()),
        ('mc2/aaxisjogincrementforward', 'f8', ()),
        ('mc2/aaxisloopingdistance', 'f8', ()),
        ('mc2/aaxismanualvelocityfast', 'f8', ()),
        ('mc2/aaxismanualvelocityslow', 'f8', ()),
        ('mc2/aaxismaxposlagfiltertime', 'f8', ()),
        ('mc2/aaxismaxposlagvalue', 'f8', ()),
        ('mc2/aaxismaxvelocity', 'f8', ()),
        ('mc2/aaxismodulotolerancewindow', 'f8', ()),
        ('mc2/aaxismotionmonitoringtime', 'f8', ()),
        ('mc2/aaxismotionmonitoringwindow', 'f8', ()),
        ('mc2/aaxismotordirectioninverse', 'u1', ()),
        ('mc2/aaxisoverridetype', 'f8', ()),
        ('mc2/aaxisposcorrectionfiltertime', 'f8', ()),
        ('mc2/aaxispositionrangewindow', 'f8', ()),
        ('mc2/aaxisrapidtraversevelocity', 'f8', ()),
        ('mc2/aaxisrefveloonrefoutput', 'f8', ()),
        ('mc2/aaxistargetpositionmonitoringtime', 'f8', ()),
        ('mc2/aaxistargetpositionwindow', 'f8', ()),
        ('mc2/aaxisunitinterpretation', 'f8', ()),
        ('mc2/acommandedvelocity', 'f8', ()),
        ('mc2/aencoderaxisoffset', 'f8', ()),
        ('mc2/aencoderaxisscalingfactor', 'f8', ()),
        ('mc2/aencoderreferencemode', 'u1', ()),
        ('mc2/ahomingvelocitoffplccam', 'f8', ()),
        ('mc2/ahomingvelocittowardsplccam', 'f8', ()),
        ('mc2/ainvertdircalibrationcamsearch', 'u1', ()),
        ('mc2/ainvertdirsyncpulssearch', 'u1', ()),
        ('mc2/amodulotargetposition', 'f8', ()),
        ('mc2/amovedirection', 'i4', ()),
        ('mc2/ancsvbcycletime', 'f8', ()),
        ('mc2/axisenmotionmonitoring', 'u1', ()),
        ('mc2/axisfastdec', 'f8', ()),
        ('mc2/extendedStateWord', 'u4', ()),
        ('mc2/ncsafcycletime', 'f8', ()),
        ('mc2ContinuousMotion', 'u1', ()),
        ('mc2DiscreteMotion', 'u1', ()),
        ('mc2ErrorStop', 'u1', ()),
        ('pollInterval', 'f4', ()),
        ('softDeviceId', 'u4', ()),
        ('specificError', 'u4', ()),
        ('stepSize', 'f8', ()),
        ('swLimitHigh', 'f8', ()),
        ('swLimitLow', 'f8', ()),
        ('targetPosition', 'f8', ()),
        ('targetVelocity', 'f8', ()),
        ('terminal', 'u4', ()),
    ] + interlock_keys + triggers_keys