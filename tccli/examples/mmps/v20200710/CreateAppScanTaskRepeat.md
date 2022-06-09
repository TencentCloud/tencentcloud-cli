**Example 1: 创建小程序隐私合规诊断重试任务**

原任务失败后，重新提交隐私合规诊断基础版任务

Input: 

```
tccli mmps CreateAppScanTaskRepeat --cli-unfold-argument  \
    --TaskType 0 \
    --Source 0 \
    --AppPackage wx66e50f1e*******6f \
    --Platform 2 \
    --OrgTaskID 170143813*******360
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

