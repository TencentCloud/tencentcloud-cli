**Example 1: 获取TCB账号绑定信息**



Input: 

```
tccli account DescribeTCBBinding --cli-unfold-argument  \
    --Type wx_open \
    --Username xxxxx
```

Output: 
```
{
    "Response": {
        "UsernameBoundUin": 123,
        "BindType": "wx_open",
        "UinBoundUsername": null,
        "RequestId": "562abe2a-0817-4097-ad24-c936eb2a01e1"
    }
}
```

