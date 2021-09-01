**Example 1: 获取关键词样本列表-无条件**

不带任何条件，遍历关键词列表。

Input: 

```
tccli mps DescribeWordSamples --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "TotalCount": 2,
        "WordSet": [
            {
                "Keyword": "张三",
                "TagSet": [
                    "明星",
                    "艺人"
                ],
                "UsageSet": [
                    "Recognition.Ocr",
                    "Recognition.Asr"
                ],
                "CreateTime": "2018-10-01T10:00:00Z",
                "UpdateTime": "2018-10-01T10:00:00Z"
            },
            {
                "Keyword": "李四",
                "TagSet": [
                    "总统"
                ],
                "UsageSet": [
                    "Review.Ocr",
                    "Review.Asr"
                ],
                "CreateTime": "2018-10-01T10:00:00Z",
                "UpdateTime": "2018-10-01T10:00:00Z"
            }
        ],
        "RequestId": "46311b39-10ce-47eb-b2b6-7ce82bb4476d"
    }
}
```

**Example 2: 获取关键词样本列表-有条件**

限定应用场景等条件的关键词查询。

Input: 

```
tccli mps DescribeWordSamples --cli-unfold-argument  \
    --Usages Recognition Review.Ocr \
    --Keywords 张三 \
    --Tags 明星 \
    --Offset 0 \
    --Limit 20
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "WordSet": [
            {
                "Keyword": "张三",
                "TagSet": [
                    "明星",
                    "艺人"
                ],
                "UsageSet": [
                    "Recognition.Ocr",
                    "Recognition.Asr"
                ],
                "CreateTime": "2018-10-01T10:00:00Z",
                "UpdateTime": "2018-10-01T10:00:00Z"
            }
        ],
        "RequestId": "46311b39-10ce-47eb-b2b6-7ce82bb4476d"
    }
}
```

