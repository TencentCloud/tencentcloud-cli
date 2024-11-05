**Example 1: 示例**

示例

Input: 

```
tccli csip DescribeGatewayAssets --cli-unfold-argument  \
    --MemberId mem-68b8087a65268000 mem-tencent-522badef8ad96a4d
```

Output: 
```
{
    "Response": {
        "AppIdList": [
            {
                "Text": "1827324",
                "Value": "1827324"
            },
            {
                "Text": "1302396215",
                "Value": "1302396215"
            }
        ],
        "AssetTypeList": [
            {
                "Text": "NATFW",
                "Value": "NATFW"
            },
            {
                "Text": "NAT",
                "Value": "NAT"
            },
            {
                "Text": "PROBE",
                "Value": "PROBE"
            },
            {
                "Text": "CLB",
                "Value": "CLB"
            }
        ],
        "Data": [
            {
                "AddressIPV6": "27::1",
                "AppId": "1827324",
                "AssetId": "cfwnat-a2b9957b",
                "AssetName": "autoDev",
                "AssetType": "NATFW",
                "ConfigureRisk": 0,
                "CreateTime": "2022-11-28 01:30:55",
                "EngineRegion": "sg",
                "ExposedPort": 0,
                "ExposedVUL": 0,
                "InboundCumulativeFlow": "352.00KB",
                "InboundPeakBandwidth": "1.75Kbps",
                "IsCore": 1,
                "IsNewAsset": 0,
                "LastScanTime": "2024-08-22 21:45:10",
                "NetworkAttack": 0,
                "Nick": "master",
                "OutboundCumulativeFlow": "38.67KB",
                "OutboundPeakBandwidth": "272.00bps",
                "PrivateIp": "172.0.12.3",
                "PublicIp": "1.**.***.59",
                "Region": "ap-shanghai",
                "RiskExposure": 0,
                "ScanTask": 0,
                "Status": "1",
                "Tag": [
                    {
                        "Name": "name1",
                        "Value": "value1"
                    }
                ],
                "Uin": "18146",
                "VpcId": "vpc-omoo5lv",
                "VpcName": "vpc-omoo5lv"
            }
        ],
        "RegionList": [
            {
                "Text": "上海",
                "Value": "ap-shanghai"
            },
            {
                "Text": "北京",
                "Value": "ap-beijing"
            },
            {
                "Text": "广州",
                "Value": "ap-guangzhou"
            }
        ],
        "RequestId": "7cf2ba3d-87ad-4691-a374-fd92ec11d9c8",
        "TotalCount": 6,
        "VpcList": [
            {
                "Text": "fengqqian3",
                "Value": "vpc-m819242"
            },
            {
                "Text": "fengqqian2",
                "Value": "vpc-fw2dus5f"
            },
            {
                "Text": "Default-VPC",
                "Value": "vpc-omoo5lv"
            }
        ]
    }
}
```

