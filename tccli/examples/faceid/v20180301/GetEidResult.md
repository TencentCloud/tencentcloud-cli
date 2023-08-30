**Example 1: 获取所有类型的信息**



Input: 

```
tccli faceid GetEidResult --cli-unfold-argument  \
    --InfoType 1 \
    --EidToken CE661F1A-0F1E-45BD-BE13-34C05CEA7681
```

Output: 
```
{
    "Response": {
        "Text": {
            "ErrCode": 0,
            "ErrMsg": "成功",
            "IdCard": "",
            "Name": "",
            "UseIDType": 1,
            "OcrNation": null,
            "OcrAddress": null,
            "OcrBirth": null,
            "OcrAuthority": null,
            "OcrValidDate": null,
            "OcrName": "爱新觉罗永琪",
            "OcrIdCard": "440111111111111111",
            "OcrGender": null,
            "IdInfoFrom": "abc",
            "LiveStatus": 0,
            "LiveMsg": "成功",
            "Comparestatus": 0,
            "Comparemsg": "成功",
            "CompareLibType": "abc",
            "Sim": "76.52",
            "Location": null,
            "Mobile": "13800000000",
            "Extra": "",
            "LivenessDetail": [
                {
                    "ReqTime": "1577179388135",
                    "Seq": "3d12da91-db34-4e55-81c3-993a41d7ccb7",
                    "Idcard": "",
                    "Name": "",
                    "CompareLibType": "公安商业库",
                    "Sim": "76.52",
                    "IsNeedCharge": true,
                    "Errcode": 0,
                    "Errmsg": "成功",
                    "Livestatus": 0,
                    "Livemsg": "成功",
                    "LivenessMode": 1,
                    "Comparestatus": 0,
                    "Comparemsg": "成功"
                }
            ],
            "LivenessMode": 1,
            "NFCRequestIds": [
                "abc"
            ],
            "NFCBillingCounts": 0,
            "PassNo": "abc",
            "VisaNum": "abc"
        },
        "IdCardData": {
            "ProcessedBackImage": "base64",
            "ProcessedFrontImage": "base64",
            "OcrFront": "base64",
            "OcrBack": "base64",
            "Avatar": "base64",
            "WarnInfos": [
                0
            ],
            "BackWarnInfos": [
                0
            ]
        },
        "BestFrame": {
            "BestFrame": "base64",
            "BestFrames": [
                "base64"
            ]
        },
        "IntentionVerifyData": {
            "IntentionVerifyVideo": "base64",
            "ErrorCode": 0,
            "ErrorMessage": "成功",
            "AsrResult": "",
            "IntentionVerifyBestFrame": "base64",
            "AsrResultSimilarity": "0"
        },
        "EidInfo": {
            "EidCode": "",
            "EidSign": "",
            "DesKey": "",
            "UserInfo": ""
        },
        "IntentionQuestionResult": {
            "ScreenShot": [
                "base64"
            ],
            "FinalResultCode": "0",
            "AsrResult": [
                ""
            ],
            "Audios": [
                "base64"
            ],
            "Video": "base64",
            "FinalResultDetailCode": 0,
            "FinalResultMessage": "Success",
            "ResultCode": [
                ""
            ]
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
        "RequestId": "f52bac9a-0aee-4fe6-8d34-7de4bce89473"
    }
}
```

