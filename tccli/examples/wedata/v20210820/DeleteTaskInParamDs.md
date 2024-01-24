**Example 1: 删除任务输入参数**

删除任务输入参数

Input: 

```
tccli wedata DeleteTaskInParamDs --cli-unfold-argument  \
    --TaskId abc \
    --ProjectId 123123 \
    --ParamKey abc
```

Output: 
```
{
    "Response": {
        "Data": true,
        "RequestId": "abc"
    }
}
```

