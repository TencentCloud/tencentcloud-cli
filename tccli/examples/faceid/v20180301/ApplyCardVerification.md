**Example 1: 正常响应**



Input: 

```
tccli faceid ApplyCardVerification --cli-unfold-argument  \
    --ImageBase64Front abc \
    --ImageBase64Back abc \
    --ImageUrlFront abc \
    --ImageUrlBack abc \
    --Nationality abc \
    --CardType abc
```

Output: 
```
{
    "Response": {
        "CardVerificationToken": "abc",
        "RequestId": "abc"
    }
}
```

