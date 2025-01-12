**Example 1: 谷歌注册用例**



Input: 

```
tccli account RegisterSaaSAccountByGoogle --cli-unfold-argument  \
    --ClientUA Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 \
    --CountryName HK \
    --CountryCode 852 \
    --Lang en \
    --Platform intlSaaSXXX \
    --Password ZaZ5nKx1Qc****aMXT96vc= \
    --TradeName kghy_01 \
    --TradeOne kghy_01 \
    --TradeTwo kghy_0101 \
    --UserType 1 \
    --FullName aha \
    --CompanyName tencent \
    --CountryFullName Hong Kong, China \
    --Mail test@gmail.com \
    --AccessToken ya29.a0ARW5****GhWOvNmulakU4hj8JUF9_Q0171
```

Output: 
```
{
    "Response": {
        "ExpiredTime": "1735307671",
        "Key": "4e1b668233042905fbb5420ffa972948",
        "RequestId": "80d188d7-9194-4291-9676-249455da2bde",
        "Sid": "SaaSSidb1182796-03b9-3e39-0682-07aa4f362979",
        "Uin": 450600000015
    }
}
```

