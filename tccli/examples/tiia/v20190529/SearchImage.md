**Example 1: 调用成功示例**



Input: 

```
tccli tiia SearchImage --cli-unfold-argument  \
    --ImageUrl https://liudhu-9527.cos.ap-guangzhou.myqcloud.com/input.jpeg \
    --Filter value > 10 \
    --MatchThreshold 1 \
    --Limit 30 \
    --Offset 0 \
    --GroupId work
```

Output: 
```
{
    "Response": {
        "Count": 1,
        "ImageInfos": [
            {
                "CustomContent": "",
                "EntityId": "work-1",
                "PicName": "work-1-1",
                "Score": 100,
                "Tags": "{\"my_tag\": \"1\"}"
            }
        ],
        "Object": {
            "AllBox": [
                {
                    "CategoryId": 0,
                    "Rect": {
                        "Height": 268,
                        "Width": 193,
                        "X": 278,
                        "Y": 162
                    },
                    "Score": 60
                },
                {
                    "CategoryId": 4,
                    "Rect": {
                        "Height": 138,
                        "Width": 132,
                        "X": 337,
                        "Y": 1053
                    },
                    "Score": 78
                },
                {
                    "CategoryId": 5,
                    "Rect": {
                        "Height": 31,
                        "Width": 83,
                        "X": 356,
                        "Y": 135
                    },
                    "Score": 27
                }
            ],
            "Attributes": [
                {
                    "Details": "渐层",
                    "Type": "图案"
                },
                {
                    "Details": "街头",
                    "Type": "风格"
                },
                {
                    "Details": "灰色",
                    "Type": "颜色"
                },
                {
                    "Details": "尼龙",
                    "Type": "材质"
                },
                {
                    "Details": "连帽",
                    "Type": "颈线设计"
                },
                {
                    "Details": "男装",
                    "Type": "类型"
                },
                {
                    "Details": "加长款",
                    "Type": "衣长"
                },
                {
                    "Details": "连衣裤",
                    "Type": "类别"
                }
            ],
            "Box": {
                "CategoryId": 0,
                "Rect": {
                    "Height": 268,
                    "Width": 193,
                    "X": 278,
                    "Y": 162
                },
                "Score": 60
            },
            "CategoryId": 0,
            "Colors": [
                {
                    "Color": "293133",
                    "Label": "Black-darkgrey",
                    "Percentage": 10
                },
                {
                    "Color": "4A3D46",
                    "Label": "Black-grapethistle",
                    "Percentage": 8
                },
                {
                    "Color": "808080",
                    "Label": "Gray-gray",
                    "Percentage": 7
                },
                {
                    "Color": "555555",
                    "Label": "Blue-ebony",
                    "Percentage": 6
                }
            ]
        },
        "RequestId": "7ddbbc94-1adc-45f7-a114-8fdebaabf6d4"
    }
}
```

