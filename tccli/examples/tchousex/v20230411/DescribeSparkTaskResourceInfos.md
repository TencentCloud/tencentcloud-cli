**Example 1: 查询pod资源信息**



Input: 

```
tccli tchousex DescribeSparkTaskResourceInfos --cli-unfold-argument  \
    --QuerySparkTaskResourceReq.Offset 0 \
    --QuerySparkTaskResourceReq.Limit 10 \
    --QuerySparkTaskResourceReq.TaskId batch-task-6wupcu \
    --InstanceId warehouse-j5bbsmrs
```

Output: 
```
{
    "Response": {
        "RequestId": "8f469c95-0c5d-4089-a778-dab28c86bbbb",
        "Count": 2,
        "SparkTaskPodInfos": [
            {
                "Id": 8885,
                "InstanceId": "warehouse-j5bbsmrs",
                "TaskId": "batch-task-6wupcu",
                "PodName": "batch-task-6wupcu-driver",
                "Status": 2,
                "PodCores": 4,
                "Type": 1,
                "CreateTime": "2024-12-12 10:19:54",
                "ModifyTime": "2024-12-12 10:48:17",
                "ExecuteTime": "28min13s",
                "BeginTime": "2024-12-12 10:20:02",
                "EndTime": "2024-12-12 10:48:15",
                "ResourceUsage": 6772,
                "PodSpec": "2X-Small"
            },
            {
                "Id": 8886,
                "InstanceId": "warehouse-j5bbsmrs",
                "TaskId": "batch-task-6wupcu",
                "PodName": "batch-task-6wupcu-exec-1",
                "Status": 2,
                "PodCores": 4,
                "Type": 2,
                "CreateTime": "2024-12-12 10:20:09",
                "ModifyTime": "2024-12-12 10:48:02",
                "ExecuteTime": "8s",
                "BeginTime": "2024-12-12 10:47:53",
                "EndTime": "2024-12-12 10:48:01",
                "ResourceUsage": 32,
                "PodSpec": "2X-Small"
            }
        ],
        "QuerySparkTaskResourceSummaryInfo": {
            "TaskStatus": 2,
            "ResourceUsage": 1.89
        },
        "ErrorMsg": ""
    }
}
```

