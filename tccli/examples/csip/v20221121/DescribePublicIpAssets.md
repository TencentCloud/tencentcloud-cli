**Example 1: 接口示例**

接口示例

Input: 

```
tccli csip DescribePublicIpAssets --cli-unfold-argument  \
    --Filter.Limit 0 \
    --Filter.Offset 0 \
    --Filter.Order  \
    --Filter.By  \
    --Filter.Filters.0.Name  \
    --Filter.Filters.0.Values  \
    --Filter.Filters.0.OperatorType 0 \
    --Filter.StartTime  \
    --Filter.EndTime 
```

Output: 
```
{
    "Response": {
        "AppIdList": [
            {
                "Text": "1251001047",
                "Value": "1251001047"
            }
        ],
        "AssetLocationList": [
            {
                "Text": "其他",
                "Value": "2"
            }
        ],
        "AssetTypeList": [],
        "Data": [
            {
                "AssetId": "",
                "AddressId": "",
                "AssetName": "",
                "AssetType": "",
                "Region": "other",
                "AssetCreateTime": "2023-01-10 17:02:50",
                "PublicIp": "103.150.141.100",
                "PublicIpType": 0,
                "VpcId": "",
                "VpcName": "",
                "AppId": 1251001047,
                "Uin": "",
                "NickName": "",
                "IsCore": 1,
                "IsCloud": 2,
                "Attack": 0,
                "Access": 0,
                "Intercept": 0,
                "InBandwidth": "0.00bps",
                "OutBandwidth": "0.00bps",
                "InFlow": "0.00B",
                "OutFlow": "0.00B",
                "LastScanTime": "-",
                "PortRisk": 0,
                "VulnerabilityRisk": 0,
                "ConfigurationRisk": 0,
                "ScanTask": 0,
                "WeakPassword": 0,
                "WebContentRisk": 0,
                "Tag": null,
                "CFWStatus": 1
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
                "Text": "未知",
                "Value": "0"
            }
        ],
        "RegionList": [
            {
                "Text": "其他",
                "Value": "other"
            }
        ],
        "RequestId": "c4b812a0-5814-4611-adec-6124bdd9b961",
        "Total": 9
    }
}
```

