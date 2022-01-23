**Example 1: 查询设备统计monitor信息**



Input: 

```
tccli iotvideoindustry DescribeDeviceMonitorData --cli-unfold-argument  \
    --StartTime 1624550400 \
    --EndTime 1624588948 \
    --Type RecordingChannels \
    --TimesSpec 1h
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "Value": 0,
                "Time": 1624550400
            },
            {
                "Value": 0,
                "Time": 1624554000
            },
            {
                "Value": 0,
                "Time": 1624557600
            },
            {
                "Value": 0,
                "Time": 1624561200
            },
            {
                "Value": 0,
                "Time": 1624564800
            },
            {
                "Value": 0,
                "Time": 1624568400
            },
            {
                "Value": 0,
                "Time": 1624572000
            },
            {
                "Value": 0,
                "Time": 1624575600
            },
            {
                "Value": 0,
                "Time": 1624579200
            },
            {
                "Value": 0,
                "Time": 1624582800
            },
            {
                "Value": 1,
                "Time": 1624586400
            }
        ],
        "RequestId": "119988ii"
    }
}
```

