**Example 1: CreateShortUrl**



Input: 

```
tccli zj CreateShortUrl --cli-unfold-argument  \
    --License KA3431QZPU \
    --WxAppId 1234 \
    --PageUrl access/new/edit \
    --MiddlePageId 1 \
    --Name name1
```

Output: 
```
{
    "Response": {
        "Data": {
            "MiniProgramUrl": "weixin://dl/business/?ticket=23",
            "MiniProgramHttpUrl": "12"
        },
        "RequestId": "111111"
    }
}
```

