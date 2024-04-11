**Example 1: 知识标签列表**

知识标签列表

Input: 

```
tccli lke ListAttributeLabel --cli-unfold-argument  \
    --BotBizId 1696822786072117248 \
    --PageNumber 1 \
    --PageSize 15
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "AttrKey": "test",
                "AttrName": "诶皮爱标签",
                "IsUpdating": false,
                "LabelNames": [
                    "你好"
                ]
            }
        ],
        "RequestId": "f949f7b3-c7f1-4e46-8049-db0c872dc174",
        "Total": "1"
    }
}
```

