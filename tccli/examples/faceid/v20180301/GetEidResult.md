**Example 1: 获取E证通结果信息成功示例**

成功获取E证通结果信息。

Input: 

```
tccli faceid GetEidResult --cli-unfold-argument  \
    --InfoType 1 \
    --EidToken CE661F1A-0F1E-45BD-BE133-34C05CEA76812
```

Output: 
```
{
    "Response": {
        "BestFrame": {
            "BestFrame": "/9j/4AAQSk...UVoYn/2Q==",
            "BestFrames": [
                "/9j/4AAQSk...AT/U//2Q=="
            ]
        },
        "EidInfo": {
            "DesKey": "",
            "EidCode": "OMKhJ5hkbPnA5PKGrzD1oKZ/e8W9w2g1yAOUIry7G/4xMDAw",
            "EidSign": "MEQCIDt0Xa...YygK4Fhw==",
            "UserInfo": ""
        },
        "IdCardData": {
            "Avatar": "",
            "BackWarnInfos": null,
            "OcrBack": "",
            "OcrFront": "",
            "ProcessedBackImage": "",
            "ProcessedFrontImage": "",
            "WarnInfos": null
        },
        "IntentionActionResult": null,
        "IntentionQuestionResult": {
            "AsrResult": null,
            "Audios": null,
            "FinalResultCode": "",
            "FinalResultDetailCode": null,
            "FinalResultMessage": null,
            "ResultCode": null,
            "ScreenShot": null,
            "Video": ""
        },
        "IntentionVerifyData": {
            "AsrResult": "",
            "AsrResultSimilarity": "",
            "ErrorCode": 0,
            "ErrorMessage": "",
            "IntentionVerifyBestFrame": "",
            "IntentionVerifyVideo": ""
        },
        "RequestId": "29a30ec8-0c15-4566-a5ab-99f88a3f0821",
        "Text": {
            "CompareLibType": "权威库",
            "Comparemsg": "成功",
            "Comparestatus": 0,
            "ErrCode": 0,
            "ErrMsg": "成功",
            "Extra": "",
            "IdCard": "",
            "IdInfoFrom": "其他",
            "LiveMsg": "成功",
            "LiveStatus": 0,
            "LivenessInfoTag": [
                "01"
            ],
            "LivenessDetail": [
                {
                    "CompareLibType": "权威库",
                    "Comparemsg": "成功",
                    "Comparestatus": 0,
                    "Errcode": 0,
                    "Errmsg": "成功",
                    "Idcard": "",
                    "IsNeedCharge": true,
                    "Livemsg": "成功",
                    "LivenessMode": 4,
                    "Livestatus": 0,
                    "Name": "",
                    "ReqTime": "1730451371368",
                    "Seq": "092ff8ca-4d1c-4c2122-b513-ec8ced564c9a",
                    "Sim": "97.31"
                }
            ],
            "LivenessMode": 4,
            "Location": "",
            "Mobile": "",
            "NFCBillingCounts": 0,
            "NFCRequestIds": null,
            "Name": "",
            "OcrAddress": "",
            "OcrAuthority": "",
            "OcrBirth": "",
            "OcrGender": "",
            "OcrIdCard": "",
            "OcrName": "",
            "OcrNation": "",
            "OcrValidDate": "",
            "PassNo": "",
            "Sim": "97.31",
            "UseIDType": 0,
            "VisaNum": ""
        }
    }
}
```

**Example 2: 获取E证通结果信息失败示例**

获取E证通结果信息失败，传入过期BizToken。

Input: 

```
tccli faceid GetEidResult --cli-unfold-argument  \
    --InfoType 1 \
    --EidToken CE661F1A-0F1E-45B1D-BE133-34C05CEA76812
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "InvalidParameterValue.BizTokenExpired",
            "Message": "BizToken过期。"
        },
        "RequestId": "19f36e49-d419-48a7-b86a-edcb81e71909"
    }
}
```

