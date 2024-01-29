**Example 1: 查询任务输出参数**

查询任务输出参数

Input: 

```
tccli wedata DescribeTaskOutParamDs --cli-unfold-argument  \
    --TaskId abc \
    --ProjectId 123123 \
    --Upstream True
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
                "ParamDefine": "abc",
                "CreateTime": "abc",
                "UpdateTime": "abc",
                "TaskName": "abc",
                "ProjectId": "abc",
                "ProjectName": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

