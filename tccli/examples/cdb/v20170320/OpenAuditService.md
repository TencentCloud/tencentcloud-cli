**Example 1: 开通实例审计服务**



Input: 

```
tccli cdb OpenAuditService --cli-unfold-argument  \
    --InstanceId cdb-1j75n2zz \
    --LogExpireDay 7 \
    --HighLogExpireDay 1
```

Output: 
```
{
    "Response": {
        "RequestId": "43-12121-812w1221213-62usf6123"
    }
}
```

