**Example 1: 删除任务输出参数**

删除任务输出参数

Input: 

```
tccli wedata DeleteTaskOutParamDs --cli-unfold-argument  \
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

