**Example 1: 修改实例用户的密码**



Input: 

```
tccli mongodb ResetDBInstancePassword --cli-unfold-argument  \
    --InstanceId cmgo-7pjedvz7 \
    --UserName rwuser \
    --Password 111111
```

Output: 
```
{
    "Response": {
        "AsyncRequestId": "4769",
        "RequestId": "e600a8d0-9014-11ea-84c1-01cccde830c6"
    }
}
```

