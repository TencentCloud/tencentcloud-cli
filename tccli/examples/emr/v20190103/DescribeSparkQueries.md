**Example 1: 查询spark查询信息**



Input: 

```
tccli emr DescribeSparkQueries --cli-unfold-argument  \
    --InstanceId emr-njry92zr \
    --StartTime 1711078120 \
    --EndTime 1711088221 \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "RequestId": "690f07d6-ac3d-4211-896d-043824aaa0f0",
        "Total": 1,
        "Results": [
            {
                "Id": "2",
                "Status": "COMPLETED",
                "BeginTime": 1711078220,
                "ScanTotalData": 0,
                "ApplicationId": [
                    "application_1710488265927_0018"
                ],
                "ScanRowNum": 1,
                "ScanFileNum": 1,
                "EndTime": 1711078223,
                "ScanPartitionNum": 1,
                "Statement": "select * from hive_table_p2 where dt='20240321.3'",
                "Duration": 2924
            }
        ]
    }
}
```

