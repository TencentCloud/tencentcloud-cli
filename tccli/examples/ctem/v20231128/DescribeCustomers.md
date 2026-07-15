**Example 1: 获取企业列表**



Input: 

```
tccli ctem DescribeCustomers --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "List": [
            {
                "AppId": 251257443,
                "AuthEndAt": "",
                "AuthFile": "",
                "AuthStartAt": "",
                "CreateAt": "2026-07-15 17:41:28",
                "Creator": "308000004436",
                "EnableAuth": false,
                "EnableCron": false,
                "EnableGroupMemberDiscovered": false,
                "EnableScanSubEnterprise": false,
                "Icon": "",
                "Id": 102188,
                "IsIncludeFullScan": false,
                "Keywords": "",
                "Name": "Mock Company 1",
                "Percent": 100,
                "PortScanQps": 100,
                "Qps": 50,
                "ScanCron": "",
                "ScanPriority": {
                    "OnlyScanNewAsset": true,
                    "PriorityRules": [
                        "new_asset"
                    ]
                },
                "ScanTime": "{\"Monday\":{\"0\":false,\"1\":false,\"10\":false,\"11\":false,\"12\":false,\"13\":false,\"14\":false,\"15\":false,\"16\":false,\"17\":false,\"18\":false,\"19\":false,\"2\":false,\"20\":false,\"21\":false,\"22\":false,\"23\":false,\"3\":false,\"4\":false,\"5\":false,\"6\":false,\"7\":false,\"8\":false,\"9\":false},\"Tuesday\":{\"0\":false,\"1\":false,\"10\":false,\"11\":false,\"12\":false,\"13\":false,\"14\":false,\"15\":false,\"16\":false,\"17\":false,\"18\":false,\"19\":false,\"2\":false,\"20\":false,\"21\":false,\"22\":false,\"23\":false,\"3\":false,\"4\":false,\"5\":false,\"6\":false,\"7\":false,\"8\":false,\"9\":false},\"Wednesday\":{\"0\":false,\"1\":false,\"10\":false,\"11\":false,\"12\":false,\"13\":false,\"14\":false,\"15\":false,\"16\":false,\"17\":false,\"18\":false,\"19\":false,\"2\":false,\"20\":false,\"21\":false,\"22\":false,\"23\":false,\"3\":false,\"4\":false,\"5\":false,\"6\":false,\"7\":false,\"8\":false,\"9\":false},\"Thursday\":{\"0\":false,\"1\":false,\"10\":false,\"11\":false,\"12\":false,\"13\":false,\"14\":false,\"15\":false,\"16\":false,\"17\":false,\"18\":false,\"19\":false,\"2\":false,\"20\":false,\"21\":false,\"22\":false,\"23\":false,\"3\":false,\"4\":false,\"5\":false,\"6\":false,\"7\":false,\"8\":false,\"9\":false},\"Friday\":{\"0\":false,\"1\":false,\"10\":false,\"11\":false,\"12\":false,\"13\":false,\"14\":false,\"15\":false,\"16\":false,\"17\":false,\"18\":false,\"19\":false,\"2\":false,\"20\":false,\"21\":false,\"22\":false,\"23\":false,\"3\":false,\"4\":false,\"5\":false,\"6\":false,\"7\":false,\"8\":false,\"9\":false},\"Saturday\":{\"0\":false,\"1\":false,\"10\":false,\"11\":false,\"12\":false,\"13\":false,\"14\":false,\"15\":false,\"16\":false,\"17\":false,\"18\":false,\"19\":false,\"2\":false,\"20\":false,\"21\":false,\"22\":false,\"23\":false,\"3\":false,\"4\":false,\"5\":false,\"6\":false,\"7\":false,\"8\":false,\"9\":false},\"Sunday\":{\"0\":false,\"1\":false,\"10\":false,\"11\":false,\"12\":false,\"13\":false,\"14\":false,\"15\":false,\"16\":false,\"17\":false,\"18\":false,\"19\":false,\"2\":false,\"20\":false,\"21\":false,\"22\":false,\"23\":false,\"3\":false,\"4\":false,\"5\":false,\"6\":false,\"7\":false,\"8\":false,\"9\":false}}",
                "ScanType": "资产收集",
                "SingleIPTaskLimit": 1,
                "SubCompanyLevel": -1,
                "Uin": "700001041233",
                "UpdateAt": "2026-07-15 17:41:28"
            }
        ],
        "Total": 570,
        "RequestId": "66f90810-be75-48cf-9238-9a183e9d3b3d"
    }
}
```

