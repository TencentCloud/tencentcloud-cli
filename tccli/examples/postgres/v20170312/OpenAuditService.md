**Example 1: 开启审计日志**

开启审计日志

Input: 

```
tccli postgres OpenAuditService --cli-unfold-argument  \
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
        "RequestId": "3fcc8953-2d5e-4f76-9fcc-84272af76d89"
    }
}
```

