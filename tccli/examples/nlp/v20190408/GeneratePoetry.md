**Example 1: 智能写诗调用示例**



Input: 

```
tccli nlp GeneratePoetry --cli-unfold-argument  \
    --Genre 7 \
    --Text 阳光 \
    --PoetryType 0
```

Output: 
```
{
    "Response": {
        "Title": "阳光",
        "Content": [
            "阳羡溪头万树梅",
            "光风吹梦入城来",
            "天涯不尽山川胜",
            "一片晴霞落酒台"
        ],
        "RequestId": "35fd611d-d4a1-4127-bd16-58ea1fa1a5dc"
    }
}
```

