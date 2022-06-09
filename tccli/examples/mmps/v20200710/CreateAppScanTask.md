**Example 1: 创建小程序隐私合规基础诊断任务**



Input: 

```
tccli mmps CreateAppScanTask --cli-unfold-argument  \
    --TaskType 0 \
    --Source 0 \
    --AppPackage wx66e50f1e*******6f \
    --Platform 2
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

