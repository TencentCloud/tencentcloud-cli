**Example 1: 获取热词表**

用户通过热词表ID获取热词表内容

Input: 

```
tccli asr GetAsrVocab --cli-unfold-argument  \
    --VocabId aa6f402f263f12ea856fc81fbecfd0sd
```

Output: 
```
{
    "Response": {
        "RequestId": "a31edb26-3b6a-481e-91f8-d0009065eaed",
        "Name": "词表名称",
        "Description": "词表描述",
        "VocabId": "aa6f402f263f12ea856fc81fbecfd0sd",
        "WordWeights": [
            {
                "Word": "智聆",
                "Weight": 1
            },
            {
                "Word": "滨海大厦",
                "Weight": 6
            },
            {
                "Word": "存储桶",
                "Weight": 8
            },
            {
                "Word": "核保",
                "Weight": 10
            }
        ],
        "CreateTime": "2020-01-14T10:24:07+08:00",
        "UpdateTime": "2020-01-14T10:24:07+08:00",
        "State": 0
    }
}
```

