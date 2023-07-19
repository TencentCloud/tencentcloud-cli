**Example 1: 时序日志主题查询**

时序日志主题查询

Input: 

```
tccli cls QueryMetric --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "x20",
        "ResultType": "vector",
        "Result": "[{\"metric\":{\"__name__\":\"up\",\"job\":\"prometheus\",\"instance\":\"localhost:9090\"},\"value\":[1435781451.781,\"1\"]},{\"metric\":{\"__name__\":\"up\",\"job\":\"node\",\"instance\":\"localhost:9100\"},\"value\":[1435781451.781,\"0\"]}]"
    }
}
```

