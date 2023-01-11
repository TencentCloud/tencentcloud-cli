**Example 1: 根据appid获取uin**



Input: 

```
tccli account GetUinByAppId --cli-unfold-argument  \
    --Appid 1255427217
```

Output: 
```
{
    "Response": {
        "Uin": 100000546547,
        "Appid": 1255427217,
        "AddTimestamp": "2022-12-15 15:35:40",
        "RequestId": "ffccca38-aef0-4487-9ead-c1f675f8d98d"
    }
}
```

