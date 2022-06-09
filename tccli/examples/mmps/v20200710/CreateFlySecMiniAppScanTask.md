**Example 1: 创建小程序翼扬安全基础诊断任务**



Input: 

```
tccli mmps CreateFlySecMiniAppScanTask --cli-unfold-argument  \
    --MiniAppID wx66e50f1e*******6f \
    --Mode 1 \
    --ScanVersion 0 \
    --MiniAppTestAccount Test \
    --MiniAppTestPwd TestPwd \
    --Industry 电商 \
    --SurveyContent {"wx66e50f1e*******6f":{"1":["B"],"n":["A","B","D"]}} \
    --Mobile 13800138000 \
    --Email wechat@tencent.com \
    --SalesPerson 王某
```

Output: 
```
{
    "Response": {
        "RequestId": "xxxxxx",
        "Ret": 0,
        "TaskID": "170143813*******360"
    }
}
```

