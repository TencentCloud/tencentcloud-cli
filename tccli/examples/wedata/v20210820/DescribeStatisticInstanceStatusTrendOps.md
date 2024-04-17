**Example 1: 任务状态趋势示例**

任务状态趋势

Input: 

```
tccli wedata DescribeStatisticInstanceStatusTrendOps --cli-unfold-argument  \
    --ProjectId 153160969665952 \
    --TaskTypeId  \
    --StateList 2 \
    --StartTime 2024-04-14 00:00:00 \
    --EndTime 2024-04-14 23:59:59 \
    --InCharge  \
    --AggregationUnit H \
    --WorkflowId 
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "Count": 9,
                "CountList": null,
                "InstanceCount": 0,
                "InstanceStatus": "SUCCEED",
                "ReportTime": "2024-04-14 01:00:00",
                "ShowTime": null,
                "TimeList": null
            }
        ],
        "RequestId": "e75879e3-0fa6-472d-a1df-3408e4501c08"
    }
}
```

