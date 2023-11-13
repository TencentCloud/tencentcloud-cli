**Example 1: 获取所有类型的信息**



Input: 

```
tccli faceid GetDetectInfoEnhanced --cli-unfold-argument  \
    --InfoType 1 \
    --BizToken CE661F1A-0F1E-45BD-BE13-34C05CEA7681 \
    --RuleId 0
```

Output: 
```
{
    "Response": {
        "Text": {
            "ErrCode": 0,
            "ErrMsg": "成功",
            "UseIDType": 0,
            "IdCard": "440111111111111111",
            "Name": "爱新觉罗永琪",
            "OcrNation": null,
            "OcrAddress": null,
            "OcrBirth": null,
            "OcrAuthority": null,
            "OcrValidDate": null,
            "OcrName": "爱新觉罗永琪",
            "OcrIdCard": "440111111111111111",
            "OcrGender": null,
            "IdInfoFrom": "abc",
            "LivenessMode": 0,
            "LiveStatus": 0,
            "LiveMsg": "成功",
            "Comparestatus": 0,
            "Comparemsg": "成功",
            "CompareLibType": "权威库",
            "Sim": "76.52",
            "Location": null,
            "Mobile": null,
            "Extra": "",
            "NFCRequestIds": [
                "abc"
            ],
            "NFCBillingCounts": 0,
            "PassNo": "abc",
            "VisaNum": "abc",
            "LivenessDetail": [
                {
                    "ReqTime": "1577179388135",
                    "Seq": "3d12da91-db34-4e55-81c3-993a41d7ccb7",
                    "Idcard": "440111111111111111",
                    "Name": "爱新觉罗永琪",
                    "CompareLibType": "权威库",
                    "Sim": "76.52",
                    "IsNeedCharge": true,
                    "Errcode": 0,
                    "Errmsg": "成功",
                    "LivenessMode": 0,
                    "Livestatus": 0,
                    "Livemsg": "成功",
                    "Comparestatus": 0,
                    "Comparemsg": "成功"
                }
            ]
        },
        "IdCardData": {
            "ProcessedBackImage": "base64",
            "ProcessedFrontImage": "base64",
            "OcrFront": "base64",
            "OcrBack": "base64",
            "Avatar": "base64",
            "WarnInfos": [],
            "BackWarnInfos": []
        },
        "IntentionVerifyData": {
            "IntentionVerifyVideo": "base64",
            "ErrorCode": 0,
            "ErrorMessage": "成功",
            "AsrResult": "同意",
            "AsrResultSimilarity": "0",
            "IntentionVerifyBestFrame": "base64"
        },
        "IntentionActionResult": {
            "FinalResultDetailCode": 0,
            "FinalResultMessage": "abc",
            "Details": [
                {
                    "Video": "abc",
                    "ScreenShot": [
                        "abc"
                    ]
                }
            ]
        },
        "IntentionQuestionResult": {
            "FinalResultDetailCode": 0,
            "FinalResultMessage": "abc",
            "AsrResult": [
                "同意"
            ],
            "ResultCode": [
                "0"
            ],
            "Audios": [
                "base64"
            ],
            "Video": "base64",
            "ScreenShot": [
                "base64"
            ],
            "FinalResultCode": "0"
        },
        "BestFrame": {
            "BestFrame": "base64",
            "BestFrames": [
                "base64"
            ]
        },
        "VideoData": {
            "LivenessVideo": "base64"
        },
        "Encryption": {
            "Iv": "iv",
            "EncryptList": [
                "Response.Text.Name"
            ],
            "CiphertextBlob": "CiphertextBlob"
        },
        "EncryptedBody": "abc",
        "RequestId": "f52bac9a-0aee-4fe6-8d34-7de4bce89473"
    }
}
```

