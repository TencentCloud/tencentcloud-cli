**Example 1: 查询诊断任务状态**

任务失败情况

Input: 

```
tccli mmps DescribeFlySecMiniAppScanTaskStatus --cli-unfold-argument  \
    --TaskID 1701438134******0
```

Output: 
```
{
    "Response": {
        "RequestId": "5e93a212-ca01-0fdc-eedd-5a1fce5e83e6",
        "Ret": 0,
        "Status": 2,
        "Errno": 100010,
        "MiniAppName": "测试小程序",
        "MiniAppVersion": "V125"
    }
}
```

