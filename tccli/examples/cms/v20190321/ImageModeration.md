**Example 1: 图片内容检测**

审核结果

Input: 

```
tccli cms ImageModeration --cli-unfold-argument  \
    --FileMD5 字符串型 \
    --FileContent 字符串型 \
    --FileUrl https://xxx.jpg
```

Output: 
```
{
    "Response": {
        "BusinessCode": 0,
        "Data": {
            "EvilFlag": 0,
            "EvilType": 100,
            "CodeDetect": {
                "ModerationCode": 0,
                "ModerationDetail": [
                    {
                        "StrCharset": "UTF-8",
                        "QrCodePosition": [
                            {
                                "FloatX": 5.8333335,
                                "FloatY": 314.16666
                            },
                            {
                                "FloatX": 5.8333335,
                                "FloatY": 5.8333335
                            },
                            {
                                "FloatX": 314.16666,
                                "FloatY": 5.8333335
                            },
                            {
                                "FloatX": 314.16666,
                                "FloatY": 314.16666
                            }
                        ],
                        "StrQrCodeText": "http://xxx",
                        "Uint32QrCodeType": 2
                    }
                ]
            },
            "HotDetect": {
                "EvilType": 100,
                "HitFlag": 0,
                "Keywords": [],
                "Labels": [],
                "Score": 0
            },
            "IllegalDetect": {
                "EvilType": 100,
                "HitFlag": 0,
                "Keywords": [],
                "Labels": [],
                "Score": 0
            },
            "OCRDetect": {
                "TextInfo": ""
            },
            "PolityDetect": {
                "EvilType": 100,
                "FaceNames": [],
                "HitFlag": 0,
                "Keywords": [],
                "PolityItems": [],
                "Score": 0
            },
            "PornDetect": {
                "EvilType": 100,
                "HitFlag": 0,
                "Keywords": [],
                "Labels": [],
                "Score": 0
            },
            "Similar": {
                "EvilType": 100,
                "HitFlag": 0,
                "SeedUrl": ""
            },
            "TerrorDetect": {
                "EvilType": 100,
                "HitFlag": 0,
                "Keywords": [],
                "Labels": [],
                "Score": 0
            }
        },
        "RequestId": "57937de8-84a6-452d-b723-0cb6dad0dd1e"
    },
    "retcode": 0,
    "retmsg": "ok"
}
```

