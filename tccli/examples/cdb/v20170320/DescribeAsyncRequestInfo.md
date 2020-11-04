**Example 1: 查询异步任务的执行结果**



Input: 

```
tccli cdb DescribeAsyncRequestInfo --cli-unfold-argument  \
    --AsyncRequestId f96e4f3c-8fc96c86-2ec79ac8-cb63a7a7
```

Output: 
```
{
    "Response": {
        "Info": "删除库表成功",
        "Status": "SUCCESS",
        "RequestId": "faae8d6a-38fb-44de-988e-5a0e78aba4a7"
    }
}
```

