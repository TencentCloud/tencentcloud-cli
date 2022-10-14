**Example 1: 获取录制的时长统计数据**



Input: 

```
tccli trtc DescribeRecordStatistic --cli-unfold-argument  \
    --EndTime 2019-10-13 \
    --StartTime 2019-10-11 \
    --SdkAppId 1400123456
```

Output: 
```
{
    "Response": {
        "SdkAppIdUsages": [
            {
                "SdkAppId": "1400123456",
                "Usages": [
                    {
                        "TimeKey": "2019-10-11",
                        "Class1VideoTime": 556026,
                        "Class2VideoTime": 86361829,
                        "Class3VideoTime": 0,
                        "AudioTime": 64169044
                    },
                    {
                        "TimeKey": "2019-10-12",
                        "Class1VideoTime": 551103,
                        "Class2VideoTime": 85103796,
                        "Class3VideoTime": 0,
                        "AudioTime": 64156599
                    },
                    {
                        "TimeKey": "2019-10-13",
                        "Class1VideoTime": 515249,
                        "Class2VideoTime": 82982805,
                        "Class3VideoTime": 0,
                        "AudioTime": 65673394
                    }
                ]
            }
        ],
        "RequestId": "644956b8-9f7c-44c5-b833-31d91dba1b24"
    }
}
```

