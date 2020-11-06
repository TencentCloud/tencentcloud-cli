**Example 1: 设置Fairplay方案所需的私钥、ASK**



Input: 

```
tccli drm AddFairPlayPem --cli-unfold-argument  \
    --Pem ENEcI2pZnZPi/x+wZNXaNDyfdw/hMoTpYDSNuaGV0gw1NhEE2zMMDdPhFcE0EbRx6sBKcTNfqTSa/M7cB6RAWcv0Ic/96UBSMjzIKvvViMUnozEoce3ySm6pS/KHxa32Xtmd/3aKxYgeHl1MIG03CdGIotV6rXo/V727gXTVQcg \
    --Ask ISS0DkPgq41Q7ca7/QWEUlAkrsCsRsxrN2y0R8kJN4jIepYnaflfNXiIsb/iR0Rrg24DofcKJx2Y5NgYUMVaxPtVyiTR5mtoo5HB9cvEyEgje9tKMlP1WyBoKRMFlYy32jqTZZeUW1uLpXdLhn2yyPOfw9s0XlsdKVKs5Hsxqnc
```

Output: 
```
{
    "Response": {
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03",
        "FairPlayPemId": 1234,
        "Priority": 2
    }
}
```

