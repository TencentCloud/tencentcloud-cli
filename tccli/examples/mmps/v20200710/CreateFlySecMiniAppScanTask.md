**Example 1: 创建小程序翼扬安全基础诊断任务**



Input: 

```
tccli mmps CreateFlySecMiniAppScanTask --cli-unfold-argument  \
    --MiniAppTestPwd TestPwd \
    --Mobile 13800138000 \
    --Industry 电商 \
    --SurveyContent {"wx66e50f1e*******6f":{"1":["B"],"n":["A","B","D"]}} \
    --MiniAppID wx66e50f1e*******6f \
    --Mode 1 \
    --SalesPerson 王某 \
    --ScanVersion 0 \
    --Email wechat@tencent.com \
    --MiniAppTestAccount Test
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

