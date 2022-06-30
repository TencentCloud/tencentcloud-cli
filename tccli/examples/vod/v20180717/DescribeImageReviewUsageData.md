**Example 1: 查询图片审核统计数据**



Input: 

```
tccli vod DescribeImageReviewUsageData --cli-unfold-argument  \
    --EndTime 2020-09-09T23:59:59+08:00 \
    --StartTime 2020-09-07T00:00:00+08:00
```

Output: 
```
{
    "Response": {
        "ImageReviewUsageDataSet": [
            {
                "Time": "2020-09-07T00:00:00+08:00",
                "Count": 2
            },
            {
                "Time": "2020-09-08T00:00:00+08:00",
                "Count": 2
            },
            {
                "Time": "2020-09-09T00:00:00+08:00",
                "Count": 2
            }
        ],
        "RequestId": "requestId"
    }
}
```

