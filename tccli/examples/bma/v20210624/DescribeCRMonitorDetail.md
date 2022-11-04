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
        "ExportURL": "xx",
        "MonitorStatus": 0,
        "RequestId": "xx",
        "Torts": [
            {
                "IsOverseas": 0,
                "WorkTitle": "xx",
                "RightNote": "xx",
                "Author": "xx",
                "ObtainType": 0,
                "BlockNote": "xx",
                "TortNum": "xx",
                "AuthStatus": 0,
                "DetectTime": "xx",
                "EvidenceStatus": 0,
                "TortTitle": "xx",
                "PubTime": "xx",
                "TortPlat": "xx",
                "TortId": 0,
                "RightStatus": 0,
                "WorkId": 0,
                "TortURL": "xx",
                "ICP": "xx",
                "ObtainStatus": 0,
                "IPLoc": "xx",
                "BlockStatus": 0,
                "IsProducer": 0,
                "WorkName": "xx",
                "TortSite": "xx",
                "ObtainNote": "xx",
                "CommStatus": 0
            }
        ]
    }
}
```

