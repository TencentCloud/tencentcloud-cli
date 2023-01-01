**Example 1: 修改审计服务**



Input: 

```
tccli cynosdb ModifyAuditService --cli-unfold-argument  \
    --InstanceId cynosdbmysql-ins-6990cckk \
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

