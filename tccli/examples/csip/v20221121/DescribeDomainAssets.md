**Example 1: 接口示例**

接口示例

Input: 

```
tccli csip DescribeDomainAssets --cli-unfold-argument  \
    --Filter.Filters.0.Name WAFStatus \
    --Filter.Filters.0.Values 1 \
    --Filter.Filters.0.OperatorType 7 \
    --Filter.Filters.1.Name TimeRange \
    --Filter.Filters.1.Values 2 \
    --Filter.Filters.1.OperatorType 7 \
    --Filter.Limit 10 \
    --Filter.Offset 0 \
    --Filter.Order desc \
    --Filter.By AssetCreateTime \
    --MemberId mem-62522c05c913c901
```

Output: 
```
{
    "Response": {
        "AssetLocationList": [
            {
                "Text": "其他",
                "Value": "2"
            }
        ],
        "Data": [
            {
                "AssetId": [
                    "book.szzucieva.com"
                ],
                "AssetName": [
                    "book.szzucieva.com"
                ],
                "SubDomain": "book.szzucieva.com",
                "SourceType": "未知",
                "BotAccessCount": 0,
                "BotCount": 0,
                "WebAttack": 0,
                "PortRisk": 0,
                "VulnerabilityRisk": 0,
                "WeakPassword": 0,
                "WebContentRisk": 0,
                "ServiceRisk": 0,
                "WAFStatus": 1,
                "AssetType": [
                    "未知"
                ],
                "AssetCreateTime": "2024-08-31 06:01:18",
                "Region": [
                    "other"
                ],
                "SeverIp": [
                    "**************"
                ],
                "AppId": 1302396219625,
                "Uin": "100014592145978",
                "NickName": "生生乌龙",
                "IsCore": 2,
                "IsCloud": 3,
                "Attack": 0,
                "Access": 0,
                "Intercept": 0,
                "InBandwidth": "0bps",
                "OutBandwidth": "0bps",
                "InFlow": "0B",
                "OutFlow": "0B",
                "LastScanTime": "2024-10-30 05:02:29",
                "ConfigurationRisk": 0,
                "ScanTask": 0,
                "Tag": [
                    {
                        "Name": "name1",
                        "Value": "value1"
                    }
                ],
                "MemberId": "mem-625c229153c9c001",
                "CCAttack": 0,
                "IsNewAsset": 0,
                "VerifyDomain": "verify.te.foo1.***.dxoyxy.top",
                "VerifyTXTRecord": "verify/cnkj1bn2k4n124n14n12",
                "VerifyStatus": 0
            },
            {
                "AssetId": [
                    "docker.dzoxyxy.top"
                ],
                "AssetName": [
                    "docker.dzoxyxy.top"
                ],
                "SubDomain": "docker.dzoxyxy.top",
                "SourceType": "未知",
                "BotAccessCount": 0,
                "BotCount": 0,
                "WebAttack": 0,
                "PortRisk": 0,
                "VulnerabilityRisk": 0,
                "WeakPassword": 0,
                "WebContentRisk": 0,
                "ServiceRisk": 0,
                "WAFStatus": 1,
                "AssetType": [],
                "AssetCreateTime": "2023-12-14 11:06:37",
                "Region": [
                    "other"
                ],
                "SeverIp": [
                    "43.165.126.15"
                ],
                "AppId": 1302396219625,
                "Uin": "100014592145978",
                "NickName": "生生乌龙",
                "IsCore": 2,
                "IsCloud": 2,
                "Attack": 0,
                "Access": 0,
                "Intercept": 0,
                "InBandwidth": "0bps",
                "OutBandwidth": "0bps",
                "InFlow": "0B",
                "OutFlow": "0B",
                "LastScanTime": "2024-10-30 05:02:29",
                "ConfigurationRisk": 0,
                "ScanTask": 31,
                "Tag": [
                    {
                        "Name": "name1",
                        "Value": "value1"
                    }
                ],
                "MemberId": "mem-625c229153c9c001",
                "CCAttack": 0,
                "IsNewAsset": 0,
                "VerifyDomain": "verify.te.foo3.***.dxoyxy.top",
                "VerifyTXTRecord": "verify/qnwofhqocnasonr31cv3ir414j21pj4p12j41u0921u",
                "VerifyStatus": 0
            },
            {
                "AssetId": [
                    "example.te.dxoyxy.top"
                ],
                "AssetName": [
                    "example.te.dxoyxy.top"
                ],
                "SubDomain": "example.te.dxoyxy.top",
                "SourceType": "未知",
                "BotAccessCount": 0,
                "BotCount": 0,
                "WebAttack": 0,
                "PortRisk": 0,
                "VulnerabilityRisk": 0,
                "WeakPassword": 0,
                "WebContentRisk": 0,
                "ServiceRisk": 0,
                "WAFStatus": 1,
                "AssetType": [],
                "AssetCreateTime": "2023-12-14 11:30:07",
                "Region": [
                    "other"
                ],
                "SeverIp": [
                    "43.137.128.53"
                ],
                "AppId": 1302396219625,
                "Uin": "100014592145978",
                "NickName": "生生乌龙",
                "IsCore": 2,
                "IsCloud": 2,
                "Attack": 0,
                "Access": 0,
                "Intercept": 0,
                "InBandwidth": "0bps",
                "OutBandwidth": "0bps",
                "InFlow": "0B",
                "OutFlow": "0B",
                "LastScanTime": "2024-10-30 05:02:29",
                "ConfigurationRisk": 0,
                "ScanTask": 31,
                "Tag": [
                    {
                        "Name": "name1",
                        "Value": "value1"
                    }
                ],
                "MemberId": "mem-625c229153c9c001",
                "CCAttack": 0,
                "IsNewAsset": 0,
                "VerifyDomain": "verify.te.foo.***.dxoyxy.top",
                "VerifyTXTRecord": "verify/qnwofhqoir414j21pj4p12j41u0921u",
                "VerifyStatus": 0
            }
        ],
        "DefenseStatusList": [
            {
                "Text": "已防护",
                "Value": "1"
            },
            {
                "Text": "未防护",
                "Value": "5"
            }
        ],
        "RegionList": [
            {
                "Text": "未知",
                "Value": "other"
            }
        ],
        "RequestId": "ddca49aa-8aaf-4525-b2ff-fdd6fe7d1d20",
        "SourceTypeList": [
            {
                "Text": "未知",
                "Value": "unknown"
            }
        ],
        "Total": 3
    }
}
```

