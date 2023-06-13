**Example 1: 域名列表**

域名列表

Input: 

```
tccli ssa DescribeDomainList --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Total": 1,
        "DomainInfoCollection": [
            {
                "Domain": "abc",
                "ResolveAddr": [
                    "abc"
                ],
                "Region": [
                    "abc"
                ],
                "AssetType": [
                    "abc"
                ],
                "RiskVulCount": 1,
                "SensitiveCount": 1,
                "HorseLinkCount": 1,
                "WebModifyCount": 1,
                "ScanTime": "abc",
                "DiscoverTime": "abc",
                "ScanTaskCount": 1,
                "PortRisk": 1,
                "WeekPwdCount": 1,
                "AssetLocation": "abc",
                "NetworkRisk": 1,
                "NetworkAttack": 1,
                "BotVisit": 1,
                "NetworkAccess": 1,
                "CreateTime": "abc",
                "WafStatus": 1,
                "LastScanTime": "abc",
                "AssetId": [
                    "abc"
                ],
                "AssetName": [
                    "abc"
                ],
                "SourceType": "abc",
                "IsNotCore": 1,
                "IsCloud": 1
            }
        ],
        "RequestId": "abc"
    }
}
```

