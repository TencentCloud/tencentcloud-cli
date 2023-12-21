**Example 1: 申请Web核验服务Token**

申请Web核验服务Token

Input: 

```
tccli faceid ApplyWebVerificationBizTokenIntl --cli-unfold-argument  \
    --CompareImageBase64 xhBQAAACBjSFJNAAB6****AAAASUVORK5CYII= \
    --RedirectURL https://www.tencentcloud.com/products/faceid \
    --Extra ExtraString
```

Output: 
```
{
    "Response": {
        "VerificationURL": "https://intl.faceid.qq.com/reflect/?token=81EEF678-28EE-4759-A82E-6CBBBE6BC442",
        "BizToken": "81EEF678-28EE-4759-A82E-6CBBBE6BC442",
        "RequestId": "b16194cd-8f52-4e66-882a-eb6bf15c016d"
    }
}
```

