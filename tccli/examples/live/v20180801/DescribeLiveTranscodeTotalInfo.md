**Example 1: 请求示例**



Input: 

```
tccli live DescribeLiveTranscodeTotalInfo --cli-unfold-argument  \
    --StartTime '2019-03-01 00:00:00' \
    --EndTime '2019-03-01 12:00:00'
```

Output: 
```
{
    "Response": {
        "DataInfoList": [
            {
                "Time": "2019-03-01 00:00:00",
                "Duration": 100,
                "ModuleCodec": "",
                "Resolution": "540*480"
            }
        ],
        "RequestId": "c8465603-c3a6-44bc-8354-a9b67bf44301"
    }
}
```

