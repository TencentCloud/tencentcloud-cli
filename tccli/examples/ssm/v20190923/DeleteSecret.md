**Example 1: 删除凭据**



Input: 

```
tccli ssm DeleteSecret --cli-unfold-argument  \
    --SecretName test-vab-206615 \
    --RecoveryWindowInDays 0 \
    --DeleteMode 1
```

Output: 
```
{
    "Response": {
        "DeleteTime": 1784001025,
        "FlowID": 75810,
        "SecretName": "test-vab-206615",
        "RequestId": "dff868ed-194f-496a-8bf3-3f04ea4a8050"
    }
}
```

