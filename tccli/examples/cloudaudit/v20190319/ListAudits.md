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
                "AuditName": "xxxxxx",
                "CosBucketName": "ccczzz",
                "LogFilePrefix": "xxxx",
                "AuditStatus": 1
            }
        ],
        "RequestId": "c4496845-6b3b-4e23-8045-e2060b0405a4"
    }
}
```

