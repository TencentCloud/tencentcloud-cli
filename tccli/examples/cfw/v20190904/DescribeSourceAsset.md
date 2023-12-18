**Example 1: 查询资产组全部资产信息**



Input: 

```
tccli cfw DescribeSourceAsset --cli-unfold-argument  \
    --FuzzySearch abc \
    --InsType abc \
    --ChooseType abc \
    --Zone abc \
    --Limit 0 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "ZoneList": [
            {
                "Zone": "abc",
                "ZoneEng": "abc"
            }
        ],
        "Data": [
            {
                "AppId": "abc",
                "Region": "abc",
                "VpcId": "abc",
                "VPCName": "abc",
                "SubnetId": "abc",
                "InstanceId": "abc",
                "InstanceName": "abc",
                "InsType": 0,
                "PublicIp": "abc",
                "PrivateIp": "abc",
                "PortNum": "abc",
                "LeakNum": "abc",
                "InsSource": "abc",
                "ResourcePath": [
                    "abc"
                ],
                "Server": [
                    "abc"
                ],
                "RegionKey": "abc"
            }
        ],
        "Total": 0,
        "RequestId": "abc"
    }
}
```

