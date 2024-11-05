**Example 1: 获取网卡列表**

获取网卡列表

Input: 

```
tccli csip DescribeNICAssets --cli-unfold-argument  \
    --MemberId mem-688033 mem-tencent-52d96a4d \
    --Filter.Limit 1
```

Output: 
```
{
    "Response": {
        "AppIdList": [
            {
                "Text": "2421",
                "Value": "2421"
            },
            {
                "Text": "1894",
                "Value": "1894"
            }
        ],
        "AssetTypeList": [
            {
                "Text": "ENI",
                "Value": "ENI"
            }
        ],
        "Data": [
            {
                "AppId": "15651",
                "AssetId": "eni-45xmwr0j",
                "AssetName": "未命名",
                "AssetType": "ENI",
                "ConfigureRisk": 0,
                "CreateTime": "2023-11-23 19:58:39",
                "ExposedPort": 0,
                "ExposedVUL": 0,
                "InboundCumulativeFlow": "0B",
                "InboundPeakBandwidth": "0bps",
                "IsCore": 1,
                "IsNewAsset": 0,
                "LastScanTime": "2024-10-12 16:33:37",
                "NetworkAttack": 0,
                "Nick": "焦糖小蛋糕",
                "OutboundCumulativeFlow": "0B",
                "OutboundPeakBandwidth": "0bps",
                "PrivateIp": "172.16.0.6",
                "PublicIp": "1.1.1.1",
                "Region": "ap-guangzhou",
                "ScanTask": 8,
                "Tag": null,
                "Uin": "10446",
                "VpcId": "vpc-hbe549z5",
                "VpcName": "league-vpc-2"
            }
        ],
        "RegionList": [
            {
                "Text": "广州",
                "Value": "ap-guangzhou"
            },
            {
                "Text": "南京",
                "Value": "ap-nanjing"
            },
            {
                "Text": "上海",
                "Value": "ap-shanghai"
            }
        ],
        "RequestId": "00369b23-b4da-446f-8d07-7ee691d237a4",
        "TotalCount": 7,
        "VpcList": [
            {
                "Text": "league-vpc-2",
                "Value": "vpc-hdbed9z5"
            },
            {
                "Text": "vpc-gz-0",
                "Value": "vpc-63z25m89"
            }
        ]
    }
}
```

