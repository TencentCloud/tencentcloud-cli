**Example 1: 修改审计**

修改审计

Input: 

```
tccli postgres ModifyAuditService --cli-unfold-argument  \
    --InstanceId postgres-nqg1hcnj \
    --LogExpireDay 7 \
    --HotLogExpireDay 7 \
    --AuditType complex \
    --Product postgres
```

Output: 
```
{
    "Response": {
        "RequestId": "ddc6e275-dac8-42d3-a64d-b51c01e0d6e1"
    }
}
```

