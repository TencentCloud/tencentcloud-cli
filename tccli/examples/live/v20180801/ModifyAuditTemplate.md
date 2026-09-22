**Example 1: 请求示例**

请求示例。

Input: 

```
tccli live ModifyAuditTemplate --cli-unfold-argument  \
    --AuditTemplate.TemplateId 55514 \
    --AuditTemplate.TemplateName 直播审核_test \
    --AuditTemplate.Description 直播审核_test \
    --AuditTemplate.AuditImage True \
    --AuditTemplate.AuditAudio True \
    --AuditTemplate.AuditText 1 \
    --AuditTemplate.SnapshotInterval 50 \
    --AuditTemplate.AudioInterval 30 \
    --AuditTemplate.CosBucket live-test \
    --AuditTemplate.CosRegion ap-shanghai \
    --AuditTemplate.CosFilePath /Audit/{Year}-{Month}-{Day}/{StreamID}-Audit-{Hour}-{Minute}-{Second}{Ext} \
    --AuditTemplate.EnableFailoverCos False \
    --AuditTemplate.SceneInfos.0.BizInfos.0.BizType 1_1_7_55514 \
    --AuditTemplate.SceneInfos.0.BizInfos.0.Status True \
    --AuditTemplate.SceneInfos.0.BizInfos.0.StrategyType ShortAudio \
    --AuditTemplate.SceneInfos.0.BizInfos.0.StrategyConfig {"ability":{"asr_text":true,"audio":true},"asr_text_labels":{"ad":["AdvertisingDiversion","FinancialAdvertising"]},"audio_labels":{},"user_text_libs":["0fd0600e-0603-41e8-a985-ae49a73fbe9f"]} \
    --AuditTemplate.SceneInfos.0.BizInfos.1.BizType 1_1_2_55514 \
    --AuditTemplate.SceneInfos.0.BizInfos.1.Status True \
    --AuditTemplate.SceneInfos.0.BizInfos.1.StrategyType Image \
    --AuditTemplate.SceneInfos.0.BizInfos.1.StrategyConfig {"ability":{"image":true,"ocr_text":true},"ocr_text_labels":{"ad":["AdvertisingDiversion","FinancialAdvertising"]},"image_labels":{"illegal":["Delinquenent","NonMainstream","Illegal","Contraband","PersonalPrivacy","Nausea"],"ad":["QRCode","LOGO"]},"user_text_libs":["0fd0600e-0603-41e8-a985-ae49a73fbe9f"]} \
    --AuditTemplate.SceneInfos.0.BizInfos.2.BizType 1_1_1_55514 \
    --AuditTemplate.SceneInfos.0.BizInfos.2.Status True \
    --AuditTemplate.SceneInfos.0.BizInfos.2.StrategyType Text \
    --AuditTemplate.SceneInfos.0.BizInfos.2.StrategyConfig {"ability":{"text":true},"ignore_word_conf":{"keyword_disable":false,"model_disable":false,"rule_disable":false},"text_labels":{"ad":["AdvertisingDiversion","FinancialAdvertising"]},"user_text_libs":["0fd0600e-0603-41e8-a985-ae49a73fbe9f"]}
```

Output: 
```
{
    "Response": {
        "RequestId": "e91114bc-9075-4d8e-a35f-d914ddf9cb39",
        "TemplateId": 55514
    }
}
```

