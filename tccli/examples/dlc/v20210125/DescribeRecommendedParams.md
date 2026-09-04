**Example 1: 获取推荐的高级参数**



Input: 

```
tccli dlc DescribeRecommendedParams --cli-unfold-argument  \
    --ModelUid m-xgboost-mao-6a2fc583-14cb \
    --Engine vllm
```

Output: 
```
{
    "Response": {
        "AdvancedParams": {
            "EngineArgs": [],
            "EnvVars": [],
            "GpuMemoryUtilization": 0,
            "RayOptions": []
        },
        "Source": "default",
        "RequestId": "9f2a4042-0fc4-4611-b091-486886322290"
    }
}
```

