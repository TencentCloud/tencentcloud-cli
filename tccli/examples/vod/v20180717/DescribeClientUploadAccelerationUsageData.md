**Example 1: 查询客户端上传加速统计数据**



Input: 

```
tccli vod DescribeClientUploadAccelerationUsageData --cli-unfold-argument  \
    --StartTime 2020-09-07T00:00:00+08:00 \
    --EndTime 2020-09-09T23:59:59+08:00 \
    --Type AccelerationWithQUIC
```

Output: 
```
{
    "Response": {
        "ClientUploadAccelerationUsageDataSet": [
            {
                "Time": "2020-09-07T00:00:00+08:00",
                "Value": 2
            },
            {
                "Time": "2020-09-08T00:00:00+08:00",
                "Value": 2
            },
            {
                "Time": "2020-09-09T00:00:00+08:00",
                "Value": 2
            }
        ],
        "RequestId": "requestId"
    }
}
```

