**Example 1: CreateUserQuota**



Input: 

```
tccli goosefs CreateUserQuota --cli-unfold-argument  \
    --FileSystemId x-c60-4lu862qo \
    --QuotaType UID \
    --QuotaObjectName 40002 \
    --QuotaSizeLimit 100G \
    --QuotaFilesLimit 1000000
```

Output: 
```
{
    "Response": {
        "QuotaId": "quota_1754029945731",
        "RequestId": "4693f5a8-3060-4658-aa43-a80de6ecd620"
    }
}
```

