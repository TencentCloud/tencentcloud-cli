**Example 1: 删除凭据信息**



Input: 

```
tccli ssm DeleteSecret --cli-unfold-argument  \
    --SecretName test \
    --RecoveryWindowInDays 1
```

Output: 
```
{
    "Response": {
        "RequestId": "2609a8fd-4584-4f89-98be-8c7ae1b81ef4",
        "SecretName": "test",
        "DeleteTime": 1574247268
    }
}
```

