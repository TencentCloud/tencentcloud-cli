**Example 1: 获取转发报表数据**



Input: 

```
tccli dayu DescribeBaradData --cli-unfold-argument  \
    --Business bgpip \
    --Id bgpip-000000x7 \
    --Period 300 \
    --StartTime '2018-08-28 07:15:00' \
    --EndTime '2018-08-28 10:05:00' \
    --Statistics max \
    --MetricName connum \
    --ProtocolPort.0.Protocol tcp \
    --ProtocolPort.0.Port 80
```

Output: 
```
{
    "Response": {
        "DataList": [
            {
                "MetricName": "connum",
                "Data": [
                    236,
                    236,
                    236,
                    236,
                    236,
                    236,
                    236,
                    236,
                    236,
                    236,
                    236,
                    236,
                    236,
                    236,
                    236,
                    236,
                    236,
                    236,
                    236,
                    236,
                    236,
                    236,
                    236,
                    236,
                    236,
                    236,
                    236,
                    236,
                    236,
                    236,
                    236,
                    236,
                    236,
                    236,
                    236
                ],
                "Count": 35
            },
            {
                "MetricName": "new_conn",
                "Data": [
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0
                ],
                "Count": 35
            }
        ],
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

