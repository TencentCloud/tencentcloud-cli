**Example 1: 注册用例2**

注册用例2

Input: 

```
tccli account RegisterCloudForSaaSIntl --cli-unfold-argument  \
    --ClientUA Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 \
    --CountryName SG \
    --CountryCode 65 \
    --Lang en \
    --Platform intlSaaSXXX \
    --Password ZaZ5nKx******M6eW1aMXT96vc= \
    --TradeName kghy_01 \
    --TradeOne kghy_01 \
    --TradeTwo kghy_0101 \
    --UserType 1 \
    --FullName ahalizeng \
    --CompanyName tencent \
    --CountryFullName Singapore \
    --RegisterType mail \
    --Area 2 \
    --AccessLevel 3 \
    --Email test@gmail.com \
    --EmailVerifyCode 788854 \
    --UserName ahaLi
```

Output: 
```
{
    "Response": {
        "ExpiredTime": 1735213901,
        "Key": "fbcde7afed9c4dfb8be44896d2aab61c",
        "RequestId": "df52a307-3fdf-44d9-87bf-e05b7fe6ee4b",
        "Uin": 450600000003
    }
}
```

