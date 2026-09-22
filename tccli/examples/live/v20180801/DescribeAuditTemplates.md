**Example 1: DescribeAuditTemplates**



Input: 

```
tccli live DescribeAuditTemplates --cli-unfold-argument  \
    --WithTextAudit False \
    --PageNum 1 \
    --PageSize 10
```

Output: 
```
{
    "Response": {
        "AuditTemplates": [
            {
                "AudioInterval": 15,
                "AuditAudio": false,
                "AuditImage": true,
                "AuditText": 0,
                "CosBucket": "2",
                "CosFilePath": "/Audit/{Year}-{Month}-{Day}/{StreamID}-Audit-{Hour}-{Minute}-{Second}{Ext}",
                "CosRegion": "ap-guangzhou",
                "Description": "",
                "EnableFailoverCos": false,
                "FailoverCosBucket": "",
                "FailoverCosRegion": "",
                "SceneInfos": [
                    {
                        "BizInfos": [
                            {
                                "BizType": "1_1_7_8390211",
                                "Status": true,
                                "StrategyConfig": "{\"ability\":{\"asr_text\":true,\"audio\":true},\"service_config\":{\"callback_info\":{},\"codec_info\":{}},\"ignore_word_conf\":{\"model_disable\":false,\"rule_disable\":false,\"keyword_disable\":false},\"user_text_libs\":[]}",
                                "StrategyType": "ShortAudio"
                            }
                        ],
                        "SceneID": "LiveAudit"
                    }
                ],
                "SnapshotInterval": 2,
                "TemplateId": 8390211,
                "TemplateName": "qwe"
            }
        ],
        "RequestId": "23171f70-25d8-4c72-9342-51439526af6d"
    }
}
```

