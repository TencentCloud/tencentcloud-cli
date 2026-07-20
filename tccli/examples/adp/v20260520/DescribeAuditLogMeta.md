**Example 1: 查询审计日志元信息**



Input: 

```
tccli adp DescribeAuditLogMeta --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Actions": [
            {
                "Key": "create",
                "Name": "新建"
            }
        ],
        "BizObjects": [
            {
                "Key": "app",
                "Name": "应用"
            }
        ],
        "RequestId": "a398a630-d061-4dbe-a353-2e4943d11182"
    }
}
```

