**Example 1: 创建知识标签**

创建知识标签

Input: 

```
tccli lke CreateAttributeLabel --cli-unfold-argument  \
    --BotBizId 1696822786072117248 \
    --AttrKey test \
    --AttrName 诶皮爱标签 \
    --Labels.0.LabelName 你好 \
    --Labels.0.SimilarLabels 车型a
```

Output: 
```
{
    "Response": {
        "RequestId": "802c3847-9781-4818-959a-aff3035d22fc"
    }
}
```

