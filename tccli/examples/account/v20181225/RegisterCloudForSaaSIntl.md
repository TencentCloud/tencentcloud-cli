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

**Example 2: 注册成功2**

含注册活动渠道上报字段

Input: 

```
tccli account RegisterCloudForSaaSIntl --cli-unfold-argument  \
    --ClientUA Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 \
    --CountryName SG \
    --CountryCode 65 \
    --Lang en \
    --Platform intlSaaSTrtc \
    --Password ZaZ5nKx******M6eW1aMXT96vc= \
    --TradeName kghy_01 \
    --TradeOne kghy_01 \
    --TradeTwo kghy_0101 \
    --UserType 1 \
    --FullName ahalizeng \
    --CompanyName tencent \
    --CountryFullName Singapore \
    --Email ahalizengsub3+802@gmail.com \
    --EmailVerifyCode 662437 \
    --RegisterType mail \
    --Area 2 \
    --AccessLevel 3 \
    --UserName ahaLi \
    --ChannelId qcloud.directEnter.document \
    --ChannelType register \
    --TrafficParams ***$;timestamp=1678086234126;from_type=server;track=928db9d8-***$;timestamp=1678086234126;from_type=server;track=928db9d8-***$;t \
    --Time 2025-02-24 03:55:47 \
    --From 19673 \
    --Referer  \
    --QcloudUid 
```

Output: 
```
{
    "Response": {
        "ExpiredTime": 1739964320,
        "Key": "44f3b906c6ce6d38a48b39804ddaefdb",
        "RequestId": "616b122f-2ce1-4406-a002-2c251d5c4a01",
        "Uin": 404000000558
    }
}
```

