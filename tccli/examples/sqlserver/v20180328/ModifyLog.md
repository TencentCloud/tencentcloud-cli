**Example 1: 修改日志**



Input: 

```
tccli sqlserver ModifyLog --cli-unfold-argument  \
    --InstanceId mssql-8eei3sy5 \
    --LogType auditLog \
    --LogExpireDay 30 \
    --HighLogExpireDay 7
```

Output: 
```
{
    "Response": {
        "RequestId": "e7d8112c-4b91-42a9-a6e4-2cd202d00f3f"
    }
}
```

