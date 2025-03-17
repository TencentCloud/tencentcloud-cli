**Example 1: 创建标签**

创建标签

Input: 

```
tccli lke CreateAttributeLabel --cli-unfold-argument  \
    --BotBizId 1826933901291945900 \
    --AttrName 汽车类型 \
    --Labels.0.LabelName SUV \
    --Labels.0.SimilarLabels 运动型多用途汽车 越野
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

