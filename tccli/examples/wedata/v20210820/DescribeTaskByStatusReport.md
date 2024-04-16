**Example 1: 任务状态趋势示例**

任务状态趋势

Input: 

```
tccli wedata DescribeTaskByStatusReport --cli-unfold-argument  \
    --ProjectId 1531609696090365052 \
    --TaskType  \
    --StartTime 2024-04-10 00:00:00 \
    --EndTime 2024-04-10 23:59:59 \
    --InCharge  \
    --Status F \
    --CycleUnit W \
    --AggregationUnit H \
    --WorkflowId 
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "Count": 1,
                "CountGroup": null,
                "CycleUnit": null,
                "ReportTime": "2024-04-11 00:00:00",
                "ShowTimeGroup": null,
                "Status": "F"
            }
        ],
        "RequestId": "96c852e0-eb58-4954-845c-b4ec5648dd9d"
    }
}
```

