**Example 1: 请求示例**

请求示例。

Input: 

```
tccli live CreateAuditTemplate --cli-unfold-argument  \
    --AuditTemplate.TemplateName appjirtp7tb2397的策略 \
    --AuditTemplate.Description appjirtp7tb2397的策略 \
    --AuditTemplate.TemplateId 0 \
    --AuditTemplate.AuditAudio True \
    --AuditTemplate.AuditImage False \
    --AuditTemplate.AudioInterval 15 \
    --AuditTemplate.SnapshotInterval 2 \
    --AuditTemplate.CosBucket live-resource \
    --AuditTemplate.CosRegion ap-shanghai \
    --AuditTemplate.CosFilePath /Audit/{Year}-{Month}-{Day}/{StreamID}-Audit-{Hour}-{Minute}-{Second}{Ext} \
    --AuditTemplate.EnableFailoverCos False \
    --AuditTemplate.FailoverCosBucket 1 \
    --AuditTemplate.FailoverCosRegion 1 \
    --AuditTemplate.SceneInfos.0.SceneID LiveAudit \
    --AuditTemplate.SceneInfos.0.BizInfos.0.BizType  \
    --AuditTemplate.SceneInfos.0.BizInfos.0.Status True \
    --AuditTemplate.SceneInfos.0.BizInfos.0.StrategyType ShortAudio \
    --AuditTemplate.SceneInfos.0.BizInfos.0.StrategyConfig {"ability":{"asr_text":true,"audio":true},"asr_text_labels":{"abuse":["AbuseSeverely","MildAbuse"],"ad":["FinancialAdvertising"],"illegal":["SensitiveSong","Contraband","ProhibitedBehavior","IllegalGroups"],"polity":["PositiveContent","NegativeContent"],"porn":["OVR","Pornography","PornographyObscene"],"terror":["TerroristOrganizations","ViolentAndBloody","Weapon"]},"audio_labels":{"moan":["OVR"]},"ignore_word_conf":{"keyword_disable":false,"model_disable":false,"rule_disable":false},"user_text_libs":["8ca1865e-eabb-4d54-9d58-f70654f963ce"]} \
    --AuditTemplate.SceneInfos.0.BizInfos.1.BizType  \
    --AuditTemplate.SceneInfos.0.BizInfos.1.Status True \
    --AuditTemplate.SceneInfos.0.BizInfos.1.StrategyType Image \
    --AuditTemplate.SceneInfos.0.BizInfos.1.StrategyConfig {"ability":{"image":true,"ocr_text":true},"image_labels":{"ad":["QRCode","LOGO"],"illegal":["Delinquenent","NonMainstream","Illegal","Contraband","PersonalPrivacy","Nausea"],"polity":["PositiveCharacter","NegativeFigure","ForeignLeaders","Underdog","PositiveFlagsLogos","NegativeFlagsLogos","ChinaMap","Gallery","Building","SpecialItems"],"porn":["Sexuality","ObsceneBehaviour","SexProducts"],"terror":["Firearms","LargeWeapons","ColdWeapons","CrowdGathering","BloodyScenes","FireExplosion","TerrorismActs","Uniforms","SpecialDress","ViolentLogos"]},"ignore_word_conf":{"model_disable":false,"rule_disable":false,"keyword_disable":false}} \
    --AuditTemplate.SceneInfos.0.BizInfos.2.BizType  \
    --AuditTemplate.SceneInfos.0.BizInfos.2.Status True \
    --AuditTemplate.SceneInfos.0.BizInfos.2.StrategyType Text \
    --AuditTemplate.SceneInfos.0.BizInfos.2.StrategyConfig {"ability":{"text":true},"ignore_word_conf":{"keyword_disable":false,"model_disable":false,"rule_disable":false},"text_labels":{"abuse":[],"ad":[],"illegal":[],"polity":[],"porn":[],"terror":[]},"user_text_libs":["8ca1865e-eabb-4d54-9d58-f70654f963ce"]}
```

Output: 
```
{
    "Response": {
        "RequestId": "0d98ffdb-3d3e-4a72-94dc-3d6b2a97df54",
        "TemplateId": 55199
    }
}
```

