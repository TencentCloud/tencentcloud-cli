**Example 1: 文本润色调用示例**

对中文文本进行扩写。

Input: 

```
tccli nlp TextEmbellish --cli-unfold-argument  \
    --Text 中国奥运健儿击败强敌，勇夺冬奥会首金 \
    --SourceLang zh \
    --Number 2 \
    --Style expansion
```

Output: 
```
{
    "Response": {
        "EmbellishList": [
            {
                "EmbellishType": "expansion",
                "Text": "现在的中国跳水奥运健儿一路高歌猛进击败强敌，不负众望的勇夺温哥华冬奥会单板滑雪首金"
            },
            {
                "EmbellishType": "expansion",
                "Text": "年轻的中国冰雪奥运健儿一次次击败强敌，历史性的勇夺温哥华冬奥会史无前例的首金"
            }
        ],
        "RequestId": "fd345650-b62b-4949-bdd7-d774152dba9a"
    }
}
```

