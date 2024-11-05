**Example 1: 资产查询**



Input: 

```
tccli csip DescribePublicIpAssets --cli-unfold-argument  \
    --Filter.Filters.0.Name CFWStatus \
    --Filter.Filters.0.Values 1 \
    --Filter.Filters.0.OperatorType 7 \
    --Filter.Filters.1.Name TimeRange \
    --Filter.Filters.1.Values 2 \
    --Filter.Filters.1.OperatorType 7 \
    --Filter.Limit 10 \
    --Filter.Offset 20 \
    --Filter.Order desc \
    --Filter.By AssetCreateTime \
    --MemberId mem-62509c52c13c9201
```

Output: 
```
{
    "Response": {
        "AppIdList": [
            {
                "Text": "1302396212401",
                "Value": "1302396212401"
            }
        ],
        "AssetLocationList": [
            {
                "Text": "腾讯云",
                "Value": "1"
            },
            {
                "Text": "其他",
                "Value": "2"
            }
        ],
        "AssetTypeList": [
            {
                "Text": "非腾讯云主机",
                "Value": "OTHER"
            },
            {
                "Text": "CVM",
                "Value": "CVM"
            },
            {
                "Text": "HAVIP",
                "Value": "HAVIP"
            },
            {
                "Text": "CLB",
                "Value": "CLB"
            },
            {
                "Text": "未知",
                "Value": "unknown"
            }
        ],
        "Data": [
            {
                "AssetId": "ins-mlyxc7ds",
                "AssetName": "cluster-node-10.26",
                "PublicIp": "106.52.96.220",
                "PublicIpType": 1,
                "Region": "ap-guangzhou",
                "AssetType": "CVM",
                "InBandwidth": "0bps",
                "OutBandwidth": "0bps",
                "InFlow": "0B",
                "OutFlow": "0B",
                "Access": 0,
                "Attack": 0,
                "PortRisk": 0,
                "VulnerabilityRisk": 2,
                "WeakPassword": 0,
                "WebContentRisk": 0,
                "RiskExposure": 0,
                "CFWStatus": 1,
                "AssetCreateTime": "2023-10-26 15:56:48",
                "VpcId": "vpc-ommo5hlv",
                "VpcName": "Default-VPC",
                "AppId": 1302396212401,
                "Uin": "10001459211278",
                "NickName": "生生乌龙",
                "IsCore": 2,
                "IsCloud": 1,
                "Intercept": 0,
                "LastScanTime": "2024-10-30 05:02:29",
                "ConfigurationRisk": 3,
                "ScanTask": 31,
                "Tag": [
                    {
                        "Name": "name1",
                        "Value": "value1"
                    }
                ],
                "AddressId": "eip-26c8hjt6",
                "MemberId": "mem-625c522c0913c901",
                "IsNewAsset": 0,
                "VerifyStatus": 0
            },
            {
                "AssetId": "asset-k2vqoh1",
                "AssetName": "asset-k2vqoh1",
                "PublicIp": "43.138.240.106",
                "PublicIpType": 0,
                "Region": "other",
                "AssetType": "未知",
                "InBandwidth": "0bps",
                "OutBandwidth": "0bps",
                "InFlow": "0B",
                "OutFlow": "0B",
                "Access": 0,
                "Attack": 0,
                "PortRisk": 0,
                "VulnerabilityRisk": 0,
                "WeakPassword": 0,
                "WebContentRisk": 0,
                "RiskExposure": 0,
                "CFWStatus": 1,
                "AssetCreateTime": "2023-10-11 17:23:31",
                "VpcId": "asset-k2vqoh1",
                "VpcName": "asset-k2vqoh1",
                "AppId": 1302396212401,
                "Uin": "10001459211278",
                "NickName": "生生乌龙",
                "IsCore": 2,
                "IsCloud": 2,
                "Intercept": 0,
                "LastScanTime": "2024-10-30 05:02:29",
                "ConfigurationRisk": 0,
                "ScanTask": 31,
                "Tag": [
                    {
                        "Name": "name1",
                        "Value": "value1"
                    }
                ],
                "AddressId": "asset-k2vqoh1",
                "MemberId": "mem-625c522c0913c901",
                "IsNewAsset": 0,
                "VerifyStatus": 0
            },
            {
                "AssetId": "asset-k2vqoh1",
                "AssetName": "asset-k2vqoh1",
                "PublicIp": "39.108.14.10",
                "PublicIpType": 0,
                "Region": "other",
                "AssetType": "未知",
                "InBandwidth": "0bps",
                "OutBandwidth": "0bps",
                "InFlow": "0B",
                "OutFlow": "0B",
                "Access": 0,
                "Attack": 0,
                "PortRisk": 0,
                "VulnerabilityRisk": 0,
                "WeakPassword": 0,
                "WebContentRisk": 0,
                "RiskExposure": 0,
                "CFWStatus": 1,
                "AssetCreateTime": "2023-09-06 11:03:28",
                "VpcId": "asset-k2vqoh1",
                "VpcName": "asset-k2vqoh1",
                "AppId": 1302396212401,
                "Uin": "10001459211278",
                "NickName": "生生乌龙",
                "IsCore": 2,
                "IsCloud": 3,
                "Intercept": 0,
                "LastScanTime": "2024-10-30 05:02:29",
                "ConfigurationRisk": 0,
                "ScanTask": 0,
                "Tag": [
                    {
                        "Name": "name1",
                        "Value": "value1"
                    }
                ],
                "AddressId": "asset-k2vqoh1",
                "MemberId": "mem-625c522c0913c901",
                "IsNewAsset": 0,
                "VerifyStatus": 0
            },
            {
                "AssetId": "havip-8h56wnzs",
                "AssetName": "NAT安全网关HaVip_请勿删改",
                "PublicIp": "114.132.124.142",
                "PublicIpType": 2,
                "Region": "ap-guangzhou",
                "AssetType": "HAVIP",
                "InBandwidth": "0bps",
                "OutBandwidth": "0bps",
                "InFlow": "0B",
                "OutFlow": "0B",
                "Access": 0,
                "Attack": 0,
                "PortRisk": 0,
                "VulnerabilityRisk": 0,
                "WeakPassword": 0,
                "WebContentRisk": 0,
                "RiskExposure": 0,
                "CFWStatus": 1,
                "AssetCreateTime": "2023-06-02 10:16:33",
                "VpcId": "asset-k2vqoh1",
                "VpcName": "asset-k2vqoh1",
                "AppId": 1302396212401,
                "Uin": "10001459211278",
                "NickName": "生生乌龙",
                "IsCore": 1,
                "IsCloud": 1,
                "Intercept": 0,
                "LastScanTime": "2024-10-30 05:02:29",
                "ConfigurationRisk": 0,
                "ScanTask": 35,
                "Tag": [
                    {
                        "Name": "name1",
                        "Value": "value1"
                    }
                ],
                "AddressId": "eip-egkkeona",
                "MemberId": "mem-625c522c0913c901",
                "IsNewAsset": 0,
                "VerifyStatus": 0
            }
        ],
        "DefenseStatusList": [
            {
                "Text": "未防护",
                "Value": "1"
            }
        ],
        "IpTypeList": [
            {
                "Text": "公网IP",
                "Value": "1"
            },
            {
                "Text": "弹性IP",
                "Value": "2"
            },
            {
                "Text": "未知",
                "Value": "0"
            }
        ],
        "RegionList": [
            {
                "Text": "广州",
                "Value": "ap-guangzhou"
            },
            {
                "Text": "成都",
                "Value": "ap-chengdu"
            },
            {
                "Text": "上海",
                "Value": "ap-shanghai"
            },
            {
                "Text": "未知",
                "Value": "other"
            },
            {
                "Text": "硅谷",
                "Value": "na-siliconvalley"
            }
        ],
        "RequestId": "27eb54eb-f654-4bae-bcce-278568d140bb",
        "Total": 4
    }
}
```

