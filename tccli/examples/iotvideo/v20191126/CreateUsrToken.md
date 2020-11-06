**Example 1: 终端用户接入授权**



Input: 

```
tccli iotvideo CreateUsrToken --cli-unfold-argument  \
    --AccessId ******* \
    --UniqueId testDev001 \
    --TtlMinutes 10
```

Output: 
```
{
    "Response": {
        "TerminalId": "-9223371585883208722",
        "AccessToken": "************",
        "AccessId": "***********",
        "ExpireTime": 1583739875,
        "RequestId": "a434f151-f8ad-4276-9cf6-714a181304d6"
    }
}
```

