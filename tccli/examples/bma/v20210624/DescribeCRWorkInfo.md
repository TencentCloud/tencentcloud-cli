**Example 1: 查询作品基本信息**



Input: 

```
tccli bma DescribeCRWorkInfo --cli-unfold-argument  \
    --WorkId 111
```

Output: 
```
{
    "Response": {
        "EvidenceStatus": 0,
        "MonitorStatus": 1,
        "AuthorizationEndTime": "xx",
        "Commission": "xx",
        "AuthStatus": 1,
        "Authorization": "xx",
        "AuthorizationStartTime": "xx",
        "IsOriginal": "xx",
        "EvidenceStartTime": "xx",
        "CommissionStartTime": "xx",
        "EvidenceEndTime": "xx",
        "IsRelease": "xx",
        "WorkDesc": "xx",
        "EvidenceUrl": "xx",
        "ProduceTime": "xx",
        "RequestId": "xx",
        "ProducerName": "xx",
        "IsProducer": 0,
        "WhiteLists": [
            "xx"
        ],
        "WorkName": "xx",
        "CommissionEndTime": "xx",
        "CommStatus": 1,
        "WorkCategory": "xx"
    }
}
```

