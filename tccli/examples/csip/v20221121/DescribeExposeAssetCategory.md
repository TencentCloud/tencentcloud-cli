**Example 1: 暴露面资产分类**



Input: 

```
tccli csip DescribeExposeAssetCategory --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "ExposeAssetTypeList": [
            {
                "Provider": "tencent",
                "ProviderName": "腾讯云",
                "AssetType": "cvm_instance",
                "AssetTypeName": "云服务器"
            }
        ],
        "RequestId": "46fb51ad-b6d8-4c91-af47-8f4bc947a69c"
    }
}
```

