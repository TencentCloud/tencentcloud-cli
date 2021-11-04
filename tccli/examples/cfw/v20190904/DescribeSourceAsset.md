**Example 1: 查询资产组全部资产信息**



Input: 

```
tccli cfw DescribeSourceAsset --cli-unfold-argument  \
    --InsType xx \
    --ChooseType xx \
    --FuzzySearch xx \
    --Zone xx
```

Output: 
```
{
    "Response": {
        "Total": 2,
        "Data": [
            {
                "LeakNum": "xx",
                "InsSource": "xx",
                "VpcId": "xx",
                "PortNum": "xx",
                "InstanceId": "xx",
                "Region": "xx",
                "ResourcePath": [
                    "xx"
                ],
                "PrivateIp": "xx",
                "PublicIp": "xx",
                "SubnetId": "xx",
                "VPCName": "xx",
                "AppId": "xx",
                "InsType": 0,
                "InstanceName": "xx"
            }
        ],
        "RequestId": "xx",
        "ZoneList": [
            {
                "ZoneEng": "xx",
                "Zone": "xx"
            }
        ]
    }
}
```

