**Example 1: 获取问答对列表**

查询已经上传的问答对列表

Input: 

```
tccli lkeap ListQAs --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "List": [
            {
                "Answer": "我是腾讯大模型知识引擎",
                "AttributeLabels": [
                    {
                        "AttributeId": "1830880287852529408",
                        "LabelIds": [
                            "1830880287865112320"
                        ]
                    }
                ],
                "QaId": "1830882708456671000",
                "Question": "你是谁"
            }
        ],
        "RequestId": "5f95d7c7-c881-49d1-98fc-34f138d8ca54"
    }
}
```

