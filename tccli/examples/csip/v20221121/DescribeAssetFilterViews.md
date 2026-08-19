**Example 1: 资产搜索视图列表**



Input: 

```
tccli csip DescribeAssetFilterViews --cli-unfold-argument  \
    --MemberId mem-0acb10f2*9a*d*ee
```

Output: 
```
{
    "Response": {
        "FilterViews": [
            {
                "Filters": [
                    {
                        "ExactMatch": "",
                        "Name": "AssetType",
                        "Values": [
                            "dsds"
                        ]
                    }
                ],
                "ViewID": 6,
                "ViewName": "点点滴滴"
            }
        ],
        "RequestId": "676d9119-3f21-454d-b22e-e5b0fd1a01f6"
    }
}
```

