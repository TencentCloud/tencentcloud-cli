**Example 1: 列举热词表**

用户通过该接口，可获得所有的热词表及其信息。

Input: 

```
tccli asr GetAsrVocabList --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "e4c745a1-27a0-4143-972e-2ced14645ab4",
        "TotalCount": 1,
        "VocabList": [
            {
                "Name": "词表1",
                "Description": "业务1",
                "VocabId": "e92bd0d632d211eab508446a2eb5fd98",
                "WordWeights": [
                    {
                        "Word": "智聆",
                        "Weight": 1
                    }
                ],
                "TagInfos": [
                    "tag"
                ],
                "CreateTime": "2020-01-09T19:26:42+08:00",
                "UpdateTime": "2020-01-14T10:43:07+08:00",
                "State": 0
            },
            {
                "Name": "词表2",
                "Description": "业务2",
                "VocabId": "f10b9bf4367411eab508446a2eb5fd98",
                "WordWeights": [
                    {
                        "Word": "滨海大厦",
                        "Weight": 6
                    }
                ],
                "TagInfos": [
                    "tag"
                ],
                "CreateTime": "2020-01-14T10:24:07+08:00",
                "UpdateTime": "2020-01-14T10:24:07+08:00",
                "State": 0
            },
            {
                "Name": "词表3",
                "Description": "业务3",
                "VocabId": "540acf7332d311eab508446a2eb5fd98",
                "WordWeights": [
                    {
                        "Word": "存储桶",
                        "Weight": 8
                    }
                ],
                "TagInfos": [
                    "tag"
                ],
                "CreateTime": "2020-01-09T19:29:41+08:00",
                "UpdateTime": "2020-01-09T19:29:42+08:00",
                "State": 0
            }
        ]
    }
}
```

