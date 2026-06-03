**Example 1: 关闭审计日志**

关闭审计日志

Input: 

```
tccli postgres CloseAuditService --cli-unfold-argument  \
    --InstanceId postgres-nqg1hcnj \
    --Product postgres
```

Output: 
```
{
    "Response": {
        "RequestId": "97e71166-704f-4ef1-8b7e-e84edfe99532"
    }
}
```

