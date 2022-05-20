**Example 1: 务工卡-生成授权令牌**



Input: 

```
tccli cpdp CreatePayRollToken --cli-unfold-argument  \
    --WechatSubAppId wxa1111111 \
    --OpenId onqOjjmo8wmTOOtSKwXtGjg9Gb58 \
    --WechatAppId wxa1111111 \
    --EmploymentType LONG_TERM_EMPLOYMENT \
    --SubMerchantId 1111111 \
    --UserName LP7bT4hQXUsOZCEvK2YrSiqFsnP0oRMfeoLN0vBg \
    --IdNo 7FzH5XksJG3a8HLLsaaUV6K54y1OnPMY5
```

Output: 
```
{
    "Response": {
        "ExpireTime": 1800,
        "MerchantId": "1111111",
        "OpenId": "9x111111",
        "RequestId": "req-164085451674",
        "SubMerchantId": "1111111",
        "Token": "abcdefghijklmn"
    }
}
```

