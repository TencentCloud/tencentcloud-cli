**Example 1: 云边界自动打标规则属性**



Input: 

```
tccli csip DescribeExposureAutoTagAttribute --cli-unfold-argument  \
    --MemberId mem-0000
```

Output: 
```
{
    "Response": {
        "AssetTypeList": [
            {
                "AssetType": "cvm_instance",
                "AssetTypeName": "云服务器",
                "Provider": "tencent",
                "ProviderName": "腾讯云"
            }
        ],
        "OpenStatusList": [
            {
                "Text": "完全开放",
                "Value": "open"
            }
        ],
        "TagList": [
            {
                "Text": "合理业务",
                "Value": "legit_business"
            }
        ],
        "RequestId": "1a255788-5756-4782-b97e-faeaf94c5839"
    }
}
```

