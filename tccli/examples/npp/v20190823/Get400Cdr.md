**Example 1: 获取中间号话单**



Input: 

```
tccli npp Get400Cdr --cli-unfold-argument  \
    --BizAppId 65535 \
    --StartTimeStamp 1586729400
```

Output: 
```
{
    "Response": {
        "ErrorCode": "0",
        "Msg": "",
        "Offset": "0",
        "Cdr": []
    }
}
```

