**Example 1: 合规管理总览页检查项列表**



Input: 

```
tccli ssa DescribeComplianceList --cli-unfold-argument  \
    --Filter test
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "Category": "xx",
                "AssetType": "xx",
                "AssetTotal": 0,
                "Name": "xx",
                "LastCheckTime": "2020-09-22 00:00:00",
                "IsIgnored": 1,
                "Title": "xx",
                "CheckItemId": "xx",
                "StandardItem": "xx",
                "Status": 1,
                "IsChecked": 1,
                "RiskItem": "xx",
                "Remarks": "xx",
                "RiskCount": 1,
                "Type": "xx",
                "Id": "xx",
                "Chapter": "xx"
            }
        ],
        "AssetTotalNum": 1,
        "ConfigTotalNum": 1,
        "RequestId": "cf8c69d7-0718-4a3e-a47e-450161359d50"
    }
}
```

