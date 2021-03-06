# Make sure to have the server side running in V-REP:
# in a child script of a V-REP scene, add following command
# to be executed just once, at simulation start:
#
# simExtRemoteApiStart(19999)
#
# then start simulation, and run this program.
#
# IMPORTANT: for each successful call to simxStart, there
# should be a corresponding call to simxFinish at the end!

import vrep, math, pyke.knowledge_engine

# get distance to obstacle detected by a given sensor
def getObstacleDist(sensorHandler_):
    dist2Obstacle_LR = [0.0, 0.0]
    # Get raw sensor readings using API
    rawSR = vrep.simxReadProximitySensor(clientID, sensorHandler_, vrep.simx_opmode_oneshot_wait)
    # Calculate Euclidean distance
    distance_ = math.sqrt(rawSR[2][0]*rawSR[2][0] + rawSR[2][1]*rawSR[2][1] + rawSR[2][2]*rawSR[2][2])
    return distance_

def calculateObstacleField(distVector):
    resultVector=[0,0,0]
    for distance in distVector:
        if(distance!=None):
            print distance
            resultVector[0]-=1/(distance[0]*1000)
            resultVector[1]-=1/(distance[1]*1000)
            resultVector[2]-=1/(distance[2]*1000)
    return resultVector

# def getMotorSpeed(dist):
#      if (dist[0] < 0.5) or (dist[1] < 0.5):
#          if(dist[5]>0.3 and dist[0]>0.15):
#              motorSpeed=dict(speedLeft=2, speedRight=0)
#          elif(dist[4]>0.3 and dist[1]>0.15):
#              motorSpeed=dict(speedLeft=0, speedRight=2)
#          else:
#              motorSpeed= dict(speedLeft=-2, speedRight=-2)
#      else:
#         motorSpeed= dict(speedLeft=2, speedRight=2)
#      return motorSpeed

# agent's reasoning procedure, using PyKE
def getMotorSpeedPyKE(dist):
    # Create Engine
    engine = pyke.knowledge_engine.engine('.')
    # Reset Engine, make sure no (old) specific fact exist
    engine.reset()
    # activate rules
    engine.activate('pioneer')
    # add percepts to the knowledge base
    engine.assert_('env', 'dist',('FFLeft', dist[0]))
    engine.assert_('env', 'dist',('FFRight', dist[1]))
    engine.assert_('env', 'dist',('FLeft', dist[2]))
    engine.assert_('env', 'dist',('FRight', dist[3]))
    engine.assert_('env', 'dist',('Left', dist[4]))
    engine.assert_('env', 'dist',('Right', dist[5]))
    engine.assert_('env', 'dist',('BLeft', dist[6]))
    engine.assert_('env', 'dist',('BRight', dist[7]))

    # deduce what action to take
    vars, plan = engine.prove_1_goal('env.action($speedLeft,$speedRight)')
    print ' MotorSpeed: ', vars
    engine.print_stats()
    return vars

# execute agent's action
def execute(motorSpeed):
    vrep.simxSetJointTargetVelocity(clientID, leftMotorHandle, motorSpeed['speedLeft'], vrep.simx_opmode_oneshot )
    vrep.simxSetJointTargetVelocity(clientID, rightMotorHandle, motorSpeed['speedRight'], vrep.simx_opmode_oneshot )

# set new position for plant
def movePlant():
    dist2Plant = math.sqrt(pos2Plant[1][0]*pos2Plant[1][0] + pos2Plant[1][1]*pos2Plant[1][1] + pos2Plant[1][2]*pos2Plant[1][2])
    currentPlantPosition = vrep.simxGetObjectPosition(clientID, indoorPlantHandle, -1, vrep.simx_opmode_oneshot)
    plantPosition = [[2, 2, 0.1], [-2, -2, 0.1]]
    if dist2Plant < 0.8:
        if currentPlantPosition[0] > 0:
            PosIdx = 1
        else:
            PosIdx = 0
        vrep.simxSetObjectPosition(clientID, indoorPlantHandle, -1, plantPosition[PosIdx], vrep.simx_opmode_oneshot)

print 'Program started'
vrep.simxFinish(-1) # just in case, close all opened connections

