**Example 1: 根据桶名获取COS产品用量明细**

COS产品用量明细查询

Input: 

```
tccli billing DescribeDosageCosDetailByDate --cli-unfold-argument  \
    --StartDate 2020-09-01 \
    --EndDate 2020-09-30 \
    --BucketName systemcover-xxxx
```

Output: 
```
{
    "Response": {
        "DetailSets": [
            {
                "DosageValue": "0.00976562",
                "DosageBeginTime": "2020-09-01 00:00:00",
                "DosageEndTime": "2020-09-01 23:59:59",
                "BucketName": "systemcover-xxxx",
                "SubProductCodeName": "COS 标准存储",
                "BillingItemCodeName": "COS 标准存储存储容量",
                "Unit": "(GB)"
            },
            {
                "DosageValue": "0.00976562",
                "DosageBeginTime": "2020-09-02 00:00:00",
                "DosageEndTime": "2020-09-02 23:59:59",
                "BucketName": "systemcover-xxxx",
                "SubProductCodeName": "COS 标准存储",
                "BillingItemCodeName": "COS 标准存储存储容量",
                "Unit": "(GB)"
            }
        ],
        "RequestId": "4c714162-6ffb-4666-afc7-33b2585b86ab"
    }
}
```

