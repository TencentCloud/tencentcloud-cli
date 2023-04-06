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
        "RequestId": "abc",
        "ErrorSummarySet": [
            {
                "Status": "200",
                "Result": "200 OK",
                "Count": 1000,
                "Rate": 1.2,
                "Message": "成功"
            }
        ]
    }
}
```

