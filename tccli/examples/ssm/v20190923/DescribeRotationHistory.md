**Example 1: 查询凭据轮转历史版本**



Input: 

```
tccli ssm DescribeRotationHistory --cli-unfold-argument  \
    --SecretName test
```

Output: 
```
{
    "Response": {
        "VersionIDs": [
            "testId"
        ],
        "TotalCount": 1,
        "RequestId": "2609a8fd-4584-4f89-98be-8c7ae1b81ef4"
    }
}
```

