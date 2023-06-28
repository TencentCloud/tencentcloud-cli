**Example 1: 请求示例**

查询实例任务执行结果。

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
        "TaskType": "redis缓存清空流程",
        "InstanceId": "crs-09u2u96z",
        "TaskMessage": "",
        "RequestId": "81120ab8-fea0-41ab-af7e-283c0348c4fc"
    }
}
```

