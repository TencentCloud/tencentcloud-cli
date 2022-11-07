**Example 1: 实时任务运行指标概览**

实时任务运行指标概览

Input: 

```
tccli wedata DescribeRealTimeTaskMetricOverview --cli-unfold-argument  \
    --ProjectId xx \
    --TaskId xx
```

Output: 
```
{
    "Response": {
        "TotalRecordNumOfWrite": 1,
        "TotalDirtyRecordByte": 1,
        "TotalDirtyRecordNum": 1,
        "EndRunTime": "xx",
        "RequestId": "xx",
        "TotalRecordNumOfRead": 1,
        "TotalRecordByteNumOfRead": 1,
        "BeginRunTime": "xx",
        "TotalRecordByteNumOfWrite": 1,
        "TotalDuration": 1
    }
}
```

