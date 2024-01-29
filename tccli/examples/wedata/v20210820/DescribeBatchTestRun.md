**Example 1: 请求demo**



Input: 

```
tccli wedata DescribeBatchTestRun --cli-unfold-argument  \
    --BatchTasks.0.CurrRunDate 20:23:23 \
    --BatchTasks.0.InstanceKey 20231012101223445_20:23:23 \
    --BatchTasks.0.TaskId 20231012101223445
```

Output: 
```
{
    "Response": {
        "RequestId": "4af5a5ed-eb41-4ab7-b1fe-da7b5144eed4",
        "BatchTaskResult": [
            {
                "InstanceKey": "20231012101223445_20:23:23",
                "Status": "FAIL",
                "Finished": true,
                "LogContent": "echo 111"
            }
        ]
    }
}
```

