**Example 1: 获取日志链接**



Input: 

```
tccli kiki CreateSessionLogViewUrl --cli-unfold-argument  \
    --Profile cloud-pc \
    --TargetUin 100024220771 \
    --SessionId 0524c9b9-2793-41e2-8761-2fc0fc0a963f \
    --IdentityIdList ********** \
    --ExpireSeconds 3600
```

Output: 
```
{
    "Response": {
        "ExpiredTime": 1781598204,
        "Url": "https://kiki.woa.com/log?token=yFocKmrMSTEKWMjexwDhQsAfNSSJnIGHDIDj9bcmg9deWBN92HEvxqaVtbjQy4EUsn2DQEbsTjavTSU29u3nhxEMaq4S026_AKJTWcsVwctcZB5QbcMKTA_7dB6ek8Q0YgfIvnPJz8nOP8QhJIkiHw2HVaiKuvZqXzhtth0",
        "RequestId": "2236780f-0cfe-4855-aaf0-66c1ca480290"
    }
}
```

