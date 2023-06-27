**Example 1: 诗词生成调用示例**

诗词生成。

Input: 

```
tccli nlp ComposePoetry --cli-unfold-argument  \
    --Text 阳光 \
    --PoetryType 2 \
    --Genre 5
```

Output: 
```
{
    "Response": {
        "Content": [
            "洛阳无人见",
            "江城日光流",
            "月明山上路",
            "柳暗水中洲"
        ],
        "RequestId": "a4878a27-7a5c-4cd4-b17d-6a1ff403f626",
        "Title": "阳光"
    }
}
```

