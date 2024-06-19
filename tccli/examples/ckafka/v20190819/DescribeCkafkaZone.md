**Example 1: 查看可用区列表**



Input: 

```
tccli ckafka DescribeCkafkaZone --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Result": {
            "ZoneList": [
                {
                    "ZoneId": "abc",
                    "IsInternalApp": 0,
                    "AppId": 0,
                    "Flag": true,
                    "ZoneName": "abc",
                    "ZoneStatus": 0,
                    "Exflag": "abc",
                    "SoldOut": "abc",
                    "SalesInfo": [
                        {
                            "Flag": true,
                            "Version": "abc",
                            "Platform": "abc",
                            "SoldOut": true
                        }
                    ],
                    "ExtraFlag": "abc"
                }
            ],
            "MaxBuyInstanceNum": 0,
            "MaxBandwidth": 0,
            "UnitPrice": {
                "RealTotalCost": 0,
                "TotalCost": 0
            },
            "MessagePrice": {
                "RealTotalCost": 0,
                "TotalCost": 0
            },
            "ClusterInfo": [
                {
                    "ClusterId": 0,
                    "ClusterName": "abc",
                    "MaxDiskSize": 0,
                    "MaxBandWidth": 0,
                    "AvailableDiskSize": 0,
                    "AvailableBandWidth": 0,
                    "ZoneId": 0,
                    "ZoneIds": [
                        0
                    ]
                }
            ],
            "Standard": "abc",
            "StandardS2": "abc",
            "Profession": "abc",
            "Physical": "abc",
            "PublicNetwork": "abc",
            "PublicNetworkLimit": "abc",
            "RequestId": "abc",
            "Version": "abc",
            "Offset": 0,
            "Limit": 0,
            "ForceCheckTag": true
        },
        "RequestId": "abc"
    }
}
```

