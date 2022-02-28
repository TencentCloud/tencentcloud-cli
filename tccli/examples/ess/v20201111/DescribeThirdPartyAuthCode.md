**Example 1: 通过AuthCode查询用户是否实名**

通过AuthCode查询用户是否实名，AuthCode 查询后作废，只能查询一次

Input: 

```
tccli ess DescribeThirdPartyAuthCode --cli-unfold-argument  \
    --AuthCode yDxMhUyKQDMFdnUyxgEv8yhSdo0ZFs8I
```

Output: 
```
{
    "Response": {
        "RequestId": "s1629444337855318929",
        "VerifyStatus": "VERIFIED"
    }
}
```

