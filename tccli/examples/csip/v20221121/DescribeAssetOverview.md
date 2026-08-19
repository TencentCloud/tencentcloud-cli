**Example 1: 资产概览**



Input: 

```
tccli csip DescribeAssetOverview --cli-unfold-argument  \
    --MemberId mem-0acb*0f2f*****e*
```

Output: 
```
{
    "Response": {
        "AssetOverview": {
            "AlarmAssetCount": 0,
            "AssetAddCount": 0,
            "AssetTotalCount": 3024,
            "CloudHostAssetCount": 82,
            "ExposeAssetCount": 55,
            "PublicAssetCount": 56,
            "RiskAssetCount": 1
        },
        "AssetProviderDistribute": {
            "AliAssetCount": 0,
            "AwsAssetCount": 0,
            "OtherAssetCount": 1,
            "TencentAssetCount": 3023
        },
        "AssetTypeOverview": {
            "AssetTypeCount": 29,
            "RiskAssetTypeCount": 1
        },
        "RequestId": "b4d28580-8428-4125-b508-2b28596502a9"
    }
}
```

