**Example 1: 列举热词表**

用户通过该接口，可获得所有的热词表及其信息。

Input: 

```
tccli trtc GetRecognizeVocabList --cli-unfold-argument  \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "RequestId": "d59cf4f8-cab8-44a6-b95f-2a1b2ba7ebe7",
        "TotalCount": 2,
        "VocabList": [
            {
                "CreateTime": "2025-08-05T21:03:04+08:00",
                "Description": "",
                "Name": "test5",
                "State": 0,
                "UpdateTime": "2025-08-05T21:03:04+08:00",
                "VocabId": "08cf39889eae427a9bc85d263f9a37f8",
                "WordWeights": [
                    {
                        "Weight": 3,
                        "Word": "测试创建"
                    },
                    {
                        "Weight": 7,
                        "Word": "测试创建2"
                    }
                ]
            },
            {
                "CreateTime": "2025-08-05T21:03:28+08:00",
                "Description": "",
                "Name": "test5",
                "State": 0,
                "UpdateTime": "2025-09-10T12:15:25+08:00",
                "VocabId": "2f3970e3515b4acaa26eaff759e223e8",
                "WordWeights": [
                    {
                        "Weight": 3,
                        "Word": "测试创建5"
                    },
                    {
                        "Weight": 7,
                        "Word": "测试创建6"
                    }
                ]
            }
        ]
    }
}
```

