**Example 1: 根据桶名获取COS产品用量明细**



Input: 

```
tccli billing DescribeDosageCosDetailByDate --cli-unfold-argument  \
    --StartDate 2020-09-01 \
    --EndDate 2020-09-30 \
    --BucketName systemcover-1000027
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
                "BucketName": "systemcover-1000027",
                "SubProductCodeName": "COS 标准存储",
                "BillingItemCodeName": "COS 标准存储存储容量",
                "Unit": "(GB)"
            },
            {
                "DosageValue": "0.00976562",
                "DosageBeginTime": "2020-09-02 00:00:00",
                "DosageEndTime": "2020-09-02 23:59:59",
                "BucketName": "systemcover-1000027",
                "SubProductCodeName": "COS 标准存储",
                "BillingItemCodeName": "COS 标准存储存储容量",
                "Unit": "(GB)"
            },
            {
                "DosageValue": "0.00976562",
                "DosageBeginTime": "2020-09-03 00:00:00",
                "DosageEndTime": "2020-09-03 23:59:59",
                "BucketName": "systemcover-1000027",
                "SubProductCodeName": "COS 标准存储",
                "BillingItemCodeName": "COS 标准存储存储容量",
                "Unit": "(GB)"
            },
            {
                "DosageValue": "0.00976562",
                "DosageBeginTime": "2020-09-04 00:00:00",
                "DosageEndTime": "2020-09-04 23:59:59",
                "BucketName": "systemcover-1000027",
                "SubProductCodeName": "COS 标准存储",
                "BillingItemCodeName": "COS 标准存储存储容量",
                "Unit": "(GB)"
            },
            {
                "DosageValue": "0.00976562",
                "DosageBeginTime": "2020-09-05 00:00:00",
                "DosageEndTime": "2020-09-05 23:59:59",
                "BucketName": "systemcover-1000027",
                "SubProductCodeName": "COS 标准存储",
                "BillingItemCodeName": "COS 标准存储存储容量",
                "Unit": "(GB)"
            },
            {
                "DosageValue": "0.00976562",
                "DosageBeginTime": "2020-09-06 00:00:00",
                "DosageEndTime": "2020-09-06 23:59:59",
                "BucketName": "systemcover-1000027",
                "SubProductCodeName": "COS 标准存储",
                "BillingItemCodeName": "COS 标准存储存储容量",
                "Unit": "(GB)"
            },
            {
                "DosageValue": "0.00976562",
                "DosageBeginTime": "2020-09-07 00:00:00",
                "DosageEndTime": "2020-09-07 23:59:59",
                "BucketName": "systemcover-1000027",
                "SubProductCodeName": "COS 标准存储",
                "BillingItemCodeName": "COS 标准存储存储容量",
                "Unit": "(GB)"
            },
            {
                "DosageValue": "0.00976562",
                "DosageBeginTime": "2020-09-08 00:00:00",
                "DosageEndTime": "2020-09-08 23:59:59",
                "BucketName": "systemcover-1000027",
                "SubProductCodeName": "COS 标准存储",
                "BillingItemCodeName": "COS 标准存储存储容量",
                "Unit": "(GB)"
            },
            {
                "DosageValue": "0.00976562",
                "DosageBeginTime": "2020-09-09 00:00:00",
                "DosageEndTime": "2020-09-09 23:59:59",
                "BucketName": "systemcover-1000027",
                "SubProductCodeName": "COS 标准存储",
                "BillingItemCodeName": "COS 标准存储存储容量",
                "Unit": "(GB)"
            },
            {
                "DosageValue": "0.00976562",
                "DosageBeginTime": "2020-09-10 00:00:00",
                "DosageEndTime": "2020-09-10 23:59:59",
                "BucketName": "systemcover-1000027",
                "SubProductCodeName": "COS 标准存储",
                "BillingItemCodeName": "COS 标准存储存储容量",
                "Unit": "(GB)"
            },
            {
                "DosageValue": "0.00976562",
                "DosageBeginTime": "2020-09-11 00:00:00",
                "DosageEndTime": "2020-09-11 23:59:59",
                "BucketName": "systemcover-1000027",
                "SubProductCodeName": "COS 标准存储",
                "BillingItemCodeName": "COS 标准存储存储容量",
                "Unit": "(GB)"
            },
            {
                "DosageValue": "0.00976562",
                "DosageBeginTime": "2020-09-12 00:00:00",
                "DosageEndTime": "2020-09-12 23:59:59",
                "BucketName": "systemcover-1000027",
                "SubProductCodeName": "COS 标准存储",
                "BillingItemCodeName": "COS 标准存储存储容量",
                "Unit": "(GB)"
            },
            {
                "DosageValue": "0.00976562",
                "DosageBeginTime": "2020-09-13 00:00:00",
                "DosageEndTime": "2020-09-13 23:59:59",
                "BucketName": "systemcover-1000027",
                "SubProductCodeName": "COS 标准存储",
                "BillingItemCodeName": "COS 标准存储存储容量",
                "Unit": "(GB)"
            },
            {
                "DosageValue": "0.00976562",
                "DosageBeginTime": "2020-09-14 00:00:00",
                "DosageEndTime": "2020-09-14 23:59:59",
                "BucketName": "systemcover-1000027",
                "SubProductCodeName": "COS 标准存储",
                "BillingItemCodeName": "COS 标准存储存储容量",
                "Unit": "(GB)"
            },
            {
                "DosageValue": "0.00976562",
                "DosageBeginTime": "2020-09-15 00:00:00",
                "DosageEndTime": "2020-09-15 23:59:59",
                "BucketName": "systemcover-1000027",
                "SubProductCodeName": "COS 标准存储",
                "BillingItemCodeName": "COS 标准存储存储容量",
                "Unit": "(GB)"
            },
            {
                "DosageValue": "0.00976562",
                "DosageBeginTime": "2020-09-16 00:00:00",
                "DosageEndTime": "2020-09-16 23:59:59",
                "BucketName": "systemcover-1000027",
                "SubProductCodeName": "COS 标准存储",
                "BillingItemCodeName": "COS 标准存储存储容量",
                "Unit": "(GB)"
            },
            {
                "DosageValue": "0.00976562",
                "DosageBeginTime": "2020-09-17 00:00:00",
                "DosageEndTime": "2020-09-17 23:59:59",
                "BucketName": "systemcover-1000027",
                "SubProductCodeName": "COS 标准存储",
                "BillingItemCodeName": "COS 标准存储存储容量",
                "Unit": "(GB)"
            },
            {
                "DosageValue": "0.00976562",
                "DosageBeginTime": "2020-09-18 00:00:00",
                "DosageEndTime": "2020-09-18 23:59:59",
                "BucketName": "systemcover-1000027",
                "SubProductCodeName": "COS 标准存储",
                "BillingItemCodeName": "COS 标准存储存储容量",
                "Unit": "(GB)"
            },
            {
                "DosageValue": "0.00976562",
                "DosageBeginTime": "2020-09-19 00:00:00",
                "DosageEndTime": "2020-09-19 23:59:59",
                "BucketName": "systemcover-1000027",
                "SubProductCodeName": "COS 标准存储",
                "BillingItemCodeName": "COS 标准存储存储容量",
                "Unit": "(GB)"
            },
            {
                "DosageValue": "0.00976562",
                "DosageBeginTime": "2020-09-20 00:00:00",
                "DosageEndTime": "2020-09-20 23:59:59",
                "BucketName": "systemcover-1000027",
                "SubProductCodeName": "COS 标准存储",
                "BillingItemCodeName": "COS 标准存储存储容量",
                "Unit": "(GB)"
            },
            {
                "DosageValue": "0.00976562",
                "DosageBeginTime": "2020-09-21 00:00:00",
                "DosageEndTime": "2020-09-21 23:59:59",
                "BucketName": "systemcover-1000027",
                "SubProductCodeName": "COS 标准存储",
                "BillingItemCodeName": "COS 标准存储存储容量",
                "Unit": "(GB)"
            },
            {
                "DosageValue": "0.00976562",
                "DosageBeginTime": "2020-09-22 00:00:00",
                "DosageEndTime": "2020-09-22 23:59:59",
                "BucketName": "systemcover-1000027",
                "SubProductCodeName": "COS 标准存储",
                "BillingItemCodeName": "COS 标准存储存储容量",
                "Unit": "(GB)"
            },
            {
                "DosageValue": "0.00976562",
                "DosageBeginTime": "2020-09-23 00:00:00",
                "DosageEndTime": "2020-09-23 23:59:59",
                "BucketName": "systemcover-1000027",
                "SubProductCodeName": "COS 标准存储",
                "BillingItemCodeName": "COS 标准存储存储容量",
                "Unit": "(GB)"
            },
            {
                "DosageValue": "0.00976562",
                "DosageBeginTime": "2020-09-24 00:00:00",
                "DosageEndTime": "2020-09-24 23:59:59",
                "BucketName": "systemcover-1000027",
                "SubProductCodeName": "COS 标准存储",
                "BillingItemCodeName": "COS 标准存储存储容量",
                "Unit": "(GB)"
            },
            {
                "DosageValue": "0.00976562",
                "DosageBeginTime": "2020-09-25 00:00:00",
                "DosageEndTime": "2020-09-25 23:59:59",
                "BucketName": "systemcover-1000027",
                "SubProductCodeName": "COS 标准存储",
                "BillingItemCodeName": "COS 标准存储存储容量",
                "Unit": "(GB)"
            },
            {
                "DosageValue": "0.00976562",
                "DosageBeginTime": "2020-09-26 00:00:00",
                "DosageEndTime": "2020-09-26 23:59:59",
                "BucketName": "systemcover-1000027",
                "SubProductCodeName": "COS 标准存储",
                "BillingItemCodeName": "COS 标准存储存储容量",
                "Unit": "(GB)"
            },
            {
                "DosageValue": "0.00976562",
                "DosageBeginTime": "2020-09-27 00:00:00",
                "DosageEndTime": "2020-09-27 23:59:59",
                "BucketName": "systemcover-1000027",
                "SubProductCodeName": "COS 标准存储",
                "BillingItemCodeName": "COS 标准存储存储容量",
                "Unit": "(GB)"
            },
            {
                "DosageValue": "0.00976562",
                "DosageBeginTime": "2020-09-28 00:00:00",
                "DosageEndTime": "2020-09-28 23:59:59",
                "BucketName": "systemcover-1000027",
                "SubProductCodeName": "COS 标准存储",
                "BillingItemCodeName": "COS 标准存储存储容量",
                "Unit": "(GB)"
            },
            {
                "DosageValue": "0.00976562",
                "DosageBeginTime": "2020-09-29 00:00:00",
                "DosageEndTime": "2020-09-29 23:59:59",
                "BucketName": "systemcover-1000027",
                "SubProductCodeName": "COS 标准存储",
                "BillingItemCodeName": "COS 标准存储存储容量",
                "Unit": "(GB)"
            },
            {
                "DosageValue": "0.00976562",
                "DosageBeginTime": "2020-09-30 00:00:00",
                "DosageEndTime": "2020-09-30 23:59:59",
                "BucketName": "systemcover-1000027",
                "SubProductCodeName": "COS 标准存储",
                "BillingItemCodeName": "COS 标准存储存储容量",
                "Unit": "(GB)"
            }
        ],
        "RequestId": "4c714162-6ffb-4666-afc7-33b2585b86ab"
    }
}
```

