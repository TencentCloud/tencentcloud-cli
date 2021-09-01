**Example 1: 搜索日志**



Input: 

```
tccli cdn SearchClsLog --cli-unfold-argument  \
    --Channel cdn \
    --LogsetId 4242424-8723-45e3-9c75-a0599ef9143a \
    --TopicIds 57460798-8723-45e3-9c75-a0599ef9143a,57460798-8723-45e3-9c75-22242141 \
    --StartTime '2019-11-18 00:00:00' \
    --EndTime '2019-11-18 02:00:00' \
    --Query abc \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "RequestId": "242144aeff-8723-45e3-9c75-a0599ef9143a",
        "Logs": {
            "Context": "2e1414",
            "Listover": false,
            "Results": [
                {
                    "TopicId": "57460798-8723-45e3-9c75-a0599ef9143a",
                    "TopicName": "test_topic",
                    "Timestamp": "2019-11-18 00:00:00",
                    "Content": "abcdafaf",
                    "Filename": "",
                    "Source": ""
                }
            ]
        }
    }
}
```

