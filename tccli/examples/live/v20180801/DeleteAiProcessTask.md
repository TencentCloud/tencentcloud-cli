**Example 1: 请求示例**

删除AI处理任务。

Input: 

```
tccli live DeleteAiProcessTask --cli-unfold-argument  \
    --DomainName abc \
    --AppName abc \
    --StreamName abc \
    --TaskParamList.0.TaskType abc
```

Output: 
```
{
    "Response": {
        "RequestId": "abc"
    }
}
```

