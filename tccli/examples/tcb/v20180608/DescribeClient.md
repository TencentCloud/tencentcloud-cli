**Example 1: 查询客户端详情**



Input: 

```
tccli tcb DescribeClient --cli-unfold-argument  \
    --EnvId env-123 \
    --Id env-123
```

Output: 
```
{
    "Response": {
        "RequestId": "req_123",
        "Id": "env-123",
        "RefreshTokenExpiresIn": 2592000,
        "AccessTokenExpiresIn": 7200,
        "MaxDevice": 1,
        "CreatedAt": "2020-09-22T00:00:00+00:00",
        "UpdatedAt": "2024-01-01T00:00:00+00:00"
    }
}
```

