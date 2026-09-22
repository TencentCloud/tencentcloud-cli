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
    --AuditTemplate.SceneInfos.0.BizInfos.0.StrategyConfig {...转义JSON字符串：ability/asr_text_labels/audio_labels/user_text_libs/ignore_word_conf...} \
    --AuditTemplate.SceneInfos.0.BizInfos.1.BizType  \
    --AuditTemplate.SceneInfos.0.BizInfos.1.Status True \
    --AuditTemplate.SceneInfos.0.BizInfos.1.StrategyType Image \
    --AuditTemplate.SceneInfos.0.BizInfos.1.StrategyConfig {...转义JSON字符串：ability/image_labels/ignore_word_conf...} \
    --AuditTemplate.SceneInfos.0.BizInfos.2.BizType  \
    --AuditTemplate.SceneInfos.0.BizInfos.2.Status True \
    --AuditTemplate.SceneInfos.0.BizInfos.2.StrategyType Text \
    --AuditTemplate.SceneInfos.0.BizInfos.2.StrategyConfig {...转义JSON字符串：ability/text_labels/user_text_libs/ignore_word_conf...}
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

