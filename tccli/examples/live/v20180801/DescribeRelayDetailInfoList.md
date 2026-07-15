**Example 1: DescribeRelayDetailInfoList**

海外转推带宽查询

Input: 

```
tccli live DescribeRelayDetailInfoList --cli-unfold-argument  \
    --StartTime 2023-02-01T20:00:00Z \
    --EndTime 2023-02-01T20:00:00Z \
    --DomainNames  \
    --RegionName 
```

Output: 
```
{
    "Response": {
        "DataInfoList": [
            {
                "RegionNames": "",
                "PeakBandwidthTime": "",
                "PeakBandwidth": 0,
                "P95PeakBandwidthTime": "",
                "P95PeakBandwidth": 0,
                "RelayBillDataInfo": [
                    {
                        "Bandwidth": 0,
                        "Time": ""
                    }
                ]
            }
        ],
        "RequestId": ""
    }
}
```

