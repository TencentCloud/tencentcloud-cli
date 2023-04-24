**Example 1: 请求示例**

创建AI处理任务。

Input: 

```
tccli live CreateAiProcessTask --cli-unfold-argument  \
    --DomainName abc \
    --AppName abc \
    --StreamName abc \
    --TaskParamList.0.TaskType abc
```

Output: 
```
{
    "Response": {
        "RequestId": "1047d0dc-6dc8-4898-a7f3-03726a822b0e"
    }
}
```

