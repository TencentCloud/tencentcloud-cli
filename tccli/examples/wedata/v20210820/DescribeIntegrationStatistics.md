**Example 1: DescribeIntegrationStatistics**



Input: 

```
tccli wedata DescribeIntegrationStatistics --cli-unfold-argument  \
    --QueryDate 2022-01-01 \
    --TaskType 201 \
    --ProjectId 1
```

Output: 
```
{
    "Response": {
        "TotalTask": 1,
        "ProdTask": 1,
        "DevTask": 2,
        "TotalReadRecords": 1,
        "TotalWriteRecords": 1,
        "TotalErrorRecords": 1,
        "TotalAlarmEvent": 1,
        "IncreaseReadRecords": 1,
        "IncreaseWriteRecords": 1,
        "IncreaseErrorRecords": 1,
        "IncreaseAlarmEvent": 1,
        "AlarmEvent": "{\"important\":1,\"ordinary\":0,\"urgent\":0}",
        "RequestId": "xx"
    }
}
```

