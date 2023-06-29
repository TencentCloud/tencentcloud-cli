**Example 1: 查询当前用户指定小程序的诊断安全得分情况**



Input: 

```
tccli mmps DescribeFlySecMiniAppScanReportList --cli-unfold-argument  \
    --Status 1 \
    --MiniAppVersion V125 \
    --MiniAppID wx66e50f1e*******6f \
    --Mode 1 \
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
                "Status": 1,
                "CreateTime": 1617796174,
                "RiskScore": "62.1",
                "RiskLevel": 1,
                "RiskItems": {
                    "RiskItem1Score": 0,
                    "RiskItem2Score": 30,
                    "RiskItem3Score": 70,
                    "RiskItem4Score": 40,
                    "RiskItem5Score": 50,
                    "RiskItem6Score": 100,
                    "RiskItem7Score": 80,
                    "RiskItem8Score": 100
                }
            }
        ],
        "Total": 1
    }
}
```

