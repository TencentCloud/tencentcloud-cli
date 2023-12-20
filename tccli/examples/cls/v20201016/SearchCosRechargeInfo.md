**Example 1: 预览cos导入信息**



Input: 

```
tccli cls SearchCosRechargeInfo --cli-unfold-argument  \
    --TopicId e6a94ed2-8191-49ac-ab67-90e33d2f1111 \
    --LogsetId 11114ed2-8191-49ac-ab67-90e33d2f3974 \
    --Name test_name \
    --Bucket examplebucket-1-1250000000 \
    --BucketRegion ap-guangzhou \
    --Prefix text_prefix \
    --Compress gzip
```

Output: 
```
{
    "Response": {
        "Msg": "",
        "Status": 0,
        "Data": [
            "2021-11-09 20:16:29.038 INFO    apis/report.go:108      report data success, size 1",
            "2021-11-09 20:16:29.039 INFO    apis/report.go:108      report data success, size 1",
            "2021-11-09 20:16:29.040 INFO    apis/report.go:108      report data success, size 1",
            "2021-11-09 20:16:29.041 INFO    apis/report.go:108      report data success, size 1",
            "2021-11-09 20:16:29.042 INFO    apis/report.go:108      report data success, size 1"
        ],
        "Sum": 10000,
        "Path": "https://bucket1.ap-guangzhou.myqcloud.com/csv/g_xxx.gz",
        "RequestId": "e6a94ed2-8191-49ac-ab67-90e33d2f3974"
    }
}
```

