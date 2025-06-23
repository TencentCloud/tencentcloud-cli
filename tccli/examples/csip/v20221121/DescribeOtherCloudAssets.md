**Example 1: 其他云资源列表**

其他云资源列表

Input: 

```
tccli csip DescribeOtherCloudAssets --cli-unfold-argument  \
    --Filter.Limit 0 \
    --Filter.Offset 0 \
    --Filter.Order abc \
    --Filter.By abc \
    --Filter.Filters.0.Name abc \
    --Filter.Filters.0.Values abc \
    --Filter.Filters.0.OperatorType 0 \
    --Filter.StartTime abc \
    --Filter.EndTime abc \
    --AssetTypes abc
```

Output: 
```
{
    "Response": {
        "Total": 1,
        "Data": [
            {
                "AssetId": "abc",
                "AssetName": "abc",
                "AssetType": "abc",
                "VpcId": "abc",
                "VpcName": "abc",
                "Region": "abc",
                "Domain": "abc",
                "AssetCreateTime": "abc",
                "LastScanTime": "abc",
                "ConfigurationRisk": 1,
                "Attack": 1,
                "Access": 1,
                "ScanTask": 1,
                "AppId": 1,
                "Uin": "abc",
                "NickName": "abc",
                "Port": 1,
                "Tag": [
                    {
                        "Name": "abc",
                        "Value": "abc"
                    }
                ],
                "PrivateIp": "abc",
                "PublicIp": "abc",
                "Status": 1,
                "IsCore": 1,
                "IsNewAsset": 1
            }
        ],
        "RegionList": [
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
        "VpcList": [
            {
                "Value": "abc",
                "Text": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

