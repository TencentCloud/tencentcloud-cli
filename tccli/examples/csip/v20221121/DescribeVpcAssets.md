**Example 1: 获取vpc列表**

获取vpc列表

Input: 

```
tccli csip DescribeVpcAssets --cli-unfold-argument  \
    --MemberId mem-68b8087a65268000 \
    --Filter.Limit 1 \
    --Filter.Offset 0
```

Output: 
```
{
    "Response": {
        "AppIdList": [
            {
                "Text": "1302111215",
                "Value": "1302111215"
            }
        ],
        "Data": [
            {
                "AppId": "1302111215",
                "AssetId": "vpc-1hezruby",
                "AssetName": "li-跨账号2",
                "CIDR": "172.16.0.0/16",
                "CVM": 3,
                "ConnectedVpc": 0,
                "CreateTime": "2024-08-27 10:22:36",
                "DNS": [
                    "183.**.**.19",
                    "183.**.**.98"
                ],
                "IsCore": 1,
                "IsNewAsset": 0,
                "Nick": "声声乌龙",
                "Region": "ap-beijing",
                "Subnet": 1,
                "Tag": null,
                "Uin": "100014125178"
            }
        ],
        "RegionList": [
            {
                "Text": "广州",
                "Value": "ap-guangzhou"
            },
            {
                "Text": "重庆",
                "Value": "ap-chongqing"
            }
        ],
        "RequestId": "25e46c79-08c5-4582-9952-eee1245bbbb2",
        "TotalCount": 35,
        "VpcList": [
            {
                "Text": "vpc_c8",
                "Value": "vpc-2pu5xuk1"
            },
            {
                "Text": "vpc_c2",
                "Value": "vpc-2t0l3vhb"
            }
        ]
    }
}
```

