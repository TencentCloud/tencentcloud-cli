**Example 1: 查询任务执行结果**

查询任务执行结果

Input: 

```
tccli dts DescribeAsyncRequestInfo --cli-unfold-argument  \
    --AsyncRequestId cafebabe-254f-11ea-8995-e92c139e6918
```

Output: 
```
{
    "Response": {
        "Status": "success",
        "Info": "ok",
        "RequestId": "cafebabe-254f-11ea-8995-e92c139e6918"
    }
}
```

