**Example 1: 同步任务的gtid校验**



Input: 

```
tccli dts DescribeSyncGtidCompareReport --cli-unfold-argument  \
    --JobId sync-hxjkg3nm \
    --NeedDiffDetail True
```

Output: 
```
{
    "Response": {
        "Conclusion": "different",
        "Detail": [
            {
                "CompareTimestamp": "2026-02-06T11:18:05+08:00",
                "DiffDst": "",
                "DiffSrc": "2e8fd913-0284-11f1-886a-6c0b84d603f8:111378-115020",
                "DiffSrcIsNeedSync": true,
                "DiffSrcTables": [
                    "percona_57.sbtest1"
                ],
                "DiffSrcTablesNeedSync": [
                    "percona_57.sbtest10"
                ],
                "DstGtidSets": "2e8fd913-0284-11f1-886a-6c0b84d603f8:1-111377",
                "Result": "inconsistent",
                "SrcGtidSets": "2e8fd913-0284-11f1-886a-6c0b84d603f8:1-115020"
            }
        ],
        "Status": "success",
        "Type": "gtid",
        "RequestId": "5b33dbf9-26af-4864-933b-d3d509a45bcb"
    }
}
```

