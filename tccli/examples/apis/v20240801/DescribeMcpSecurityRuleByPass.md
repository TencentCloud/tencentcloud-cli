**Example 1: 查询mcp 安全规则ByPass状态**

查询mcp 安全规则ByPass状态

Input: 

```
tccli apis DescribeMcpSecurityRuleByPass --cli-unfold-argument  \
    --InstanceID ins-9c4a1db3 \
    --Type security_event_check
```

Output: 
```
{
    "Response": {
        "Data": {
            "ByPass": "open"
        },
        "RequestId": "85598f6d-547d-4663-970a-5277ab17ee26"
    }
}
```

