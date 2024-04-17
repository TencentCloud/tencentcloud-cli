**Example 1: 实时任务运行指标概览**

实时任务运行指标概览

Input: 

```
tccli wedata DescribeRealTimeTaskMetricOverview --cli-unfold-argument  \
    --ProjectId 1486446569620893696 \
    --TaskId j224b9321-3be0-45de-ad6a-8fed924036a4 \
    --StartTime 1669693200000 \
    --EndTime 1669693200000
```

Output: 
```
{
    "Response": {
        "TotalRecordNumOfRead": 91171,
        "TotalRecordByteNumOfRead": 91171,
        "TotalRecordNumOfWrite": 91171,
        "TotalRecordByteNumOfWrite": 191171,
        "TotalDirtyRecordNum": 91171,
        "TotalDirtyRecordByte": 91171,
        "TotalDuration": 191171,
        "BeginRunTime": "2022-04-10 16:27:09",
        "EndRunTime": "2022-04-11 17:46:40",
        "RequestId": "55c2c097-26da-4302-b0dc-fc22bd33b54d"
    }
}
```

