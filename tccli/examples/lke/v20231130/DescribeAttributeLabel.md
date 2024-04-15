**Example 1: 查询知识标签**

查询知识标签

Input: 

```
tccli lke DescribeAttributeLabel --cli-unfold-argument  \
    --BotBizId 1696822786072117248 \
    --AttributeBizId 1734549420823662592 \
    --LastLabelBizId 1734549420823662593 \
    --Limit 1
```

Output: 
```
{
    "Response": {
        "AttrKey": "test",
        "AttrName": "诶皮爱标签",
        "AttributeBizId": "1734549420823662592",
        "LabelNumber": "1",
        "Labels": [],
        "RequestId": "99ff53c2-120a-4d0a-b54d-760a65852cd6"
    }
}
```

