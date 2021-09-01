**Example 1: IP解封操作**



Input: 

```
tccli dayu CreateUnblockIp --cli-unfold-argument  \
    --Ip 1.1.1.1 \
    --ActionType user
```

Output: 
```
{
    "Response": {
        "ActionType": "user",
        "Ip": "111.230.156.235",
        "RequestId": "a78db8c5-598e-459e-87d0-37682739920e",
        "UnblockTime": "2018-09-10 21:15:23"
    }
}
```

