**Example 1: 串行防火墙开关列表**

串行防火墙开关列表

Input: 

```
tccli cfw DescribeFwEdgeIps --cli-unfold-argument  \
    --Filters.0.Name PublicIp \
    --Filters.0.Values 1.1.1.1 \
    --Filters.0.OperatorType 9 \
    --Limit 10 \
    --Offset 0 \
    --StartTime 2022-07-27 16:00:00 \
    --EndTime 2022-07-27 16:00:00 \
    --Order desc \
    --By PublicIp
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "PublicIp": "2.2.2.2",
                "PublicIpType": 2,
                "InstanceId": "ins-xxxxxxxx",
                "InstanceName": "cvm实例1",
                "IntranetIp": "172.16.1.1",
                "AssetType": "cvm",
                "Region": "ap-chongqing",
                "PortRiskCount": 10,
                "LastScanTime": "2022-07-27 16:00:00",
                "SwitchMode": 2,
                "IsRegionEip": 1,
                "VpcId": "vpc-abcdabcd",
                "IsSerialRegion": 1,
                "IsPublicClb": 0,
                "EndpointBindEipNum": 1,
                "ScanMode": "medium",
                "ScanStatus": 0,
                "EndpointId": "vpce-xxxxxxxx",
                "EndpointIp": "10.10.10.10",
                "SwitchWeight": 100
            }
        ],
        "Total": 10,
        "RegionLst": [
            "abc"
        ],
        "InstanceTypeLst": [
            "nat",
            "cvm"
        ],
        "RequestId": "0752de63-570c-4c2e-bbd2-78574e22a1ae"
    }
}
```

