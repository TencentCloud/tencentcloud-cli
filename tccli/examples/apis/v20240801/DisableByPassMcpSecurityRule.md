**Example 1: 禁用绕过mcp 安全规则**

禁用绕过mcp 安全规则

Input: 

```
tccli apis DisableByPassMcpSecurityRule --cli-unfold-argument  \
    --Type security_event_check \
    --InstanceID ins-9c4a1db3
```

Output: 
```
{
    "Response": {
        "Data": {
            "ID": "mr-4431f5d2"
        },
        "RequestId": "6bef837d-b7be-488c-9693-ea503d93faf0"
    }
}
```

