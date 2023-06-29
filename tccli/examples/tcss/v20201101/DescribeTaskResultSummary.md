**Example 1: 常规请求**

请求成功获取的实例

Input: 

```
tccli tcss DescribeTaskResultSummary --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "SeriousRiskNodeCount": [
            2,
            3,
            2,
            3,
            2,
            3,
            2,
            3,
            2
        ],
        "HighRiskNodeCount": [
            2,
            3,
            2,
            3,
            2,
            3,
            2,
            3,
            2
        ],
        "MiddleRiskNodeCount": [
            2,
            3,
            2,
            3,
            2,
            3,
            2,
            3,
            2
        ],
        "HintRiskNodeCount": [
            2,
            3,
            2,
            3,
            2,
            3,
            2,
            3,
            2
        ],
        "RequestId": "xx"
    }
}
```

