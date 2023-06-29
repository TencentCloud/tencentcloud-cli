**Example 1: 运行时查询木马概览信息**

运行时查询木马概览信息

Input: 

```
tccli tcss DescribeVirusSummary --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "TaskId": "xx",
        "RiskContainerCnt": 1,
        "RiskCnt": 1,
        "VirusDataBaseModifyTime": "xx",
        "RiskContainerIncrease": 1,
        "RiskIncrease": 1,
        "IsolateIncrease": 1,
        "IsolateCnt": 1,
        "RequestId": "xx"
    }
}
```

