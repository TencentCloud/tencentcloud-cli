**Example 1: 成功示例**



Input: 

```
tccli ocr AuditMaterialAgent --cli-unfold-argument  \
    --AgentType StorePicAudit \
    --ImageUrl https://engine-private-1258344699.cos.ap-guangzhou.myqcloud.com/test/kaibin/%E7%A4%BA%E4%BE%8B%E4%BA%8C%E9%97%A8%E5%A4%B4%E7%85%A7%E6%9C%89%E6%B0%B4%E5%8D%B0.jpg?q-sign-algorithm=sha1&q-**********gT*FEwNXR4SZP0KNAhxwf8KFsEJ7e&q-sign-time=1793793983;1793801183&q-key-time=1793793983;1793801183&q-header-list=host&q-url-param-list=&q-signature=43c532b0554a5060e9ab7e9a95a7083c94455cb1 \
    --ImageBase64 base64 \
    --NeedSceneType True \
    --StoreInfoHint 星星便利店 \
    --IgnoreWatermarkCategories PhoneCam
```

Output: 
```
{
    "Response": {
        "Angle": 4.170954704284668,
        "RemakeScreen": {
            "IsWarn": true,
            "Polygon": [],
            "RiskConfidence": 0.735259
        },
        "SceneType": "各类杂货店,便利店（5331）、瓶装酒零售店（5921）、各类食品店及专门食品零售店（5499）",
        "Screenshot": {
            "IsWarn": true,
            "Polygon": [],
            "RiskConfidence": 0.735259
        },
        "StoreInfo": [
            {
                "Name": "商店名称",
                "Rect": {
                    "Height": 386,
                    "Width": 990,
                    "X": 307,
                    "Y": -30
                },
                "Value": "芙蓉兴盛"
            }
        ],
        "StoreLabel": [
            "标准门头照"
        ],
        "Synthesis": {
            "IsWarn": false,
            "Polygon": [],
            "RiskConfidence": 0.0009727084
        },
        "Tamper": {
            "IsWarn": false,
            "Polygon": [],
            "RiskConfidence": 0
        },
        "Template": {
            "IsWarn": false,
            "Polygon": [],
            "RiskConfidence": 0.415345
        },
        "TextWatermark": {
            "IsWarn": true,
            "Polygon": [],
            "RiskConfidence": 0.9999729
        },
        "WatermarkContent": "仅限商户注册，他用无效|商户入网专用",
        "RequestId": "b73c12fb-0b91-4f01-90cd-03131dc362f3"
    }
}
```

