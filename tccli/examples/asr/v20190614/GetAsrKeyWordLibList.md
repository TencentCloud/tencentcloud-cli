**Example 1: 列举关键词表**

用户通过该接口，可获得所有的关键词表及其信息。

Input: 

```
tccli asr GetAsrKeyWordLibList --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Data": {
            "KeyWordLibList": [
                {
                    "KeyWordLibId": "aa6f402f263f12ea856fc81fbecfd0sd",
                    "Name": "示例词表",
                    "KeyWordList": [
                        "避风港"
                    ],
                    "CreateTime": "2024-08-24T13:28:48+00:00",
                    "UpdateTime": "2024-08-24T13:28:48+00:00"
                }
            ],
            "TotalCount": 1
        },
        "RequestId": "b3808ad3-d8dd-4b65-96c9-7d6f1f81b6b6"
    }
}
```

