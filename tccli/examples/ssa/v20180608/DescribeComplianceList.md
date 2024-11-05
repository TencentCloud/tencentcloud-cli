**Example 1: 合规管理总览页检查项列表**



Input: 

```
tccli ssa DescribeComplianceList --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "Category": "1",
                "AssetType": "2",
                "AssetTotal": 0,
                "Name": "name",
                "LastCheckTime": "2020-09-22 00:00:00",
                "IsIgnored": 1,
                "Title": "title",
                "CheckItemId": "1",
                "StandardItem": "2",
                "Status": 1,
                "IsChecked": 1,
                "RiskItem": "2",
                "Remarks": "remark",
                "RiskCount": 1,
                "Type": "1",
                "Id": "1",
                "Chapter": "chapter"
            }
        ],
        "AssetTotalNum": 1,
        "ConfigTotalNum": 1,
        "RequestId": "cf8c69d7-0718-4a3e-a47e-450161359d50"
    }
}
```

