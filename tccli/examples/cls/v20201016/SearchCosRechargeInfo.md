**Example 1: 预览cos导入信息**



Input: 

```
tccli cls SearchCosRechargeInfo --cli-unfold-argument  \
    --TopicId xxx-xxx-xxx-xxx \
    --LogsetId xxx-xxx-xxx-xxx \
    --Name test_name \
    --Bucket test_bucket \
    --BucketRegion gz_open \
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

