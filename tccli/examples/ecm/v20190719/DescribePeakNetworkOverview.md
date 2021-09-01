**Example 1: 获取网络峰值数据**

获取网络峰值数据

Input: 

```
tccli ecm DescribePeakNetworkOverview --cli-unfold-argument  \
    --StartTime 2020-09-04 \
    --EndTime 2020-09-04 \
    --Filters.0.Name region \
    --Filters.0.Values ap-zhengzhou-ecm
```

Output: 
```
{
    "Response": {
        "RequestId": "ee2849f2-facd-4f84-a0ab-bec49edda5fc",
        "PeakNetworkRegionSet": [
            {
                "PeakNetworkSet": [
                    {
                        "PeakInNetwork": "31467.2",
                        "RecordTime": "2020-09-04 00:00:00",
                        "PeakOutNetwork": "32461.6"
                    },
                    {
                        "PeakInNetwork": "25255.2",
                        "RecordTime": "2020-09-04 00:05:00",
                        "PeakOutNetwork": "31626.4"
                    },
                    {
                        "PeakInNetwork": "24559.2",
                        "RecordTime": "2020-09-04 00:10:00",
                        "PeakOutNetwork": "30908.0"
                    },
                    {
                        "PeakInNetwork": "24356.8",
                        "RecordTime": "2020-09-04 00:15:00",
                        "PeakOutNetwork": "31393.6"
                    },
                    {
                        "PeakInNetwork": "28112.0",
                        "RecordTime": "2020-09-04 00:20:00",
                        "PeakOutNetwork": "33372.0"
                    },
                    {
                        "PeakInNetwork": "28352.8",
                        "RecordTime": "2020-09-04 00:25:00",
                        "PeakOutNetwork": "32520.0"
                    },
                    {
                        "PeakInNetwork": "25950.4",
                        "RecordTime": "2020-09-04 00:30:00",
                        "PeakOutNetwork": "30731.2"
                    },
                    {
                        "PeakInNetwork": "29326.4",
                        "RecordTime": "2020-09-04 00:35:00",
                        "PeakOutNetwork": "39581.6"
                    },
                    {
                        "PeakInNetwork": "30898.4",
                        "RecordTime": "2020-09-04 00:40:00",
                        "PeakOutNetwork": "40880.8"
                    },
                    {
                        "PeakInNetwork": "30900.8",
                        "RecordTime": "2020-09-04 00:45:00",
                        "PeakOutNetwork": "35427.2"
                    },
                    {
                        "PeakInNetwork": "31771.2",
                        "RecordTime": "2020-09-04 00:50:00",
                        "PeakOutNetwork": "37540.0"
                    }
                ],
                "Region": "ap-zhengzhou-ecm"
            }
        ]
    }
}
```

