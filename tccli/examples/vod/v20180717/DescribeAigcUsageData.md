**Example 1: 查询AI生成视频的用量数据**



Input: 

```
tccli vod DescribeAigcUsageData --cli-unfold-argument  \
    --StartTime 2025-11-18T00:00:00+08:00 \
    --EndTime 2025-11-19T23:59:00+08:00 \
    --AigcType Video
```

Output: 
```
{
    "Response": {
        "AigcUsageDataSet": [
            {
                "DataSet": [
                    {
                        "Count": 0,
                        "Time": "2025-11-17T00:00:00+08:00",
                        "Usage": 0
                    },
                    {
                        "Count": 3,
                        "Time": "2025-11-18T00:00:00+08:00",
                        "Usage": 15
                    },
                    {
                        "Count": 0,
                        "Time": "2025-11-19T00:00:00+08:00",
                        "Usage": 0
                    }
                ],
                "Specification": "Kling2.0&2.1std_720P"
            }
        ],
        "RequestId": "2f47fc6d-c03a-49f7-b50b-xxxxxxxx"
    }
}
```

