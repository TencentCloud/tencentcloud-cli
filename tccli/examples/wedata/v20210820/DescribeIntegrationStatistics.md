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
        "TotalTask": 0,
        "ProdTask": 0,
        "DevTask": 0,
        "TotalReadRecords": 0,
        "TotalWriteRecords": 0,
        "TotalErrorRecords": 0,
        "TotalAlarmEvent": 0,
        "IncreaseReadRecords": 0,
        "IncreaseWriteRecords": 0,
        "IncreaseErrorRecords": 0,
        "IncreaseAlarmEvent": 0,
        "AlarmEvent": "{\"important\":1,\"ordinary\":0,\"urgent\":0}",
        "RequestId": "as1cs2c123asyi23bh213cc"
    }
}
```

