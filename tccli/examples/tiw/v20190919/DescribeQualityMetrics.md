**Example 1: 查询白板图片加载失败统计**



Input: 

```
tccli tiw DescribeQualityMetrics --cli-unfold-argument  \
    --SdkAppId 1400296030 \
    --Metric image_load_fail_count \
    --Interval 1h \
    --StartTime 1617874404 \
    --EndTime 1618479204
```

Output: 
```
{
    "Response": {
        "RequestId": "6c41b5df-2326-4c0b-baca-2fd85ebb4097",
        "Metric": "image_load_fail_count",
        "Content": [
            {
                "Time": 1617872400,
                "Value": 0
            }
        ]
    }
}
```

