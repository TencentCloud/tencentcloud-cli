**Example 1: 调用示例**



Input: 

```
tccli csip DescribeBaselineItemRiskList --cli-unfold-argument  \
    --PolicyID 761 \
    --ParentCategoryID 4 \
    --ItemID 8 \
    --CheckAssetType HOST \
    --CategoryID 50 \
    --MemberId mem-tencent-6*************29 \
    --Limit 10 \
    --Offset 0 \
    --Order asc \
    --By id
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "AssetType": "HOST",
                "HostInfo": {
                    "AgentStatus": "ONLINE",
                    "Appid": 200000000,
                    "CloudTag": [],
                    "InstanceID": "ins-g*****8w",
                    "InstanceStatus": "RUNNING",
                    "Name": "tke_cls-p************er",
                    "OsInfo": "TencentOS Server 3.1 (TK4)",
                    "PrivateIP": "172.16.0.2",
                    "ProtectVersion": "ULTIMATE",
                    "PublicIP": "",
                    "QUUID": "1*********************************68",
                    "RegionInfo": {
                        "Region": "ap-guangzhou",
                        "RegionCode": "",
                        "RegionId": 0,
                        "RegionName": "广州",
                        "RegionNameEn": "Guangzhou"
                    },
                    "TagItem": [],
                    "UUID": "1*********************************68"
                },
                "ID": 860000000981,
                "ItemID": 8,
                "JobID": "4f79e5a928c46322fd15525a74f1bb60",
                "LatestCheckTime": "2026-08-11T12:51:15Z",
                "ResultStatus": "PASS",
                "RiskID": "0144c54f6cb6a5c2173c7a7d15f8605f"
            }
        ],
        "TotalCount": 11,
        "RequestId": "c54373bc-6d6b-4e17-9d6b-803db402b0af"
    }
}
```

