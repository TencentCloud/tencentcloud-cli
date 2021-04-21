**Example 1: BTOE存证电子凭证查询**

用户通过存证编码向BTOE查询存证电子凭证信息。

Input: 

```
tccli btoe GetDepositCert --cli-unfold-argument  \
    --EvidenceId testt222e32278733387121ststtest
```

Output: 
```
{
    "Response": {
        "RequestId": "testtest33111113333111",
        "EvidenceId": "testt222e32278733387121ststtest",
        "EvidenceCert": "http://test-1251451924.cos.ap-nanjing.myqcloud.com/btoe%2620210326%26testt222e32278733387121ststtest.png?sign=q-sign-algorithm%3Dsha1%26q-ak%3DAKIDkIyS6YfpfH3bcTuzz05uWr1vwkMjrra6%26q-sign-time%3D1617003400%3B1617007000%26q-key-time%3D1617003400%3B1617007000%26q-header-list%3Dhost%26q-url-param-list%3D%26q-signature%3D2c2c544622742db817848beff9580c51804ec7f0"
    }
}
```

