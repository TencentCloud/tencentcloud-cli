**Example 1: 检查知识标签是否被引用**

检查知识标签是否被引用

Input: 

```
tccli lke CheckAttributeLabelRefer --cli-unfold-argument  \
    --BotBizId 1696822786072117248 \
    --LabelBizId 1734549420823662593 \
    --AttributeBizId 1734549420823662592
```

Output: 
```
{
    "Response": {
        "IsRefer": false,
        "RequestId": "2bf7f1f1-9346-4919-9561-e85805017676"
    }
}
```

