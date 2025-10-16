**Example 1: 获取智能识别热词表 **

用户通过热词表ID获取热词表内容

Input: 

```
tccli trtc GetRecognizeVocab --cli-unfold-argument  \
    --VocabId a6c66d9721b840219674660c32755599
```

Output: 
```
{
    "Response": {
        "CreateTime": "2025-08-05T12:09:36+08:00",
        "Description": "",
        "Name": "test3",
        "RequestId": "e599e38a-d9e1-4c7c-a245-5a7f29f2632f",
        "State": 0,
        "UpdateTime": "2025-08-05T12:09:36+08:00",
        "VocabId": "a6c66d9721b840219674660c32755599",
        "WordWeights": [
            {
                "Weight": 2,
                "Word": "test3"
            }
        ]
    }
}
```

