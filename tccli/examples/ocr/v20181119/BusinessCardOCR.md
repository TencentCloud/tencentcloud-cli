**Example 1: BusinessCardOCR调用**



Input: 

```
tccli ocr BusinessCardOCR --cli-unfold-argument  \
    --ImageUrl https://ocr-demo-1254418846.cos.ap-guangzhou.myqcloud.com/card/BusinessCardOCR/BusinessCardOCR1.jpg
```

Output: 
```
{
    "Response": {
        "Angle": 0,
        "BusinessCardInfos": [
            {
                "ItemCoord": {
                    "Height": 36,
                    "Width": 67,
                    "X": 68,
                    "Y": 47
                },
                "Name": "姓名",
                "Value": "李明"
            },
            {
                "ItemCoord": {
                    "Height": 23,
                    "Width": 201,
                    "X": 67,
                    "Y": 103
                },
                "Name": "职位",
                "Value": "优图研发中心工程师"
            },
            {
                "ItemCoord": {
                    "Height": 22,
                    "Width": 379,
                    "X": 103,
                    "Y": 302
                },
                "Name": "地址",
                "Value": "上海市徐汇区田林路397号腾云大厦6F"
            },
            {
                "ItemCoord": {
                    "Height": 21,
                    "Width": 184,
                    "X": 290,
                    "Y": 270
                },
                "Name": "邮箱",
                "Value": "abc8888@qq.com"
            },
            {
                "ItemCoord": {
                    "Height": 23,
                    "Width": 226,
                    "X": 118,
                    "Y": 233
                },
                "Name": "手机",
                "Value": "+86-185-8907-2228"
            },
            {
                "ItemCoord": {
                    "Height": 21,
                    "Width": 101,
                    "X": 93,
                    "Y": 268
                },
                "Name": "QQ",
                "Value": "888888"
            }
        ],
        "RequestId": "83b207b2-b5e4-4084-b3fe-f9018d58bef0",
        "RetImageBase64": ""
    }
}
```

