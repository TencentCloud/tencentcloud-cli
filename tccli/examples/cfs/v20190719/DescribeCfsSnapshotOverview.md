**Example 1: 查询快照概览**



Input: 

```
tccli cfs DescribeCfsSnapshotOverview --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "StatisticsList": [
            {
                "Region": "ap-guangzhou",
                "SnapshotNumber": 6,
                "SnapshotSize": 33
            },
            {
                "Region": "all",
                "SnapshotNumber": 10,
                "SnapshotSize": 330
            }
        ],
        "RequestId": "b398b508-6ac6-4a05-9c20-388399bd1965"
    }
}
```

