**Example 1: 电信手机号三要素核验一致示例**



Input: 

```
tccli faceid PhoneVerificationCTCC --cli-unfold-argument  \
    --IdCard 11204416541220243X \
    --Name 韦小宝 \
    --Phone 16137688175
```

Output: 
```
{
    "Response": {
        "Result": "0",
        "Description": "认证通过",
        "Isp": "电信",
        "RequestId": "a5fdb909-5ee6-43ff-a152-bb1b9744ee8b"
    }
}
```

**Example 2: 电信手机号三要素核验不一致示例**



Input: 

```
tccli faceid PhoneVerificationCTCC --cli-unfold-argument  \
    --IdCard 11204416541220243X \
    --Name 韦小宝 \
    --Phone 16137688175
```

Output: 
```
{
    "Response": {
        "Description": "信息不一致",
        "Isp": "电信",
        "RequestId": "5d3e13ad-ff97-409c-ad98-373158369b43",
        "Result": "-4"
    }
}
```

