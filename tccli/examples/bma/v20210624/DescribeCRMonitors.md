**Example 1: 查询监测列表**

查询监测列表

Input: 

```
tccli bma DescribeCRMonitors --cli-unfold-argument  \
    --PageNumber 1 \
    --PageSize 10
```

Output: 
```
{
    "Response": {
        "TotalCount": 4,
        "ExportURL": "xx",
        "Monitors": [
            {
                "TortURLNum": 0,
                "EvidenceNote": "xx",
                "MonitorStatus": 1,
                "EvidenceStatus": 0,
                "WorkId": 39,
                "WorkCategoryAll": "xx",
                "TortPlatNum": 0,
                "WorkName": "xx",
                "InsertTime": "xx",
                "TortSiteNum": 0,
                "WorkCategory": "xx",
                "MonitorNote": "xx",
                "MonitorTime": "xx",
                "WorkType": "xx"
            },
            {
                "TortURLNum": 0,
                "EvidenceNote": "xx",
                "MonitorStatus": 1,
                "EvidenceStatus": 0,
                "WorkId": 38,
                "WorkCategoryAll": "xx",
                "TortPlatNum": 0,
                "WorkName": "xx",
                "InsertTime": "xx",
                "TortSiteNum": 0,
                "WorkType": "xx",
                "MonitorNote": "xx",
                "MonitorTime": "xx",
                "WorkCategory": "xx"
            },
            {
                "TortURLNum": 0,
                "EvidenceNote": "xx",
                "MonitorStatus": 1,
                "EvidenceStatus": 0,
                "WorkId": 37,
                "WorkCategoryAll": "xx",
                "TortPlatNum": 0,
                "WorkName": "xx",
                "InsertTime": "xx",
                "TortSiteNum": 0,
                "WorkType": "xx",
                "MonitorNote": "xx",
                "MonitorTime": "xx",
                "WorkCategory": "xx"
            },
            {
                "TortURLNum": 4,
                "EvidenceNote": "xx",
                "MonitorStatus": 1,
                "EvidenceStatus": 0,
                "WorkId": 36,
                "WorkCategoryAll": "xx",
                "TortPlatNum": 4,
                "WorkName": "xx",
                "InsertTime": "xx",
                "TortSiteNum": 0,
                "WorkType": "xx",
                "MonitorNote": "xx",
                "MonitorTime": "xx",
                "WorkCategory": "xx"
            }
        ],
        "RequestId": "xx"
    }
}
```