int_portNb = 19999 # define port_nr
clientID = vrep.simxStart( '127.0.0.1', int_portNb, True, True, 5000, 5) # connect to server
if clientID != -1:
    print 'Connected to remote API server'
    res,objs = vrep.simxGetObjects(clientID,vrep.sim_handle_all,vrep.simx_opmode_oneshot_wait) # get all objects in the scene
    if res == vrep.simx_return_ok: # Remote function call succeeded
        print 'Number of objects in the scene: ',len(objs)# print number of object in the scene

        ret_lm,  leftMotorHandle = vrep.simxGetObjectHandle(clientID, 'Pioneer_p3dx_leftMotor', vrep.simx_opmode_oneshot_wait)
        ret_rm,  rightMotorHandle = vrep.simxGetObjectHandle(clientID, 'Pioneer_p3dx_rightMotor', vrep.simx_opmode_oneshot_wait)
        ret_pr,  pioneerRobotHandle = vrep.simxGetObjectHandle(clientID, 'Pioneer_p3dx', vrep.simx_opmode_oneshot_wait)
        ret_pl,  indoorPlantHandle = vrep.simxGetObjectHandle(clientID, 'indoorPlant', vrep.simx_opmode_oneshot_wait)
        ret_sl,  ultraSonicSensorStraightLeft = vrep.simxGetObjectHandle(clientID, 'Pioneer_p3dx_ultrasonicSensor' + str(4),vrep.simx_opmode_oneshot_wait)
        ret_sr,  ultraSonicSensorStraightRight = vrep.simxGetObjectHandle(clientID, 'Pioneer_p3dx_ultrasonicSensor' + str(5),vrep.simx_opmode_oneshot_wait)
        ret_sr,  ultraSonicSensorAngleLeft = vrep.simxGetObjectHandle(clientID, 'Pioneer_p3dx_ultrasonicSensor' + str(3),vrep.simx_opmode_oneshot_wait)
        ret_sr,  ultraSonicSensorAngleRight = vrep.simxGetObjectHandle(clientID, 'Pioneer_p3dx_ultrasonicSensor' + str(6),vrep.simx_opmode_oneshot_wait)
        ret_sr,  ultraSonicSensorLeft = vrep.simxGetObjectHandle(clientID, 'Pioneer_p3dx_ultrasonicSensor' + str(1),vrep.simx_opmode_oneshot_wait)
        ret_sr,  ultraSonicSensorRight = vrep.simxGetObjectHandle(clientID, 'Pioneer_p3dx_ultrasonicSensor' + str(8),vrep.simx_opmode_oneshot_wait)
        ret_sr,  ultraSonicSensorBackLeft = vrep.simxGetObjectHandle(clientID, 'Pioneer_p3dx_ultrasonicSensor' + str(14),vrep.simx_opmode_oneshot_wait)
        ret_sr,  ultraSonicSensorBackRight = vrep.simxGetObjectHandle(clientID, 'Pioneer_p3dx_ultrasonicSensor' + str(10),vrep.simx_opmode_oneshot_wait)

        sensorHandleList=[(sensorNumber,vrep.simxGetObjectHandle(clientID, 'Pioneer_p3dx_ultrasonicSensor' + str(sensorNumber),vrep.simx_opmode_oneshot_wait)[1]) for sensorNumber in range(1,17) ]
        error,currentOrientationEuler=vrep.simxGetObjectOrientation(clientID,pioneerRobotHandle,-1,vrep.simx_opmode_streaming)
        while True: # main Control loop

            #################################################
            # Perception Phase: Get information about environment
            ##############################################

            # distance to plant
            pos2Plant = vrep.simxGetObjectPosition(clientID, pioneerRobotHandle, indoorPlantHandle, vrep.simx_opmode_oneshot_wait)
            movePlant()

            # distance to obstacle, return [distLeft, distRight]
            dist2Obstacle= [(sensorNumber,getObstacleDist(sensor)) for sensorNumber,sensor in sensorHandleList]

            ########################################
            # Reasoning: figure out which action to take
            ########################################

            # get motor speed using IF-THEN rule
            #motorSpeed = getMotorSpeed(dist2Obstacle_LR)
            print pos2Plant
            # get motor speed using PyKE
            #motorSpeed = getMotorSpeedPyKE(dist2Obstacle)
            #motorSpeed=getMotorSpeedToPlant(dist2ObstacleVector,pos2Plant)
            ########################################
            # Action Phase: Assign speed to wheels
            ########################################
            execute(motorSpeed)
    else:
        print 'Remote API function call returned with error code: ',res
    vrep.simxFinish(clientID) # close all opened connections
else:
    print 'Failed connecting to remote API server'
    print 'Program finished'
