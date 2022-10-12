**Example 1: 个人认证**



Input: 

```
tccli bma CreateCRUserVerify --cli-unfold-argument  \
    --UserName xx \
    --Type xx \
    --UserPhone xx \
    --UserID xx \
    --VerificationCode xx
```

Output: 
```
{
    "Response": {
        "Status": 0,
        "Note": "xx",
        "RequestId": "xx"
    }
}
```

