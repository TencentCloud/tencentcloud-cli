**Example 1: 请求示例**

查询转码总量数据。

Input: 

```
tccli live DescribeLiveTranscodeTotalInfo --cli-unfold-argument  \
    --EndTime 2019-03-01T12:00:00+08:00 \
    --StartTime 2019-03-01T00:00:00+08:00
```

Output: 
```
{
    "Response": {
        "DataInfoList": [
            {
                "Time": "2019-03-01T00:00:00+08:00",
                "Duration": 100,
                "ModuleCodec": "",
                "Resolution": "540*480"
            }
        ],
        "RequestId": "c8465603-c3a6-44bc-8354-a9b67bf44301"
    }
}
```

