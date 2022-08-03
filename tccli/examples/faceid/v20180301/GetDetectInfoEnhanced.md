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
            "LiveStatus": 0,
            "LiveMsg": "成功",
            "Comparestatus": 0,
            "Comparemsg": "成功",
            "CompareLibType": "xx",
            "Sim": "76.52",
            "Location": null,
            "Mobile": null,
            "Extra": "",
            "LivenessDetail": [
                {
                    "ReqTime": "1577179388135",
                    "Seq": "3d12da91-db34-4e55-81c3-993a41d7ccb7",
                    "Idcard": "440111111111111111",
                    "Name": "爱新觉罗永琪",
                    "CompareLibType": "xx",
                    "Sim": "76.52",
                    "IsNeedCharge": true,
                    "Errcode": 0,
                    "Errmsg": "成功",
                    "Livestatus": 0,
                    "Livemsg": "成功",
                    "Comparestatus": 0,
                    "Comparemsg": "成功"
                }
            ]
        },
        "IdCardData": {
            "ProcessedBackImage": "xx",
            "ProcessedFrontImage": "xx",
            "OcrFront": "xx",
            "OcrBack": "xx",
            "Avatar": "xx"
        },
        "IntentionVerifyData": {
            "IntentionVerifyVideo": "xx",
            "ErrorCode": 0,
            "ErrorMessage": "成功",
            "AsrResult": "xx",
            "IntentionVerifyBestFrame": "xx"
        },
        "IntentionQuestionResult": {
            "AsrResult": [
                "同意"
            ],
            "ResultCode": [
                "0"
            ],
            "Video": "xx",
            "ScreenShot": [
                "xx"
            ],
            "FinalResultCode": "0"
        },
        "BestFrame": {
            "BestFrame": "xx",
            "BestFrames": [
                "xx"
            ]
        },
        "VideoData": {
            "LivenessVideo": "xx"
        },
        "Encryption": {
            "Iv": "xx",
            "EncryptList": [
                "xx"
            ],
            "CiphertextBlob": "xx"
        },
        "RequestId": "f52bac9a-0aee-4fe6-8d34-7de4bce89473"
    }
}
```

