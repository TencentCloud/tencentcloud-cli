**Example 1: 获取某一天云存时间轴**



Input: 

```
tccli iotvideo DescribeCloudStorageTime --cli-unfold-argument  \
    --ProductId AQTV2839QJ \
    --DeviceName p2p_32731213_1 \
    --Date 2021-01-14
```

Output: 
```
{
    "Response": {
        "RequestId": "ac74ecca-b866-4ab1-87e0-18b92816fb20",
        "Data": {
            "VideoURL": "47b9d579-9088-4cc2-a16e-2b8cf245319b",
            "TimeList": [
                {
                    "StartTime": 1610607600,
                    "EndTime": 1610608200
                },
                {
                    "StartTime": 1610607600,
                    "EndTime": 1610608200
                },
                {
                    "StartTime": 1610607600,
                    "EndTime": 1610608200
                },
                {
                    "StartTime": 1610607600,
                    "EndTime": 1610608200
                }
            ]
        }
    }
}
```

