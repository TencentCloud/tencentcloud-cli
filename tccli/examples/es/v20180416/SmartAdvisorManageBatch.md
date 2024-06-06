**Example 1: demo**



Input: 

```
tccli es SmartAdvisorManageBatch --cli-unfold-argument  \
    --InstanceId es-q3qu29c7 \
    --StrategyName cluster.enable.opack \
    --StrategyType 2
```

Output: 
```
{
    "Response": {
        "StrategyResult": [
            {
                "StrategyName": "cluster.enable.opack",
                "StrategyValue": "true"
            }
        ],
        "RequestId": "abc"
    }
}
```

