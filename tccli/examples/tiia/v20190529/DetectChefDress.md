**Example 1: 厨师穿戴识别请求成功**



Input: 

```
tccli tiia DetectChefDress --cli-unfold-argument  \
    --ImageUrl https://test.jpg
```

Output: 
```
{
    "Response": {
        "Bodies": [
            {
                "Attributes": [
                    {
                        "Confidence": 0.6875998,
                        "Label": "无厨师服",
                        "Name": "厨师服识别"
                    },
                    {
                        "Confidence": 0.6875998,
                        "Label": "无厨师服",
                        "Name": "厨师服识别(酒店版)"
                    },
                    {
                        "Confidence": 0.9608861,
                        "Label": "无厨师帽",
                        "Name": "厨师帽识别"
                    },
                    {
                        "Confidence": 0,
                        "Label": "被优选过滤",
                        "Name": "口罩识别"
                    },
                    {
                        "Confidence": 0.99437755,
                        "Label": "赤膊",
                        "Name": "赤膊识别"
                    }
                ],
                "DetectConfidence": 0.914,
                "Rect": {
                    "Height": 1110,
                    "Width": 440,
                    "X": 217,
                    "Y": 79
                }
            }
        ],
        "RequestId": "a9050291-41a7-48ca-bd94-7a2a25d1d466"
    }
}
```

**Example 2: 厨师穿戴识别请求失败**



Input: 

```
tccli tiia DetectChefDress --cli-unfold-argument  \
    --ImageUrl https://123.jpg
```

Output: 
```
{
    "Response": {
        "RequestId": "a169390a-6ff3-4c42-ad25-a7858c35e576"
    }
}
```

