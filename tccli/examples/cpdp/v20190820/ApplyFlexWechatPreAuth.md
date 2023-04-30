**Example 1: 微工卡预核身**

微工卡预核身

Input: 

```
tccli cpdp ApplyFlexWechatPreAuth --cli-unfold-argument  \
    --AuthNo abc \
    --OpenId abc \
    --ProjectName abc \
    --EmployerName abc \
    --UserName abc \
    --IdNo abc \
    --EmploymentType abc \
    --AuthType abc \
    --Environment abc
```

Output: 
```
{
    "Response": {
        "ErrCode": "abc",
        "ErrMessage": "abc",
        "Result": {},
        "RequestId": "abc"
    }
}
```

