**Example 1: 查询冲突问详情**

查询冲突问详情

Input: 

```
tccli adp DescribeConflictQA --cli-unfold-argument  \
    --KbId 2097944147493706368 \
    --ConflictGroupId 2097944306089351424
```

Output: 
```
{
    "Response": {
        "ConflictQaList": [
            {
                "QaId": "2097944152336885184",
                "Question": "智阅Air14轻薄笔记本电脑的价格是多少？",
                "Answer": "智阅Air14轻薄笔记本电脑的价格为¥4123。",
                "SourceType": 3,
                "FileName": "",
                "FileType": "",
                "UpdateTime": "1789023875",
                "EffectiveDomain": 4
            }
        ],
        "RequestId": "889461f2-8d96-4704-999b-30f5c5b55d43"
    }
}
```

