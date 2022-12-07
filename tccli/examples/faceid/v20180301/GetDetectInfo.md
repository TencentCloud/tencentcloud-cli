**Example 1: 获取所有类型的信息**



Input: 

```
tccli faceid GetDetectInfo --cli-unfold-argument  \
    --InfoType 0 \
    --BizToken CE661F1A-0F1E-45BD-BE13-34C05CEA7681 \
    --RuleId 0
```

Output: 
```
{
    "Response": {
        "DetectInfo": "{\"Text\":{\"ErrCode\":null,\"ErrMsg\":null,\"IdCard\":\"\",\"Name\":\"\",\"OcrNation\":null,\"OcrAddress\":null,\"OcrBirth\":null,\"OcrAuthority\":null,\"OcrValidDate\":null,\"OcrName\":null,\"OcrIdCard\":null,\"OcrGender\":null,\"LiveStatus\":null,\"LiveMsg\":null,\"Comparestatus\":null,\"Comparemsg\":null,\"Extra\":\"\",\"Detail\":{\"LivenessData\":[]}},\"IdCardData\":{\"OcrFront\":null,\"OcrBack\":null},\"BestFrame\":{\"BestFrame\":null},\"VideoData\":{\"LivenessVideo\":null}}",
        "RequestId": "0f96cf39-a183-485c-ab29-8427ab81f9ae"
    }
}
```

**Example 2: 仅获取文本与身份证照片类型的信息**



Input: 

```
tccli faceid GetDetectInfo --cli-unfold-argument  \
    --InfoType 12 \
    --BizToken CE661F1A-0F1E-45BD-BE13-34C05CEA7681 \
    --RuleId 0
```

Output: 
```
{
    "Response": {
        "DetectInfo": "{\"Text\":{\"ErrCode\":null,\"ErrMsg\":null,\"IdCard\":\"\",\"Name\":\"\",\"OcrNation\":null,\"OcrAddress\":null,\"OcrBirth\":null,\"OcrAuthority\":null,\"OcrValidDate\":null,\"OcrName\":null,\"OcrIdCard\":null,\"OcrGender\":null,\"LiveStatus\":null,\"LiveMsg\":null,\"Comparestatus\":null,\"Comparemsg\":null,\"Extra\":\"\",\"Detail\":{\"LivenessData\":[]}},\"IdCardData\":{\"OcrFront\":null,\"OcrBack\":null}}",
        "RequestId": "7be0c0e4-57f5-44c4-b471-21390ca88fb2"
    }
}
```

