**Example 1: 查询死锁日志**



Input: 

```
tccli dbbrain DescribeDeadLockLogs --cli-unfold-argument  \
    --Product sqlserver \
    --InstanceId mssql-15rso1sb \
    --StartTime 2026-09-18 14:50:00 \
    --EndTime 2026-09-18 23:59:59
```

Output: 
```
{
    "Response": {
        "HasMore": false,
        "TotalCount": 8,
        "Items": [
            {
                "InstanceId": "mssql-15rso1sb",
                "TimestampSource": "OBSERVED_LOG",
                "PartialReasonCode": "XML_NOT_AVAILABLE",
                "VictimProcessIds": [],
                "PayloadTruncated": false,
                "SourceUuids": [
                    "7ebe128e-fb90-4f2b-af4c-abc62336e478"
                ],
                "ObservedTransactionCount": 2,
                "GraphStatus": "MISSING",
                "XmlIncluded": false,
                "ProcessCount": 2,
                "Transactions": [
                    {
                        "Status": "Unknown",
                        "Sessions": [
                            {
                                "SqlFingerprint": null,
                                "LoginName": "sa",
                                "Frames": [],
                                "IsolationLevel": null,
                                "ProcessStatus": null,
                                "ClientApp": null,
                                "Priority": null,
                                "DatabaseName": null,
                                "LockHold": [],
                                "SqlText": null,
                                "Host": "30.101.245.168",
                                "DatabaseId": 11,
                                "IsVictim": null,
                                "WaitTimeMs": null,
                                "ExecutionContextId": null,
                                "LastTransStarted": null,
                                "ProcessId": null,
                                "ClientAppNormalized": null,
                                "LockRequest": [],
                                "SessionId": 61
                            }
                        ],
                        "IsVictim": null,
                        "TransactionId": "170329108"
                    }
                ],
                "DeadlockId": "75789",
                "XmlReport": "",
                "OriginalXmlBytes": null,
                "EventTimestamp": "2026-09-18T09:43:41.5434049+00:00",
                "VictimSessionIds": [
                    83
                ],
                "IsPartial": true,
                "DatabaseNames": [
                    "test_lock"
                ],
                "EventId": "partial:7ebe128e-fb90-4f2b-af4c-abc62336e478",
                "DeadlockSignature": "",
                "Resources": [],
                "AssociationStatus": "UNMATCHED",
                "TransactionCount": 2
            }
        ],
        "ResultVersion": "8cc6fd1f70a2dfbdaa69b590f5daab353a98c959fb24a9d342df483b550ec796",
        "RequestId": "13890fe3-ff26-419e-8b11-78b829cfa9c5"
    }
}
```

