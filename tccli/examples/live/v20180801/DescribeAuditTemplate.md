**Example 1: 请求示例**

请求示例。

Input: 

```
tccli live DescribeAuditTemplate --cli-unfold-argument  \
    --TemplateId 55023
```

Output: 
```
{
    "Response": {
        "AuditTemplate": {
            "TemplateId": 55023,
            "TemplateName": "appwl9ph4hf4030的消音策略",
            "Description": "appwl9ph4hf4030的消音策略",
            "AuditAudio": true,
            "AuditImage": false,
            "AuditText": 0,
            "AudioInterval": 15,
            "SnapshotInterval": 2,
            "CosBucket": "live-resource",
            "CosRegion": "ap-shanghai",
            "CosFilePath": "/Audit/{Year}-{Month}-{Day}/{StreamID}-Audit-{Hour}-{Minute}-{Second}{Ext}",
            "EnableFailoverCos": false,
            "FailoverCosBucket": "1",
            "FailoverCosRegion": "1",
            "SceneInfos": [
                {
                    "SceneID": "LiveAudit",
                    "BizInfos": [
                        {
                            "BizType": "1_1_7_55023",
                            "Status": true,
                            "StrategyType": "ShortAudio",
                            "StrategyConfig": "{\"user_text_libs\":[\"2758c78c-04c2-478a-a978-e7938037222e\"],\"ability\":{\"asr_text\":true,\"audio\":true},\"asr_text_labels\":{\"abuse\":[],\"ad\":[],\"illegal\":[],\"polity\":[],\"porn\":[],\"terror\":[]},\"audio_labels\":{\"moan\":[\"OVR\"]},\"service_config\":{\"callback_info\":{\"rcb_hseg_count\":30,\"scb_type\":3},\"codec_info\":{\"audio_frequency\":30,\"audio_sampling_rate\":16000},\"maximum_duration\":20},\"ignore_word_conf\":{\"model_disable\":false,\"rule_disable\":false,\"keyword_disable\":false}}"
                        },
                        {
                            "BizType": "1_1_1_55023",
                            "Status": true,
                            "StrategyType": "Text",
                            "StrategyConfig": "{\"user_text_libs\":[\"2758c78c-04c2-478a-a978-e7938037222e\"],\"ability\":{\"text\":true},\"text_labels\":{\"abuse\":[],\"ad\":[],\"illegal\":[],\"polity\":[],\"porn\":[],\"terror\":[]},\"service_config\":{\"callback_info\":{},\"codec_info\":{}},\"ignore_word_conf\":{\"model_disable\":false,\"rule_disable\":false,\"keyword_disable\":false}}"
                        },
                        {
                            "BizType": "1_1_2_55023",
                            "Status": true,
                            "StrategyType": "Image",
                            "StrategyConfig": "{\"ability\":{\"image\":true,\"ocr_text\":true},\"image_labels\":{\"ad\":[\"QRCode\",\"LOGO\"],\"illegal\":[\"Delinquenent\",\"NonMainstream\",\"Illegal\",\"Contraband\",\"PersonalPrivacy\",\"Nausea\"],\"polity\":[\"PositiveCharacter\",\"NegativeFigure\",\"ForeignLeaders\",\"Underdog\",\"PositiveFlagsLogos\",\"NegativeFlagsLogos\",\"ChinaMap\",\"Gallery\",\"Building\",\"SpecialItems\"],\"porn\":[\"Sexuality\",\"ObsceneBehaviour\",\"SexProducts\"],\"terror\":[\"Firearms\",\"LargeWeapons\",\"ColdWeapons\",\"CrowdGathering\",\"BloodyScenes\",\"FireExplosion\",\"TerrorismActs\",\"Uniforms\",\"SpecialDress\",\"ViolentLogos\"]},\"service_config\":{\"callback_info\":{},\"codec_info\":{\"image_frequency\":10}},\"ignore_word_conf\":{\"model_disable\":false,\"rule_disable\":false,\"keyword_disable\":false},\"user_text_libs\":[]}"
                        }
                    ]
                }
            ]
        },
        "RequestId": "0b370345-f1b7-4fc3-a635-93032ac540c2"
    }
}
```

