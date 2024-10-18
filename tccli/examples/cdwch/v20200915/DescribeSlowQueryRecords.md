**Example 1: 慢查询列表**

慢查询列表

Input: 

```
tccli cdwch DescribeSlowQueryRecords --cli-unfold-argument  \
    --InstanceId abc \
    --QueryDurationMs 0 \
    --StartTime abc \
    --EndTime abc \
    --PageSize 0 \
    --PageNum 0 \
    --DurationMs abc \
    --VirtualCluster abc
```

Output: 
```
{
    "Response": {
        "RequestId": "afde5f25-76b8-4734-b99f-d6f0b01059d6",
        "TotalCount": 0,
        "SlowQueryRecords": []
    }
}
```

