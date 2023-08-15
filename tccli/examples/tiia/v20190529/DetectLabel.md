**Example 1: 图像标签检测请求成功**



Input: 

```
tccli tiia DetectLabel --cli-unfold-argument  \
    --ImageUrl https://test.jpg \
    --Scenes WEB CAMERA ALBUM
```

Output: 
```
{
    "Response": {
        "NewsLabels": [
            {
                "Confidence": 80,
                "Name": "塔楼",
                "SecondCategory": "建筑",
                "FirstCategory": "场景"
            }
        ],
        "Labels": [
            {
                "Name": "塔楼",
                "FirstCategory": "场景",
                "SecondCategory": "建筑",
                "Confidence": 81
            },
            {
                "Name": "夜晚",
                "FirstCategory": "场景",
                "SecondCategory": "自然风光",
                "Confidence": 79
            },
            {
                "Name": "天际线",
                "FirstCategory": "场景",
                "SecondCategory": "自然风光",
                "Confidence": 77
            },
            {
                "Name": "城市景观",
                "FirstCategory": "场景",
                "SecondCategory": "其他",
                "Confidence": 77
            },
            {
                "Name": "城市",
                "FirstCategory": "场景",
                "SecondCategory": "生活/娱乐场所",
                "Confidence": 72
            },
            {
                "Name": "都市",
                "FirstCategory": "场景",
                "SecondCategory": "其他",
                "Confidence": 69
            }
        ],
        "CameraLabels": [
            {
                "Name": "夜景",
                "FirstCategory": "场景",
                "SecondCategory": "自然风光",
                "Confidence": 92
            },
            {
                "Name": "城市",
                "FirstCategory": "场景",
                "SecondCategory": "建筑",
                "Confidence": 3
            },
            {
                "Name": "游乐园",
                "FirstCategory": "场景",
                "SecondCategory": "生活/娱乐场所",
                "Confidence": 2
            },
            {
                "Name": "大厦",
                "FirstCategory": "场景",
                "SecondCategory": "建筑",
                "Confidence": 1
            },
            {
                "Name": "桥",
                "FirstCategory": "场景",
                "SecondCategory": "建筑",
                "Confidence": 0
            }
        ],
        "AlbumLabels": [
            {
                "Name": "夜景",
                "FirstCategory": "场景",
                "SecondCategory": "自然风光",
                "Confidence": 93
            },
            {
                "Name": "塔",
                "FirstCategory": "场景",
                "SecondCategory": "建筑",
                "Confidence": 82
            },
            {
                "Name": "城市",
                "FirstCategory": "场景",
                "SecondCategory": "建筑",
                "Confidence": 5
            }
        ],
        "RequestId": "e6d685b1-d898-4dc9-a545-cfeb3a988da8"
    }
}
```

**Example 2: 图像标签检测请求失败**



Input: 

```
tccli tiia DetectLabel --cli-unfold-argument  \
    --ImageUrl https://123.jpg
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "FailedOperation.DownLoadError",
            "Message": "下载失败"
        },
        "RequestId": "a169390a-6ff3-4c42-ad25-a7858c35e576"
    }
}
```

