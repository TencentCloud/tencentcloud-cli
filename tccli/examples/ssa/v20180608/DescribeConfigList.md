**Example 1: 云配置检查项总览页检查项列表**



Input: 

```
tccli ssa DescribeConfigList --cli-unfold-argument  \
    --Filter test
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "Id": "x",
                "Name": "name",
                "Type": "type",
                "LastCheckTime": "2020-12-12 12:12:00",
                "Status": 1,
                "IsIgnored": 0,
                "RiskCount": 100,
                "IsChecked": 1,
                "AssetTotal": 200,
                "Remarks": "xx"
            }
        ],
        "RequestId": "cf8c69d7-0718-4a3e-a47e-450161359d50"
    }
}
```

