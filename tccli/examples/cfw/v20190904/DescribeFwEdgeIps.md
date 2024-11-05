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
                "PublicIp": "43.138.181.57",
                "PublicIpType": 2,
                "InstanceId": "havip-berhzoxi",
                "InstanceName": "防火墙专用_请勿删改",
                "IntranetIp": "172.16.1.1",
                "AssetType": "HAVIP",
                "Region": "ap-guangzhou",
                "PortRiskCount": -1,
                "LastScanTime": "2022-07-27 16:00:00",
                "SwitchMode": 0,
                "IsRegionEip": 1,
                "VpcId": "vpc-wxecrvtb",
                "IsSerialRegion": 2,
                "EndpointId": "vpce-wxecrvtb",
                "EndpointIp": "172.16.1.1",
                "IsPublicClb": 0,
                "EndpointBindEipNum": 0,
                "ScanMode": "medium",
                "ScanStatus": 0,
                "Status": 1,
                "SwitchWeight": 1,
                "Domain": "*****",
                "OverUsedStatus": 0
            }
        ],
        "Total": 10,
        "RegionLst": [
            "ap-beijing"
        ],
        "InstanceTypeLst": [
            "nat",
            "cvm"
        ],
        "RequestId": "0752de63-570c-4c2e-bbd2-78574e22a1ae"
    }
}
```

