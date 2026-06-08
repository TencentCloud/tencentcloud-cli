**Example 1: 开关查询示例**



Input: 

```
tccli cfw DescribeClusterNatCcnFwSwitchList --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "AssetType": "nat",
                "AttachId": "",
                "AttachIns": null,
                "Bypass": 0,
                "Endpoints": null,
                "FwType": "nat",
                "InsObj": "nat-0ktoayqe",
                "IpVersion": 0,
                "IpsAction": 0,
                "NatVpcId": "",
                "NonCluster": 0,
                "ObjName": "NAT测试",
                "Region": "eu-frankfurt",
                "RoutingMode": 0,
                "Status": 0,
                "SwitchMode": 1,
                "TransEnable": 0
            }
        ],
        "RegionList": [
            {
                "Text": "法兰克福",
                "Value": "eu-frankfurt"
            }
        ],
        "Total": 8,
        "RequestId": "7b1b108b-271a-4b84-8eaf-e2e962144a9c"
    }
}
```

