**Example 1: 审核通过某客户**

对待审核某客户，给予审核通过操作

Input: 

```
tccli partners AuditApplyClient --cli-unfold-argument  \
    --ClientUin 123456 \
    --AuditResult accept \
    --Note reason
```

Output: 
```
{
    "Response": {
        "RequestId": "xx",
        "AuditResult": "xx",
        "ClientUin": "xx",
        "AgentTime": 1,
        "Uin": "xx"
    }
}
```

