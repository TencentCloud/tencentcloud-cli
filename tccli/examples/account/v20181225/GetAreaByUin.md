**Example 1: 根据uin获取地域**



Input: 

```
tccli account GetAreaByUin --cli-unfold-argument  \
    --OpUin 100000546547
```

Output: 
```
{
    "Response": {
        "Area": 1,
        "CountryName": "CN",
        "CountryCode": "86",
        "RequestId": "ffccca38-aef0-4487-9ead-c1f675f8d98d"
    }
}
```

