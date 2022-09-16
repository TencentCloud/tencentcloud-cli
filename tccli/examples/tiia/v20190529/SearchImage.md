**Example 1: 调用成功示例**



Input: 

```
tccli tiia SearchImage --cli-unfold-argument  \
    --ImageUrl http://test.com/1.jpg \
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
        "RequestId": "8bab9614-3f62-4b1d-bc9b-e773703c727e",
        "Count": 1,
        "ImageInfos": [
            {
                "EntityId": "test1",
                "PicName": "test2",
                "Score": 100,
                "CustomContent": "",
                "Tags": "{}"
            }
        ],
        "Object": {
            "Box": {
                "Rect": {
                    "Width": 447,
                    "Height": 816,
                    "X": 88,
                    "Y": 264
                },
                "Score": 53
            },
            "Colors": [
                {
                    "Color": "0A0A0A",
                    "Percentage": 15,
                    "Label": "Black-black"
                },
                {
                    "Color": "8B4513",
                    "Percentage": 11,
                    "Label": "Brown-saddlebrown"
                },
                {
                    "Percentage": 7,
                    "Label": "Yellow-khaki",
                    "Color": "D8C59D"
                },
                {
                    "Label": "Yellow-darkkhaki",
                    "Color": "BDB76B",
                    "Percentage": 6
                }
            ],
            "CategoryId": 5,
            "Attributes": []
        }
    }
}
```

