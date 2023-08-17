**Example 1: client上报**

client上报

Input: 

```
tccli ms UpdateClientState --cli-unfold-argument  \
    --ClientId abc \
    --Ip abc \
    --Internal 0 \
    --ServerVersion abc \
    --Hostname abc \
    --Os abc
```

Output: 
```
{
    "Response": {
        "ResultCode": "abc",
        "RequestId": "abc"
    }
}
```

