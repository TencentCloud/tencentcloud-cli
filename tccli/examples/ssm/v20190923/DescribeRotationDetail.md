**Example 1: 查询凭据轮转详情**



Input: 

```
tccli ssm DescribeRotationDetail --cli-unfold-argument  \
    --SecretName test
```

Output: 
```
{
    "Response": {
        "RequestId": "2609a8fd-4584-4f89-98be-8c7ae1b81ef4",
        "EnableRotation": true,
        "Frequency": 35,
        "LatestRotateTime": "2021-01-02 15:04:05",
        "NextRotateBeginTime": "2021-02-02 15:04:05"
    }
}
```

