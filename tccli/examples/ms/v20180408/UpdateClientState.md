**Example 1: client上报**

client上报

Input: 

```
tccli ms UpdateClientState --cli-unfold-argument  \
    --ClientId ClientId \
    --Ip 1.1.1.1 \
    --Internal 0 \
    --ServerVersion ServerVersion \
    --Hostname Hostname \
    --Os windows
```

Output: 
```
{
    "Response": {
        "ResultCode": "0",
        "RequestId": "RequestId-xxxxx"
    }
}
```

