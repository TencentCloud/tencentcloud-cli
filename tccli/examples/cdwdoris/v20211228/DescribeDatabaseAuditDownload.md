**Example 1: DescribeDatabaseAuditDownload**

下载数据库审计日志

Input: 

```
tccli cdwdoris DescribeDatabaseAuditDownload --cli-unfold-argument  \
    --InstanceId abc \
    --StartTime abc \
    --EndTime abc \
    --PageSize 0 \
    --PageNum 0 \
    --OrderType abc \
    --User abc \
    --DbName abc \
    --SqlType abc \
    --Sql abc \
    --Users abc \
    --DbNames abc \
    --SqlTypes abc
```

Output: 
```
{
    "Response": {
        "CosUrl": "abc",
        "RequestId": "abc"
    }
}
```

