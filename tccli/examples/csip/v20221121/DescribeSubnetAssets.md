**Example 1: 获取子网列表**

获取子网列表

Input: 

```
tccli csip DescribeSubnetAssets --cli-unfold-argument  \
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
                "Text": "1827324",
                "Value": "1827324"
            }
        ],
        "Data": [
            {
                "AppId": "1827324",
                "AssetId": "subnet-0pptyoj8",
                "AssetName": "sub2",
                "AvailableIp": 253,
                "CIDR": "192.168.25.0/24",
                "CVM": 0,
                "ConfigureRisk": 1,
                "CreateTime": "2024-06-12 18:01:54",
                "IsCore": 2,
                "IsNewAsset": 0,
                "LastScanTime": "2024-10-30 11:16:07",
                "Nick": "yooyan",
                "Region": "ap-guangzhou",
                "ScanTask": 193,
                "Tag": null,
                "Uin": "100014592178",
                "VpcId": "vpc-9eoyt5v",
                "VpcName": "feoyian2",
                "Zone": "ap-guangzhou-6"
            }
        ],
        "RegionList": [
            {
                "Text": "广州",
                "Value": "ap-guangzhou"
            }
        ],
        "RequestId": "0604124a-7416-408c-9c70-793880a82005",
        "TotalCount": 54,
        "VpcList": [
            {
                "Text": "vpc_c2",
                "Value": "vpc-2toy3vhb"
            },
            {
                "Text": "vpc-gz-0",
                "Value": "vpc-68toym89"
            }
        ],
        "ZoneList": [
            {
                "Text": "广州六区",
                "Value": "ap-guangzhou-6"
            },
            {
                "Text": "广州三区",
                "Value": "ap-guangzhou-3"
            }
        ]
    }
}
```

