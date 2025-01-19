**Example 1: DescribeDatabaseAuditDownload**

下载数据库审计日志

Input: 

```
tccli cdwdoris DescribeDatabaseAuditDownload --cli-unfold-argument  \
    --InstanceId cdwdoris-akxtck1n \
    --StartTime 2025-01-06 09:36:04 \
    --EndTime 2025-01-06 10:36:04 \
    --PageSize 0 \
    --PageNum 1 \
    --OrderType DESC \
    --Sql 
```

Output: 
```
{
    "Response": {
        "CosUrl": "http://abc",
        "RequestId": "abc-1xas"
    }
}
```

