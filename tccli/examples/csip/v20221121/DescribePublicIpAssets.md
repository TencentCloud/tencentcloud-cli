**Example 1: 资产查询**



Input: 

```
tccli csip DescribePublicIpAssets --cli-unfold-argument  \
    --MemberId abc \
    --Filter.Limit 0 \
    --Filter.Offset 0 \
    --Filter.Order abc \
    --Filter.By abc \
    --Filter.Filters.0.Name abc \
    --Filter.Filters.0.Values abc \
    --Filter.Filters.0.OperatorType 0 \
    --Filter.StartTime abc \
    --Filter.EndTime abc \
    --Tags.0.TagKey abc \
    --Tags.0.TagValue abc
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "AssetId": "abc",
                "AssetName": "abc",
                "AssetType": "abc",
                "Region": "abc",
                "CFWStatus": 1,
                "AssetCreateTime": "abc",
                "PublicIp": "abc",
                "PublicIpType": 1,
                "VpcId": "abc",
                "VpcName": "abc",
                "AppId": 1,
                "Uin": "abc",
                "NickName": "abc",
                "IsCore": 1,
                "IsCloud": 1,
                "Attack": 1,
                "Access": 1,
                "Intercept": 1,
                "InBandwidth": "abc",
                "OutBandwidth": "abc",
                "InFlow": "abc",
                "OutFlow": "abc",
                "LastScanTime": "abc",
                "PortRisk": 1,
                "VulnerabilityRisk": 1,
                "ConfigurationRisk": 1,
                "ScanTask": 1,
                "WeakPassword": 1,
                "WebContentRisk": 1,
                "Tag": [
                    {
                        "Name": "abc",
                        "Value": "abc"
                    }
                ],
                "AddressId": "abc",
                "MemberId": "abc",
                "RiskExposure": 0,
                "IsNewAsset": 1,
                "VerifyStatus": 0
            }
        ],
        "Total": 1,
        "AssetLocationList": [
            {
                "Value": "abc",
                "Text": "abc"
            }
        ],
        "IpTypeList": [
            {
                "Value": "abc",
                "Text": "abc"
            }
        ],
        "RegionList": [
            {
                "Value": "abc",
                "Text": "abc"
            }
        ],
        "AppIdList": [
            {
                "Value": "abc",
                "Text": "abc"
            }
        ],
        "DefenseStatusList": [
            {
                "Value": "abc",
                "Text": "abc"
            }
        ],
        "AssetTypeList": [
            {
                "Value": "abc",
                "Text": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

