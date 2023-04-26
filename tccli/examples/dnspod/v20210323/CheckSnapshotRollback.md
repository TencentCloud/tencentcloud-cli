**Example 1: 快照回滚前检查**

 

Input: 

```
tccli dnspod CheckSnapshotRollback --cli-unfold-argument  \
    --Domain domain.com \
    --SnapshotId A45A0XXX
```

Output: 
```
{
    "Response": {
        "RequestId": "b8a0fd97-4a54-40ce-a7a9-a97523eaaf2e",
        "Domain": "domain.com",
        "SnapshotId": "A45A0XXX",
        "Total": 63,
        "Failed": 1,
        "CostMinutes": 1,
        "FailedRecordList": [
            {
                "RecordId": "15772994",
                "SubDomain": "@",
                "RecordType": "CNAME",
                "RecordLine": "test",
                "Value": "mailhz.qiye.163.com.",
                "Weight": null,
                "Reason": "线路不存在",
                "TTL": "600",
                "MX": "0"
            }
        ],
        "Timeout": null
    }
}
```

