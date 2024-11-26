**Example 1: 创建标签**

创建标签

Input: 

```
tccli lke CreateAttributeLabel --cli-unfold-argument  \
    --BotBizId 1851816552255193088 \
    --AttrName 哈哈哈 \
    --Labels.0.LabelName 的点点滴滴 \
    --Labels.0.SimilarLabels dfdf 发的
```

Output: 
```
{
    "Response": {
        "AttrBizId": "1856169972235990080",
        "RequestId": "044de4f1-8d88-4779-b9f7-b8c0e9f81752"
    }
}
```

