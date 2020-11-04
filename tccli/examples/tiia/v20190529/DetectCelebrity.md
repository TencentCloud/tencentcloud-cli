**Example 1: 单个公众人物识别示例**



Input: 

```
tccli tiia DetectCelebrity --cli-unfold-argument  \
    --ImageUrl https://n.sinaimg.cn/sinacn/20171026/52e7-fynhhay5373192.jpg
```

Output: 
```
{
    "Response": {
        "Faces": [
            {
                "Name": "程潇",
                "Labels": [
                    {
                        "FirstLabel": "娱乐明星",
                        "SecondLabel": "歌手"
                    }
                ],
                "BasicInfo": "中国女歌手",
                "ID": "70004506",
                "Confidence": 61,
                "X": 163,
                "Y": 192,
                "Width": 96,
                "Height": 122
            }
        ],
        "Threshold": {
            "FalseRate1Percent": 80,
            "FalseRate5Permil": 85,
            "FalseRate1Permil": 90
        },
        "RequestId": "393fa9e0-3827-4183-9fe7-68ed622028a1"
    }
}
```

**Example 2: 图片中无人脸示例**



Input: 

```
tccli tiia DetectCelebrity --cli-unfold-argument  \
    --ImageUrl http://a.hiphotos.baidu.com/image/pic/item/e61190ef76c6a7efcefee3c3f3faaf51f2de667e.jpg
```

Output: 
```
{
    "Response": {
        "Faces": [],
        "Threshold": null,
        "RequestId": "fa73f07f-ecc8-48be-ada1-9534b64089b9"
    }
}
```

**Example 3: 多个公众人物识别示例**



Input: 

```
tccli tiia DetectCelebrity --cli-unfold-argument  \
    --ImageUrl https://detectproduct-1253284268.cos.ap-guangzhou.myqcloud.com/6b3c4866af0c03c6a87ff4c6a016e28b.jpg
```

Output: 
```
{
    "Response": {
        "Faces": [
            {
                "Name": "吕凉",
                "Labels": [
                    {
                        "FirstLabel": "娱乐明星",
                        "SecondLabel": "影视明星"
                    }
                ],
                "BasicInfo": "中国男演员",
                "ID": "30058074",
                "Confidence": 100,
                "X": 58,
                "Y": 56,
                "Width": 60,
                "Height": 73
            },
            {
                "Name": "胡歌",
                "Labels": [
                    {
                        "FirstLabel": "娱乐明星",
                        "SecondLabel": "影视明星"
                    }
                ],
                "BasicInfo": "中国男演员",
                "ID": "40001288",
                "Confidence": 100,
                "X": 177,
                "Y": 46,
                "Width": 52,
                "Height": 68
            },
            {
                "Name": "许亚军",
                "Labels": [
                    {
                        "FirstLabel": "娱乐明星",
                        "SecondLabel": "影视明星"
                    }
                ],
                "BasicInfo": "中国男演员",
                "ID": "19992439",
                "Confidence": 100,
                "X": 282,
                "Y": 64,
                "Width": 52,
                "Height": 66
            },
            {
                "Name": "韩东君",
                "Labels": [
                    {
                        "FirstLabel": "娱乐明星",
                        "SecondLabel": "影视明星"
                    },
                    {
                        "FirstLabel": "体育明星",
                        "SecondLabel": "赛车"
                    }
                ],
                "BasicInfo": "中国男演员、赛车手",
                "ID": "40007144",
                "Confidence": 97,
                "X": 382,
                "Y": 37,
                "Width": 55,
                "Height": 72
            }
        ],
        "Threshold": {
            "FalseRate1Percent": 80,
            "FalseRate5Permil": 85,
            "FalseRate1Permil": 90
        },
        "RequestId": "866f3d73-ead9-409a-9848-164d8d4e059c"
    }
}
```

