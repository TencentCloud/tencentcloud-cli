**Example 1: 查询任务输入参数**

查询任务输入参数

Input: 

```
tccli wedata DescribeTaskInParamDs --cli-unfold-argument  \
    --TaskId abc \
    --ProjectId 12312312
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "Id": 0,
                "TaskId": "abc",
                "ParamKey": "abc",
                "ParamDesc": "abc",
                "FromTaskId": "abc",
                "FromParamKey": "abc",
                "CreateTime": "abc",
                "UpdateTime": "abc",
                "FromTaskName": "abc",
                "FromProjectId": "abc",
                "FromProjectName": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

