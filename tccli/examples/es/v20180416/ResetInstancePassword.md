**Example 1: 重置集群实例cam账号密码**



Input: 

```
tccli es ResetInstancePassword --cli-unfold-argument  \
    --UserResourceId es-f90lqeug \
    --ResourceRegion ap-guangzhou \
    --ResourceAccount test2 \
    --Password elastic@123 \
    --AccountHost %
```

Output: 
```
{
    "Response": {
        "ResetTimestamp": 1760694123,
        "TimeCost": 120,
        "RequestId": "312a7ccb-c255-479d-b261-8563740abf8d"
    }
}
```

