**Example 1: 实时任务运行指标概览**

实时任务运行指标概览

Input: 

```
tccli wedata DescribeRealTimeTaskMetricOverview --cli-unfold-argument  \
    --ProjectId abc \
    --TaskId 123 \
    --StartTime 1669693200000 \
    --EndTime 1669693200000
```

Output: 
```
{
    "Response": {
        "TotalRecordNumOfRead": 1,
        "TotalRecordByteNumOfRead": 1,
        "TotalRecordNumOfWrite": 1,
        "TotalRecordByteNumOfWrite": 1,
        "TotalDirtyRecordNum": 1,
        "TotalDirtyRecordByte": 1,
        "TotalDuration": 1,
        "BeginRunTime": "abc",
        "EndRunTime": "abc",
        "RequestId": "abc"
    }
}
```

