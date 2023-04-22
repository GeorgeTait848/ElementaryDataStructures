import time
from dataStructures import LinkedList, Node, TwoSum
import plotly.graph_objects as go
import inspect
import numpy as np



def hasMethod(dataStructure, methodName: str) -> bool:

    attr = getattr(dataStructure, methodName, None)
    if not attr: 
        return False
    
    return callable(attr)


def getFunctionParameters(func: callable):

    signature = inspect.signature(func)
    paramNames = [param.name for param in signature.parameters.values()]

    try: 
        paramNames.remove('self')
        return paramNames

    except:
        return paramNames



def hasCorrectParameters(func: callable, params: dict):

    funcArgs = getFunctionParameters(func)
    return all(arg in params for arg in funcArgs)



def getMissingArgs(func: callable, params: dict):

    args = getFunctionParameters(func)
    missingArgs =  list(filter(lambda x: x not in params, args))

    return ", ".join(missingArgs)   


def getComputationTimes(dataStructure, operationName: str, lens: list[int], **kwargs):

    '''Calculates the computation time of an operation (algorithm) on any data structure that can be initialised with only a list. 
    e.g: LinkedList([0,1,2]) '''
    

    if not hasMethod(dataStructure, operationName):
        raise Exception('The data Structure has no method {}'.format(operationName))
    

    operation = getattr(dataStructure, operationName)

    if not hasCorrectParameters(operation, kwargs):

        missingArgs = getMissingArgs(operation, kwargs)
        raise Exception('kwargs missing arguments: {} for operation {}'.format(missingArgs, operationName))

    

    instances = [dataStructure([0 for _ in range(l)]) for l in lens]
    times = [0 for _ in lens]


    for i in range(len(lens)):
        
        start = time.time()
        operation(instances[i], **kwargs)
        end=time.time()

        times[i] = (end-start)/1e-3

    return times
    



def plotTimeComplexity(dataStructure, operationName: str, lens: list[int], **kwargs):

    times = getComputationTimes(dataStructure, operationName, lens, **kwargs)

    lnLens = np.log(lens)
    lnTimes = np.log(times)

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=lnLens,
        y=lnTimes, 
        mode='lines+markers', 
        line=dict(width=1), 
        marker=dict(size=12)
    ))

    fig.update_layout(
        xaxis_title = r"$\ln{L}$",
        yaxis_title = r"$\ln{T}$", 
        title_text = "Time Complexity of algorithm {} for data structure {}".format(operationName, dataStructure.__name__),
        title_font = dict(size=25),
        title_x = 0.5
    )
    
    
    grad, _ = np.polyfit(lnLens, lnTimes, deg=1)

    fig.add_annotation(
        text="Time complexity of order {}".format(np.round(grad, 2)), 
        x=np.mean(lnLens), 
        y=max(lnTimes), showarrow=False, 
        font=dict(size=25, ))

    fig.show()



def main():

    lens = [1_000, 10_000, 100_000, 1_000_000]

    plotTimeComplexity(LinkedList, 'addFirst', lens, node=Node(0))

    # plotTimeComplexity(LinkedList, 'addLast', lens, node=Node(0))
    # plotTimeComplexity(TwoSum, 'useLoop', lens, target=1)
    # plotTimeComplexity(TwoSum, 'useHashMap', lens, target=1)


if __name__ == "__main__":
    main()
