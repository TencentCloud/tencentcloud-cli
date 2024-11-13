**Example 1: 查询站点详情**

查询站点详情

Input: 

```
tccli cdc DescribeSitesDetail --cli-unfold-argument  \
    --SiteIds site-98dj3kd
```

Output: 
```
{
    "Response": {
        "SiteDetailSet": [
            {
                "SiteId": "site-98dj3kd",
                "Name": "sitename",
                "Description": "this is a description",
                "CreateTime": "2020-12-25T08:39:57Z",
                "FiberType": "MM",
                "UplinkSpeedGbps": 0,
                "UplinkCount": 0,
                "OpticalStandard": "MM",
                "RedundantNetworking": false,
                "PowerConnectors": "1000Base-SX",
                "PowerFeedDrop": "above",
                "PowerDrawKva": 0.0,
                "ConditionRequirement": false,
                "DimensionRequirement": false,
                "NeedHelp": false,
                "BreakerRequirement": false,
                "RedundantPower": false,
                "MaxWeight": 0,
                "AddressLine": "Nanshan Road",
                "OptionalAddressLine": "详细地址",
                "Country": "China",
                "Province": "guangdong",
                "City": "shenzhen",
                "PostalCode": 518000
            }
        ],
        "TotalCount": 1,
        "RequestId": "a07a5f9c-277c-4f03-a338-c2863982b1a6"
    }
}
```

