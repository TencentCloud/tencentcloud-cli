**Example 1: 查询作品监测详情**



Input: 

```
tccli bma DescribeCRMonitorDetail --cli-unfold-argument  \
    --PageNumber 0 \
    --PageSize 0 \
    --WorkId 0
```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "MonitorStatus": 0,
        "RequestId": "xx",
        "Torts": [
            {
                "TortId": 0,
                "DetectTime": "xx",
                "WorkTitle": "xx",
                "Author": "xx",
                "BlockStatus": 0,
                "TortURL": "xx",
                "TortTitle": "xx",
                "PubTime": "xx",
                "TortNum": "xx",
                "ObtainNote": "xx",
                "TortPlat": "xx",
                "RightStatus": 0,
                "ObtainStatus": 0
            }
        ]
    }
}
```

