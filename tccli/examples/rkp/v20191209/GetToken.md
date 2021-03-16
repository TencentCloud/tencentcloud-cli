**Example 1: RPGetToken**



Input: 

```
tccli rkp GetToken --cli-unfold-argument  \
    --BusinessId 0 \
    --Scene 0 \
    --ExpireTime 0 \
    --AppClientIp xx \
    --BusinessUserId xx \
    --OldToken xx
```

Output: 
```
{
    "Response": {
        "RequestId": "5e93a212-ca01-0fdc-eedd-5a1fce5e83e6",
        "Token": "fafdafldsf;jds"
    }
}
```

