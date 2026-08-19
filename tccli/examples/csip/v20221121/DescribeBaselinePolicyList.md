**Example 1: 获取系统策略列表**

获取系统策略列表

Input: 

```
tccli csip DescribeBaselinePolicyList --cli-unfold-argument  \
    --PolicyType SYSTEM \
    --MemberId mem-tencent-6*************29 \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "Appid": 200000000,
                "AutoSyncItem": true,
                "CategoryConf": [
                    {
                        "AllSelect": true,
                        "CategoryID": 100000000,
                        "SubCategoryConfList": [
                            {
                                "AllSelect": true,
                                "CategoryID": 100000001,
                                "ItemIDList": []
                            }
                        ]
                    }
                ],
                "CheckAssetType": "CLUSTER",
                "CloudTagList": [],
                "ConfClusterCount": 0,
                "ConfClusterExcludeList": [],
                "ConfClusterIncludeList": [],
                "ConfClusterType": "ALL",
                "ConfHostCount": 0,
                "ConfHostExcludeList": [],
                "ConfHostIncludeList": [],
                "ConfHostType": "ALL",
                "ConfItemCount": 12,
                "CustomItemConf": [],
                "CycleScanConf": {
                    "Enable": 0,
                    "IntervalType": "",
                    "IntervalValueList": [],
                    "ScanEnd": "",
                    "ScanStart": ""
                },
                "Description": "集群安全检测",
                "Enable": true,
                "ID": 182,
                "LatestCycleScanTime": "1970-01-01T00:00:00Z",
                "LatestScanTime": "1970-01-01T00:00:00Z",
                "Name": "集群安全检测",
                "ScanningTaskID": 0,
                "TagIDList": [],
                "Type": "SYSTEM"
            }
        ],
        "TotalCount": 19,
        "RequestId": "e20d1938-ab97-4af4-ab0f-f785d3e56193"
    }
}
```

