**Example 1: 示例**

示例

Input: 

```
tccli cwp DescribeTrialReport --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "AddMachineCnt": 8,
        "AutoBlockBruteCnt": 46,
        "AutoDefenceCnt": 0,
        "AutoIsolateMalwareCnt": 2,
        "AutoVulFixCnt": -1,
        "BaselineRiskCnt": 214,
        "BashCnt": -1,
        "BruteAlarmCnt": 415,
        "CloudFrom": [
            {
                "CloudFrom": 0,
                "MachineCnt": 218
            },
            {
                "CloudFrom": 2,
                "MachineCnt": 2
            },
            {
                "CloudFrom": 3,
                "MachineCnt": 1
            }
        ],
        "DnsCnt": 0,
        "EventCnt": 0,
        "FileTamperCnt": 0,
        "IsShow": false,
        "JavaShellCnt": -1,
        "MalwareAlarmCnt": 59,
        "RequestId": "aa3ccfe9-5dc3-40d2-8831-aa99e9a12207",
        "VulCnt": 26
    }
}
```

