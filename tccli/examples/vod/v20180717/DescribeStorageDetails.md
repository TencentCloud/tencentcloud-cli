**Example 1: 查询点播存储统计数据**

查询2018年12月1日（含）到2018年12月7日（含）的存储空间数据。

Input: 

```
tccli vod DescribeStorageDetails --cli-unfold-argument  \
    --StartTime 2018-12-01T00:00:00+08:00 \
    --EndTime 2018-12-07T00:00:00+08:00 \
    --Area 'Chinese Mainland'
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "Time": "2018-12-01T00:00:00+08:00",
                "Value": 1000000
            },
            {
                "Time": "2018-12-02T00:00:00+08:00",
                "Value": 1500000
            },
            {
                "Time": "2018-12-03T00:00:00+08:00",
                "Value": 1500000
            },
            {
                "Time": "2018-12-04T00:00:00+08:00",
                "Value": 1500000
            },
            {
                "Time": "2018-12-05T00:00:00+08:00",
                "Value": 1500000
            },
            {
                "Time": "2018-12-06T00:00:00+08:00",
                "Value": 1500000
            },
            {
                "Time": "2018-12-07T00:00:00+08:00",
                "Value": 1500000
            }
        ],
        "RequestId": "requestId"
    }
}
```

