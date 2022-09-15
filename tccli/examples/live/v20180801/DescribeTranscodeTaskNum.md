**Example 1: 请求示例**



Input: 

```
tccli live DescribeTranscodeTaskNum --cli-unfold-argument  \
    --StartTime 2020-10-12 00:00:00 \
    --EndTime 2020-10-12 00:10:00
```

Output: 
```
{
    "Response": {
        "DataInfoList": [
            {
                "CodeRate": 2000,
                "Num": 1,
                "Time": "2022-01-09 00:00"
            }
        ],
        "RequestId": "f54e3deb-f318-4148-8a68-3c959642f9ec"
    }
}
```

