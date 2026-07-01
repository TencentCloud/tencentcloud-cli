**Example 1: 迁移任务的gtid校验**



Input: 

```
tccli dts DescribeMigrateGtidCompareReport --cli-unfold-argument  \
    --JobId dts-49pe4shn
```

Output: 
```
{
    "Response": {
        "Conclusion": "same",
        "Detail": [
            {
                "CompareTimestamp": "2026-02-09T14:48:47+08:00",
                "DiffDst": "",
                "DiffSrc": "7137921b-0247-11f1-8c65-02208de0dcc7:702713-703158",
                "DiffSrcIsNeedSync": false,
                "DiffSrcTables": [],
                "DiffSrcTablesNeedSync": [],
                "DstGtidSets": "7137921b-0247-11f1-8c65-02208de0dcc7:1-702712",
                "Result": "consistent",
                "SrcGtidSets": "7137921b-0247-11f1-8c65-02208de0dcc7:1-703158"
            }
        ],
        "Status": "success",
        "Type": "gtid",
        "RequestId": "359c197e-f6fb-4b24-b4f2-aae6abcea090"
    }
}
```

