**Example 1: 查询错误汇总信息**

查询错误汇总信息

Input: 

```
tccli pts DescribeErrorSummary --cli-unfold-argument  \
    --ProjectId project-xx \
    --JobId job-xx \
    --ScenarioId scenario-xx
```

Output: 
```
{
    "Response": {
        "RequestId": "abc-123-xyz",
        "ErrorSummarySet": [
            {
                "Status": "404",
                "Result": "404 Not Found",
                "Proto": "HTTP/1.1",
                "Count": 17,
                "Rate": 47.22222222222222,
                "Message": "该状态码表明，服务器找不到客户端请求的资源"
            }
        ]
    }
}
```

