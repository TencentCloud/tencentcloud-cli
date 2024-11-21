**Example 1: 查询凭据轮转详情**



Input: 

```
tccli ssm DescribeRotationDetail --cli-unfold-argument  \
    --SecretName test3-db-secret
```

Output: 
```
{
    "Response": {
        "EnableRotation": true,
        "Frequency": 30,
        "LatestRotateTime": "2024-10-30 16:24:48",
        "NextRotateBeginTime": "2024-10-31 11:11:00",
        "RequestId": "d44e1c39-1e87-4ebe-ac8f-e06d0885971d"
    }
}
```

