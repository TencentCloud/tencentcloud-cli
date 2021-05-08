**Example 1: 查询通用资源配额信息**

查询实例资源配额信息

Input: 

```
tccli lighthouse DescribeGeneralResourceQuotas --cli-unfold-argument  \
    --ResourceNames INSTANCE
```

Output: 
```
{
    "Response": {
        "GeneralResourceQuotaSet": [
            {
                "ResourceName": "INSTANCE",
                "ResourceQuotaAvailable": 9,
                "ResourceQuotaTotal": 10
            }
        ],
        "RequestId": "4dd1a440-39ca-49fb-9f2f-c995db3ae20b"
    }
}
```

