**Example 1: 获取基础诊断任务参数信息**

获取当前用户提交诊断时的参数信息

Input: 

```
tccli mmps DescribeFlySecMiniAppScanTaskParam --cli-unfold-argument  \
    --TaskID 1701438134******0
```

Output: 
```
{
    "Response": {
        "RequestId": "5e93a212-ca01-0fdc-eedd-5a1fce5e83e6",
        "Ret": 0,
        "MiniAppID": "wx66e50f1e*******6f",
        "Mode": 1,
        "ScanVersion": 0,
        "MiniAppTestAccount": "Test",
        "MiniAppTestPwd": "TestPwd"
    }
}
```

