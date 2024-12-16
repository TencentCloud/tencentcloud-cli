**Example 1: 同步cam用户**



Input: 

```
tccli emr SyncCamUsers --cli-unfold-argument  \
    --Users.0.Uin 1 \
    --Users.0.Name abc \
    --UserPwd abc
```

Output: 
```
{
    "Response": {
        "RequestId": "abc"
    }
}
```

