**Example 1: 获取SparkSQL批任务运行状态**

获取SparkSQL批任务运行状态

Input: 

```
tccli dlc DescribeSparkSessionBatchSQL --cli-unfold-argument  \
    --BatchId d3018ad4-9a7e-4f64-a3f4-fsjr37c69742
```

Output: 
```
{
    "Response": {
        "State": 0,
        "Event": "",
        "Tasks": [
            {
                "TaskId": "b8sdsdds-ekd4-4e5e-993e-e87js4fa21c1",
                "ExecuteSQL": "select 1;",
                "Message": "Task Success!"
            }
        ],
        "RequestId": "b8sd7dd7-ekd4-4e5e-993e-e5db64fa21c1"
    }
}
```

