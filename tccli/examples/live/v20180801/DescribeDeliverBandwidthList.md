**Example 1: 请求示例**

查询直播转推计费带宽。

Input: 

```
tccli live DescribeDeliverBandwidthList --cli-unfold-argument  \
    --EndTime 2020-01-07T21:15:00+08:00 \
    --StartTime 2020-01-07T21:10:00+08:00
```

Output: 
```
{
    "Response": {
        "DataInfoList": [
            {
                "Bandwidth": 45927.6,
                "Time": "2020-05-01T00:00:00+08:00"
            },
            {
                "Bandwidth": 44494.84,
                "Time": "2020-05-01T00:05:00+08:00"
            },
            {
                "Bandwidth": 43061.09,
                "Time": "2020-05-01T00:10:00+08:00"
            }
        ],
        "RequestId": "f54e3deb-f318-4148-8a68-3c959642f9ec"
    }
}
```

