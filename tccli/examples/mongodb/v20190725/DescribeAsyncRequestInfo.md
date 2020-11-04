**Example 1: 查询异步任务状态接口**



Input: 

```
tccli mongodb DescribeAsyncRequestInfo --cli-unfold-argument  \
    --AsyncRequestId 4762
```

Output: 
```
{
    "Response": {
        "RequestId": "e600a8d0-9014-11ea-84c1-01cccde830c6",
        "Status": "success"
    }
}
```

