**Example 1: ES 云顾问管理接口**



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
        "RequestId": "xxx-xxxx"
    }
}
```

