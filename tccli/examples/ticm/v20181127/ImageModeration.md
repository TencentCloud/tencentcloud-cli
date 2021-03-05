**Example 1: 多个识别场景调用都成功**

例：同时调用色情识别、暴恐识别和政治敏感识别，返回结果均为成功。

Input: 

```
tccli ticm ImageModeration --cli-unfold-argument  \
    --ImageUrl https://xx/a.jpg \
    --Config  \
    --Scenes PORN POLITICS TERRORISM
```

Output: 
```
{
    "Response": {
        "Suggestion": "REVIEW",
        "PornResult": {
            "Code": 0,
            "Msg": "OK",
            "Suggestion": "PASS",
            "Confidence": 83,
            "AdvancedInfo": "",
            "Type": "LABEL"
        },
        "PoliticsResult": {
            "Code": 0,
            "Msg": "OK",
            "Suggestion": "PASS",
            "Confidence": 8,
            "FaceResults": [
                {
                    "FaceRect": {
                        "Height": 221,
                        "Width": 221,
                        "X": 98,
                        "Y": 115
                    },
                    "Candidates": [
                        {
                            "Name": "本拉登",
                            "Confidence": 8
                        }
                    ]
                }
            ],
            "Type": "FACE"
        },
        "TerrorismResult": {
            "Code": 0,
            "Msg": "OK",
            "Suggestion": "REVIEW",
            "Confidence": 42,
            "AdvancedInfo": "",
            "FaceResults": [],
            "Type": "LABEL"
        },
        "Extra": "",
        "RequestId": "02f1733c-1bfe-49ed-9e72-8ecd6ba058dd"
    }
}
```

**Example 2: 部分识别场景调用都成功**

例：只调用其中的色情识别，返回结果为成功。

Input: 

```
tccli ticm ImageModeration --cli-unfold-argument  \
    --ImageUrl https://porn.jpg \
    --Config  \
    --Scenes PORN
```

Output: 
```
{
    "Response": {
        "Suggestion": "PASS",
        "PornResult": {
            "Code": 0,
            "Msg": "OK",
            "Suggestion": "PASS",
            "Confidence": 0,
            "AdvancedInfo": "",
            "Type": "LABEL"
        },
        "PoliticsResult": null,
        "TerrorismResult": null,
        "Extra": "",
        "RequestId": "5a645a08-2e2b-4979-9815-1f2c00c2304e"
    }
}
```

**Example 3: 部分识别场景调用失败**

例：只调用其中的色情识别，返回结果为失败，Code 不为0。

Input: 

```
tccli ticm ImageModeration --cli-unfold-argument  \
    --ImageUrl https://porn.jpg \
    --Config  \
    --Scenes PORN
```

Output: 
```
{
    "Response": {
        "Suggestion": "",
        "PornResult": {
            "Code": -1,
            "Msg": "内部错误",
            "Suggestion": "",
            "Confidence": 0,
            "AdvancedInfo": "",
            "Type": "LABEL"
        },
        "PoliticsResult": null,
        "TerrorismResult": null,
        "Extra": "",
        "RequestId": "3854392b-19d4-4cae-8933-b010cd087c84"
    }
}
```

**Example 4: 部分识别场景调用且部分成功**

例：同时调用色情识别和暴恐识别，其中色情识别的结果为失败（Code非0），暴恐识别的结果为成功。

Input: 

```
tccli ticm ImageModeration --cli-unfold-argument  \
    --ImageUrl https://fack.jpg \
    --Config  \
    --Scenes PORN TERRORISM
```

Output: 
```
{
    "Response": {
        "Suggestion": "REVIEW",
        "PornResult": {
            "Code": -1,
            "Msg": "内部错误",
            "Suggestion": "",
            "Confidence": 0,
            "AdvancedInfo": "",
            "Type": "LABEL"
        },
        "TerrorismResult": {
            "Code": 0,
            "Msg": "OK",
            "Suggestion": "REVIEW",
            "Confidence": 44,
            "AdvancedInfo": "",
            "Type": "LABEL",
            "FaceResults": []
        },
        "PoliticsResult": null,
        "Extra": "",
        "RequestId": "547d2427-2f82-4d8d-99e0-f2a504619661"
    }
}
```

**Example 5: 整体结果失败**

例：调用部分识别场景或者全部场景，由于下载等原因，导致整体结果失败。

Input: 

```
tccli ticm ImageModeration --cli-unfold-argument  \
    --ImageUrl https://error.jpg \
    --Config  \
    --Scenes PORN POLITICS TERRORISM
```

Output: 
```
{
    "Response": {
        "RequestId": "5f77ef5e-f381-49af-89bf-e558b25b3c15"
    }
}
```

