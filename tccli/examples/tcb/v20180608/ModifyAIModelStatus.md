**Example 1: 打开单个模型**



Input: 

```
tccli tcb ModifyAIModelStatus --cli-unfold-argument  \
    --EnvId ************************** \
    --GroupName cloudbase \
    --Models.0.Model deepseek-v4-pro \
    --Models.0.Status ENABLE
```

Output: 
```
{
    "Response": {
        "Count": 1,
        "RequestId": "6a8f8d31-5bb9-40e4-8d42-04746e1b2cd9"
    }
}
```

