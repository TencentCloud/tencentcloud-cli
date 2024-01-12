**Example 1: 获取某个应用关键指标统计数据**

获取某个应用关键指标统计数据

Input: 

```
tccli tdid GetOverSummary --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "30e5b3c3-19fa-4601-8b29-cdb09cea4467",
        "AppCnt": 2,
        "DeployCnt": 2,
        "ChainCnt": 1,
        "AppCounter": {
            "DidCnt": 677,
            "VCCnt": 942,
            "CPTCnt": 4,
            "VerifyCnt": 1288
        },
        "UserCounter": {
            "DidCnt": 342,
            "VCCnt": 484,
            "CPTCnt": 4,
            "VerifyCnt": 648
        }
    }
}
```

