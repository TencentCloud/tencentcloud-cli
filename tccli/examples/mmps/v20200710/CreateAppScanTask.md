**Example 1: 创建小程序隐私合规基础诊断任务**



Input: 

```
tccli mmps CreateAppScanTask --cli-unfold-argument  \
    --AppPackage wx66e50f1e*******6f \
    --Source 0 \
    --Platform 2 \
    --TaskType 0
```

Output: 
```
{
    "Response": {
        "RequestId": "xxxxxx",
        "Result": 0,
        "TaskID": "170143813*******360"
    }
}
```

