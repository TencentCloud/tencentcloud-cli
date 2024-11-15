**Example 1: 审核通过某客户**

对待审核某客户，给予审核通过操作

Input: 

```
tccli partners AuditApplyClient --cli-unfold-argument  \
    --Note reason \
    --AuditResult accept \
    --ClientUin 2000002
```

Output: 
```
{
    "Response": {
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03",
        "AuditResult": "qcloudaudit",
        "ClientUin": "2000002",
        "AgentTime": 1,
        "Uin": "1000001"
    }
}
```

