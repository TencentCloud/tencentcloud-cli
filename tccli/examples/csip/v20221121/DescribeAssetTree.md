**Example 1: 资产树**



Input: 

```
tccli csip DescribeAssetTree --cli-unfold-argument  \
    --MemberId mem-0acb1****9a*d***
```

Output: 
```
{
    "Response": {
        "AssetTree": [
            {
                "Categories": [
                    {
                        "AssetTypes": [
                            {
                                "AssetCount": 1,
                                "AssetType": "node",
                                "AssetTypeID": 120,
                                "AssetTypeName": "集群节点"
                            }
                        ],
                        "Category": "容器",
                        "DisplayOrder": 2
                    }
                ],
                "Provider": "other",
                "ProviderName": "其他环境"
            }
        ],
        "RequestId": "daa434fc-22d3-41fa-88d8-a5220b444b21"
    }
}
```

