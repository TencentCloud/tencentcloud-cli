**Example 1: 审核通过某客户**

对待审核某客户，给予审核通过操作

Input: 

```
tccli partners AuditApplyClient --cli-unfold-argument  \
    --ClientUin 123456\
    --AuditResult accept\
    --Note reason
```

Output: 
```
{
    "Response": {
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03",
        "Uin": "1111111",
        "ClientUin": "22222222",
        "AuditResult": "qcloudaudit"
    }
}
```

