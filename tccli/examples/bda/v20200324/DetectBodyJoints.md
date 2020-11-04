**Example 1: 调用失败示例**



Input: 

```
tccli bda DetectBodyJoints --cli-unfold-argument  \
    --Url IamNotUrl
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "InvalidParameterValue.UrlIllegal",
            "Message": "URL格式不合法。"
        },
        "RequestId": "b5f77c78-efaf-42d1-b0ac-419cc70b4994"
    }
}
```

**Example 2: 调用成功示例**



Input: 

```
tccli bda DetectBodyJoints --cli-unfold-argument  \
    --Url test.jpg
```

Output: 
```
{
    "Response": {
        "BodyJointsResults": [
            {
                "BoundBox": {
                    "X": 134,
                    "Y": 169,
                    "Width": 270,
                    "Height": 486
                },
                "BodyJoints": [
                    {
                        "X": 233.458984375,
                        "Y": 212.494140625,
                        "KeyPointType": "头部"
                    },
                    {
                        "X": 237.619140625,
                        "Y": 249.935546875,
                        "KeyPointType": "颈部"
                    },
                    {
                        "X": 283.380859375,
                        "Y": 266.576171875,
                        "KeyPointType": "右肩"
                    },
                    {
                        "X": 324.982421875,
                        "Y": 308.177734375,
                        "KeyPointType": "右肘"
                    },
                    {
                        "X": 295.861328125,
                        "Y": 349.779296875,
                        "KeyPointType": "右腕"
                    },
                    {
                        "X": 208.498046875,
                        "Y": 274.896484375,
                        "KeyPointType": "左肩"
                    },
                    {
                        "X": 183.537109375,
                        "Y": 337.298828125,
                        "KeyPointType": "左肘"
                    },
                    {
                        "X": 158.576171875,
                        "Y": 387.220703125,
                        "KeyPointType": "左腕"
                    },
                    {
                        "X": 262.580078125,
                        "Y": 395.541015625,
                        "KeyPointType": "右髋"
                    },
                    {
                        "X": 237.619140625,
                        "Y": 466.263671875,
                        "KeyPointType": "右膝"
                    },
                    {
                        "X": 216.818359375,
                        "Y": 557.787109375,
                        "KeyPointType": "右踝"
                    },
                    {
                        "X": 254.259765625,
                        "Y": 399.701171875,
                        "KeyPointType": "左髋"
                    },
                    {
                        "X": 266.740234375,
                        "Y": 482.904296875,
                        "KeyPointType": "左膝"
                    },
                    {
                        "X": 349.943359375,
                        "Y": 545.306640625,
                        "KeyPointType": "左踝"
                    }
                ],
                "Confidence": 0.99999010562897
            }
        ],
        "RequestId": "97d85578-6b11-4e7c-beea-65601bc0bc04"
    }
}
```

