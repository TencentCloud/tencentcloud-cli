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

**Example 2: 注册成功2**

含注册活动渠道上报

Input: 

```
tccli account RegisterSaaSAccountByGoogle --cli-unfold-argument  \
    --ClientUA Mozilla/5.0 (Maci*********ecko) Chrome/131.0.0.0 Safari/537.36 \
    --CountryName AU \
    --CountryCode 61 \
    --Lang zh \
    --Platform intlSaaSTrtc \
    --Password yrRWHfN***********eBBNNtlLHA= \
    --TradeName kghy_16 \
    --TradeOne kghy_16 \
    --TradeTwo kghy_1601 \
    --UserType 1 \
    --FullName aha \
    --CompanyName tencent \
    --CountryFullName Australia \
    --Mail ahali****@gmail.com \
    --IdToken eyJhbGciOiJSUzI1NiIsIm****WlDMcnN2C6hPnmRVLmrHeD5zaCVCxYeW-tDQuatA \
    --Cip 127.0.0.2 \
    --ChannelId test.directEnter1 \
    --ChannelType register \
    --TrafficParams ***$;timestamp=1678086234126;from_type=server;track=928db9d8-***$;timestamp=1678086234126;from_type=server;track=928db9d8-***$;t \
    --From 19673 \
    --Referer  \
    --QcloudUid 
```

Output: 
```
{
    "Response": {
        "ExpiredTime": "1739953366",
        "Key": "27bf37536d6b843791f22a4b2ad8a12e",
        "RequestId": "a8a6cf1a-d255-467b-bf56-8a5ceeb679ce",
        "Sid": "SaaSSid1b0abaf5-dca1-c0e9-198a-d0fb42f02bb2",
        "Uin": 404000000556
    }
}
```

