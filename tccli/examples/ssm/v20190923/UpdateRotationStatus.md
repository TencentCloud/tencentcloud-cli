**Example 1: 设置云产品凭据轮转策略**



Input: 

```
tccli ssm UpdateRotationStatus --cli-unfold-argument  \
    --SecretName test \
    --EnableRotation true \
    --Frequency 35 \
    --RotationBeginTime '2006-01-02 15:04:05'
```

Output: 
```
{
    "Response": {
        "RequestId": "2609a8fd-4584-4f89-98be-8c7ae1b81ef4"
    }
}
```

