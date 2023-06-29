**Example 1: 重新创建小程序翼扬安全基础诊断任务**

原任务失败后，重新提交基础诊断任务

Input: 

```
tccli mmps CreateFlySecMiniAppScanTaskRepeat --cli-unfold-argument  \
    --MiniAppTestPwd TestPwd \
    --OrgTaskID 170143813*******360 \
    --MiniAppID wx66e50f1e*******6f \
    --Mode 1 \
    --ScanVersion 0 \
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

