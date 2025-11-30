**Example 1: 设备风险检测示例**

设备风险检测示例

Input: 

```
tccli rce DescribeDeviceRisk --cli-unfold-argument  \
    --BizData.UserId userId \
    --BizData.FaceIdBizCode 1 \
    --BizData.ProductMode PLUS \
    --BizData.SceneCode 1 \
    --BizData.FaceIdToken a24fr3g****b5de3 \
    --BizData.Source faceid \
    --BizData.DeviceToken AYIAwde9ZhP4QUS***Ddqsr \
    --BizData.DeviceIp 198.100.***.***
```

Output: 
```
{
    "Response": {
        "Data": {
            "Code": 0,
            "Message": "OK",
            "Uuid": "ee291cae-****-****-****-3d5787e84a93",
            "Value": {
                "CamParam": "DQABAShTeeC40****N292UzBucmRiWT0=",
                "Extra": "{\"ActionSequence\":\"1\",\"EnableCameraRisk\":\"false\"}",
                "HitRules": "{\"默认策略\":\"10000\"}",
                "OpenId": "MRF3A2995****E12F1E",
                "RiskLevel": "pass",
                "RiskScore": 1,
                "Seq": "1757222262-****-34-1705"
            }
        },
        "RequestId": "4c40d8f8-***-***-***-2d2e31dd7b42"
    }
}
```

