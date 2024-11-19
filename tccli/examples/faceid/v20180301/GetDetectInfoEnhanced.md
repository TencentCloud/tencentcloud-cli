**Example 1: 获取结果信息成功示例**



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
        "BestFrame": {
            "BestFrame": "/9j/4AAQSk...JKD2A//9k=",
            "BestFrames": [
                "/9j/4AAQSk...002dgP/9k=",
                "/9j/4AAQSk...vx+YH/2Q==",
                "/9j/4AAQSk...n6fj5Af//Z",
                "/9j/4AAQSk...dzlFFagf/Z"
            ]
        },
        "EncryptedBody": "",
        "Encryption": {
            "Algorithm": "",
            "CiphertextBlob": "",
            "EncryptList": [],
            "Iv": "",
            "TagList": []
        },
        "IdCardData": {
            "Avatar": null,
            "BackWarnInfos": null,
            "OcrBack": null,
            "OcrFront": null,
            "ProcessedBackImage": null,
            "ProcessedFrontImage": null,
            "WarnInfos": null
        },
        "IntentionActionResult": null,
        "IntentionQuestionResult": {
            "AsrResult": [],
            "Audios": [],
            "FinalResultCode": null,
            "FinalResultDetailCode": null,
            "FinalResultMessage": null,
            "ResultCode": [],
            "ScreenShot": [],
            "Video": null
        },
        "IntentionVerifyData": {
            "AsrResult": null,
            "AsrResultSimilarity": null,
            "ErrorCode": null,
            "ErrorMessage": null,
            "IntentionVerifyBestFrame": null,
            "IntentionVerifyVideo": null
        },
        "RequestId": "91173d84-e461-4da4-a270-2b8d48a2e136",
        "Text": {
            "CompareLibType": "权威库",
            "Comparemsg": "成功",
            "Comparestatus": 0,
            "ErrCode": 0,
            "ErrMsg": "成功",
            "Extra": "",
            "IdCard": "11204416541220243X",
            "IdInfoFrom": "其他",
            "LiveMsg": "成功",
            "LiveStatus": 0,
            "LivenessDetail": [
                {
                    "CompareLibType": "权威库",
                    "Comparemsg": "成功",
                    "Comparestatus": 0,
                    "Errcode": 0,
                    "Errmsg": "成功",
                    "Idcard": "11204416541220243X",
                    "IsNeedCharge": true,
                    "Livemsg": "成功",
                    "LivenessMode": 1,
                    "Livestatus": 0,
                    "Name": "韦小宝",
                    "ReqTime": "1730444265275",
                    "Seq": "1f330eea-f5db-4726-a7b4-38cdf1aefb02",
                    "Sim": "95.51"
                }
            ],
            "LivenessInfoTag": null,
            "LivenessMode": 1,
            "Location": null,
            "Mobile": "",
            "NFCBillingCounts": 0,
            "NFCRequestIds": [],
            "Name": "韦小宝",
            "OcrAddress": null,
            "OcrAuthority": null,
            "OcrBirth": null,
            "OcrGender": null,
            "OcrIdCard": "",
            "OcrName": "",
            "OcrNation": null,
            "OcrValidDate": null,
            "PassNo": null,
            "Sim": "95.51",
            "UseIDType": 0,
            "VisaNum": null
        },
        "VideoData": {
            "LivenessVideo": "AAAAGGZ0eX...VyYWxidW0h"
        }
    }
}
```

**Example 2: 获取结果信息失败示例**



Input: 

```
tccli faceid GetDetectInfoEnhanced --cli-unfold-argument  \
    --InfoType 2 \
    --BizToken 4237FAC9-1AE4-4954-B495-FB07D91141CA \
    --RuleId 0
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "InvalidParameter",
            "Message": "非法BizToken。"
        },
        "RequestId": "0832c071-0c3e-4a1f-b7d3-4910221a1e18"
    }
}
```

