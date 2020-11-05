**Example 1: Request Sample**



Input: 

```
tccli redis DescribeTaskInfo --cli-unfold-argument  \
    --TaskId 18215
```

Output: 
```
{
    "Response": {
        "Status": "succeed",
        "StartTime": "2018-11-01 17:25:14",
        "TaskType": "Redis cache purge process",
        "InstanceId": "crs-09u2u96z",
        "TaskMessage": "",
        "RequestId": "81120ab8-fea0-41ab-af7e-283c0348c4fc"
    }
}
```

