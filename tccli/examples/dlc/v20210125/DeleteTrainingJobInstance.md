**Example 1: 删除训练作业实例（软删除本地元数据，仅终态实例可删除）**



Input: 

```
tccli dlc DeleteTrainingJobInstance --cli-unfold-argument  \
    --InstanceId rayjob-20260714164222-1jrz
```

Output: 
```
{
    "Response": {
        "RequestId": "7e5896e7-e9f6-4db2-9c37-fea3102aa400"
    }
}
```

