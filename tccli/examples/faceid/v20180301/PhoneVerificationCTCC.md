**Example 1: 认证成功示例**

校验中国电信手机号、姓名和身份证号的真实性和一致性。

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

**Example 2: 认证失败示例**

传入不一致信息，校验中国电信手机号、姓名和身份证号的真实性和一致性。

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

