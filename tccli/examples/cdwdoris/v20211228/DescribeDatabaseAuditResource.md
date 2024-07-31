**Example 1: DescribeDatabaseAuditResource**

获取审计日志的相关信息

Input: 

```
tccli cdwdoris DescribeDatabaseAuditResource --cli-unfold-argument  \
    --InstanceId abc
```

Output: 
```
{
    "Response": {
        "Databases": [
            "abc"
        ],
        "Users": [
            "abc"
        ],
        "SqlTypes": [
            "abc"
        ],
        "RequestId": "abc"
    }
}
```

