**Example 1: 创建小程序安全的深度诊断任务**

对小程序全面的进行诊断，包括后台服务安全，UGC合规等

Input: 

```
tccli mmps CreateFlySecMiniAppProfessionalScanTask --cli-unfold-argument  \
    --MiniAppName 测试小程序 \
    --Remark thanks \
    --Mobile 13800138000 \
    --MiniAppID wx66e50f1e*******6f \
    --Mode 2 \
    --CorpName 微信小程序有限公司 \
    --Email wechat@tencent.com
```

Output: 
```
{
    "Response": {
        "RequestId": "5e93a212-ca01-0fdc-eedd-5a1fce5e83e6",
        "Ret": 0
    }
}
```

