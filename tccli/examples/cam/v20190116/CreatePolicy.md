**Example 1: 创建一个策略**

以下示例将创建一个允许cos所有API访问所有的cos资源的策略

Input: 

```
tccli cam CreatePolicy --cli-unfold-argument  \
    --PolicyName test-2019-04-29 \
    --Description 策略描述 \
    --PolicyDocument {"version":"2.0","statement":[{"effect":"allow","action":["name/cos:*"],"resource":["*"]}]}
```

Output: 
```
{
    "Response": {
        "PolicyId": 17698703,
        "RequestId": "89360f78-b1dd-4e43-aa91-ecb2c8b8f282"
    }
}
```

