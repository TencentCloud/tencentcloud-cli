**Example 1: 开启日志**



Input: 

```
tccli sqlserver OpenLog --cli-unfold-argument  \
    --InstanceId mssql-8eei3sy5 \
    --LogType auditLog \
    --LogExpireDay 30 \
    --HighLogExpireDay 7
```

Output: 
```
{
    "Response": {
        "RequestId": "e8e9d3de-b429-460c-9a95-aa2805f42be2"
    }
}
```

