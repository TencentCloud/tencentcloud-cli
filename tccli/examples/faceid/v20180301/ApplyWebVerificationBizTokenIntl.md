**Example 1: 申请Web核验服务Token**

申请Web核验服务Token

Input: 

```
tccli faceid ApplyWebVerificationBizTokenIntl --cli-unfold-argument  \
    --RedirectURL https://www.tencentcloud.com/products/faceid \
    --Config.CheckMode 1 \
    --Config.IDCardType MainlandIDCard
```

Output: 
```
{
    "Response": {
        "BizToken": "584D404C-F1C3-401C-961E-78C6EF90BDDB",
        "VerificationURL": "https://intl-test.faceid.qq.com/reflect/?token=584D404C-F1C3-401C-961E-78C6EF90BDDB",
        "VerificationUrl": "https://intl-test.faceid.qq.com/reflect/?token=584D404C-F1C3-401C-961E-78C6EF90BDDB",
        "RequestId": "1334f124-317f-4ea0-969e-19fba57f568a"
    }
}
```

