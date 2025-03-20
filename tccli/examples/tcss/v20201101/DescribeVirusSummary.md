**Example 1: 运行时查询木马概览信息**

运行时查询木马概览信息

Input: 

```
tccli tcss DescribeVirusSummary --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "IsolateCnt": 1133,
        "IsolateIncrease": 0,
        "RequestId": "83b45d62-7383-4257-8de5-f460a3446a2c",
        "RiskCnt": 94,
        "RiskContainerCnt": 58,
        "RiskContainerIncrease": 0,
        "RiskIncrease": 0,
        "TaskId": "67204f7cad8a5e71a40875752cc2f374",
        "VirusDataBaseModifyTime": "2020-11-21 15:16:00"
    }
}
```

