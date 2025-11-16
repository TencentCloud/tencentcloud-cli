**Example 1: 相机指纹风险检测示例**

相机指纹风险检测示例

Input: 

```
tccli rce DescribeCameraRisk --cli-unfold-argument  \
    --BizData.UserId userId \
    --BizData.FaceIdBizCode 1 \
    --BizData.ProductMode PLUS \
    --BizData.SceneCode e_activity_9291 \
    --BizData.FaceIdToken a24fr3g****b5de3 \
    --BizData.CamToken v3:AAAAA****YyWjqZdo=
```

Output: 
```
{
    "Response": {
        "Data": {
            "Code": 0,
            "Message": "OK",
            "Uuid": "743a2698-****-****-****-e2ab389e81b1",
            "Value": {
                "Extra": "{\"ActionSequence\":\"1\",\"EnableCameraRisk\":\"false\"}",
                "HitRules": "{\"默认策略\":\"10000\"}",
                "OpenId": "MRF3A****12F1E",
                "RiskLevel": "pass",
                "RiskScore": 1,
                "Seq": "1757318214-****-**-169"
            }
        },
        "RequestId": "eedd5977-****-****-****-4d4c78a1e96c"
    }
}
```

