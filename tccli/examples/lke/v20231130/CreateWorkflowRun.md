**Example 1: 正确示例**

正确示例

Input: 

```
tccli lke CreateWorkflowRun --cli-unfold-argument  \
    --AppBizId 2013099073199108224 \
    --RunEnv 0 \
    --Query 你好 \
    --CustomVariables.0.Name Url \
    --CustomVariables.0.Value https://www.baidu.com \
    --VisitorId user-123
```

Output: 
```
{
    "Response": {
        "AppBizId": "2013099073199108224",
        "CreateTime": "1774444678419",
        "CustomVariables": [
            {
                "Name": "Url",
                "Value": "https://www.baidu.com"
            }
        ],
        "Query": "你好",
        "RunEnv": 0,
        "WorkflowRunId": "wfr-brem67jp5pmo",
        "RequestId": "c62597e1-994b-48cd-be41-ba9dee88d5ed"
    }
}
```

