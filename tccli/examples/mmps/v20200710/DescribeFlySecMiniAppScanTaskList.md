**Example 1: 获取诊断任务列表**



Input: 

```
tccli mmps DescribeFlySecMiniAppScanTaskList --cli-unfold-argument  \
    --MiniAppID wx66e50f1e*******6f \
    --Mode 1 \
    --Status 1 \
    --Size 10
```

Output: 
```
{
    "Response": {
        "RequestId": "5e93a212-ca01-0fdc-eedd-5a1fce5e83e6",
        "Ret": 0,
        "Data": [
            {
                "TaskID": "1701438134******0",
                "MiniAppID": "wx66e50f1e*******6f",
                "MiniAppName": "测试小程序",
                "MiniAppVersion": "V125",
                "Mode": 1,
                "CreateTime": 1617796174,
                "Status": 2,
                "Error": 100010
            }
        ],
        "Total": 1
    }
}
```

