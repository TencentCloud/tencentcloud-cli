**Example 1: 修改审计服务**

无

Input: 

```
tccli cdb ModifyAuditService --cli-unfold-argument  \
    --InstanceId cdb-6990cckk \
    --LogExpireDay 30 \
    --HighLogExpireDay 7 \
    --AuditAll True
```

Output: 
```
{
    "Response": {
        "RequestId": "43-12121-812w1221213-62usf9093"
    }
}
```

