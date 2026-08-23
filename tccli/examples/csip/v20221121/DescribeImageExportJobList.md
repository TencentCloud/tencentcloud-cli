**Example 1: 查询镜像仓库导出任务列表**



Input: 

```
tccli csip DescribeImageExportJobList --cli-unfold-argument  \
    --MemberId mem-12e1se11
```

Output: 
```
{
    "Response": {
        "JobList": [
            {
                "ExportCreateTime": "2026-08-12T20:40:10+08:00",
                "ExportType": "ImageAssetList",
                "JobID": "8a487ee1-f811-40a1-91f8-53cd45c408c7",
                "Name": "asset_list",
                "OwnerAppId": 260000000,
                "Status": "SUCCESS"
            }
        ],
        "TotalCount": 88,
        "RequestId": "341177b1-9a65-4759-88a5-d73545d60944"
    }
}
```

