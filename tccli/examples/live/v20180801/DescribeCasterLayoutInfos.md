**Example 1: 查询导播台的布局列表**



Input: 

```
tccli live DescribeCasterLayoutInfos --cli-unfold-argument  \
    --CasterId 63501
```

Output: 
```
{
    "Response": {
        "LayoutInfos": [
            {
                "LayoutIndex": 1,
                "InputIndexList": "1|2",
                "LayoutTemplateId": 20,
                "LayoutWidth": 1280,
                "LayoutHeight": 720,
                "LayoutParams": [
                    {
                        "LayerId": 1,
                        "LayerWidth": 0.5,
                        "LayerHeight": 1,
                        "LayerLocationX": 0,
                        "LayerLocationY": 0,
                        "UsePortraitSegment": false
                    },
                    {
                        "LayerId": 2,
                        "LayerWidth": 0.5,
                        "LayerHeight": 1,
                        "LayerLocationX": 0.5,
                        "LayerLocationY": 0,
                        "UsePortraitSegment": false
                    }
                ]
            }
        ],
        "RequestId": "203cd886-18d8-4f42-a9b4-141c182bc920"
    }
}
```

