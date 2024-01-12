**Example 1: 获取某个应用关键指标统计数据**

获取某个应用关键指标统计数据

Input: 

```
tccli tdid GetAppSummary --cli-unfold-argument  \
    --DAPId 1
```

Output: 
```
{
    "Response": {
        "RequestId": "f3a54a2d-679b-4fd0-9b27-70ae7353b0e9",
        "AppCounter": {
            "DidCnt": 676,
            "VCCnt": 942,
            "CPTCnt": 2,
            "VerifyCnt": 1288,
            "AuthCnt": 2
        },
        "UserCounter": {
            "DidCnt": 341,
            "VCCnt": 484,
            "CPTCnt": 2,
            "VerifyCnt": 648,
            "AuthCnt": 2
        }
    }
}
```

