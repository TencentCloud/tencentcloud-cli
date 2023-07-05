**Example 1: 获取Impala查询信息列表**

获取Impala查询信息列表

Input: 

```
tccli emr DescribeImpalaQueries --cli-unfold-argument  \
    --InstanceId emr-qy2p6mem \
    --Offset 0 \
    --Limit 2 \
    --StartTime 1685633400 \
    --EndTime 1686239999
```

Output: 
```
{
    "Response": {
        "Total": 136,
        "RequestId": "12345678999",
        "Results": [
            {
                "Id": "ff4d80b5b577a8e9:79b5f50600000000",
                "TotalInnerBytesSent": 0,
                "State": "FINISHED",
                "ScanKUDURows": 0,
                "Statement": "drop table if  exists impala_cos_parquet",
                "TotalBytesSent": 0,
                "EndTime": 1686068286527,
                "TotalScanBytesSent": 0,
                "NumRowsFetchedFromCache": 0,
                "EstimatedPerHostMemBytes": 0,
                "DefaultDB": "impalatest",
                "User": "hadoop",
                "ScanHDFSRows": 0,
                "ScanRowsTotal": 0,
                "QueryType": "DDL",
                "MaxNodePeakMemoryUsage": "",
                "TotalCpuTime": 0,
                "RowsFetched": 0,
                "Coordinator": "10.0.16.107:27000",
                "StartTime": 1686068286349,
                "Duration": "178.226ms",
                "TotalBytesRead": 0
            },
            {
                "Id": "fd495e63d07810a7:c4c6f25500000000",
                "TotalInnerBytesSent": 0,
                "State": "FINISHED",
                "ScanKUDURows": 0,
                "Statement": "select p1,p2,sum(sore),GROUPING_ID(p1,p2) from impalatest.impala_hdfs_depart group by p1,p2 WITH CUBE",
                "TotalBytesSent": 0,
                "EndTime": 1686068516778,
                "TotalScanBytesSent": 0,
                "NumRowsFetchedFromCache": 0,
                "EstimatedPerHostMemBytes": 0,
                "DefaultDB": "default",
                "User": "hadoop",
                "ScanHDFSRows": 0,
                "ScanRowsTotal": 0,
                "QueryType": "QUERY",
                "MaxNodePeakMemoryUsage": "251.94 MB",
                "TotalCpuTime": 0,
                "RowsFetched": 0,
                "Coordinator": "10.0.16.107:27000",
                "StartTime": 1686068516359,
                "Duration": "418.326ms",
                "TotalBytesRead": 0
            }
        ]
    }
}
```

