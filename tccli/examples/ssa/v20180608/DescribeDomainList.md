**Example 1: 获取域名列表**

获取域名列表

Input: 

```
tccli ssa DescribeDomainList --cli-unfold-argument  \
    --Limit 10 \
    --Order desc \
    --By Domain
```

Output: 
```
{
    "Response": {
        "Total": 1,
        "DomainInfoCollection": [
            {
                "Domain": "excample.com",
                "ResolveAddr": [
                    "10.0.0.1"
                ],
                "Region": [
                    "ap-guangzhou"
                ],
                "AssetType": [
                    "cvm"
                ],
                "RiskVulCount": 1,
                "SensitiveCount": 1,
                "HorseLinkCount": 1,
                "WebModifyCount": 1,
                "ScanTime": "2020-10-10 12:12:12",
                "DiscoverTime": "2020-10-10 12:12:12",
                "ScanTaskCount": 1,
                "PortRisk": 1,
                "WeekPwdCount": 1,
                "AssetLocation": "guangzhou",
                "NetworkRisk": 1,
                "NetworkAttack": 1,
                "BotVisit": 1,
                "NetworkAccess": 1,
                "CreateTime": "2020-10-10 12:12:12",
                "WafStatus": 1,
                "LastScanTime": "2020-10-10 12:12:12",
                "AssetId": [
                    "1"
                ],
                "AssetName": [
                    "name"
                ],
                "SourceType": "1",
                "IsNotCore": 1,
                "IsCloud": 1
            }
        ],
        "RequestId": "f9184c15-9721-456d-8ca0-4263967b5ead"
    }
}
```

