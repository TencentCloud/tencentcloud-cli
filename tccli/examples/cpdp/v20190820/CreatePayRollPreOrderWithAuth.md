**Example 1: 务工卡-核身预下单带授权**



Input: 

```
tccli cpdp CreatePayRollPreOrderWithAuth --cli-unfold-argument  \
    --WechatSubAppId wxa1111111 \
    --OpenId onqOjjmo8wmTOOtSKwXtGjg9Gb58 \
    --WechatAppId wxa1111111 \
    --CompanyName 某用工企业 \
    --EmploymentType LONG_TERM_EMPLOYMENT \
    --ProjectName 某项目 \
    --SubMerchantId 1111111 \
    --UserName LP7bT4hQXUsOZCEvK2YrSiqFsnP0oRMfeoLN0vBg \
    --IdNo 7FzH5XksJG3a8HLLsaaUV6K54y1OnPMY5 \
    --AuthNumber mcdhehfgisdhfjghed39384564i83
```

Output: 
```
{
    "Response": {
        "AuthNumber": "mcdhehfgisdhfjghed39384564i83",
        "ExpireTime": 300,
        "MerchantId": "1111111",
        "OpenId": "onqOjjmo8wmTOOtSKwXtGjg9Gb58",
        "RequestId": "req-164085245170",
        "SubMerchantId": "1111111",
        "Token": "abcdefghijklmn"
    }
}
```

