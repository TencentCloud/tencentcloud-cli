**Example 1: 查询跟踪集概要**

查询跟踪集概要

Input: 

```
tccli cloudaudit ListAudits --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "AuditSummarys": [
            {
                "AuditStatus": 0,
                "CosBucketName": "bucket",
                "AuditName": "test",
                "LogFilePrefix": "audit"
            }
        ],
        "RequestId": "4c17b8ae-6b1e-4e68-bcff-825d73916011"
    }
}
```

