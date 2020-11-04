**Example 1: probeTokenQ**



Input: 

```
tccli rkp GetOpenId --cli-unfold-argument  \
    --DeviceToken aaaa\
    --BusinessId 1
```

Output: 
```
{
    "Response": {
        "RequestId": "5e93a212-ca01-0fdc-eedd-5a1fce5e83e6",
        "OpenId": "5e93a212-ca01-0fdc-eedd-5a1fce5e83e6",
        "RiskInfo": []
    }
}
```

