**Example 1: 联通手机号三要素核验一致示例**



Input: 

```
tccli faceid PhoneVerificationCUCC --cli-unfold-argument  \
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
        "Isp": "联通",
        "RequestId": "a5fdb909-5ee6-43ff-a152-bb1b9744ee8b"
    }
}
```

**Example 2: 联通手机号三要素核验不一致示例**



Input: 

```
tccli faceid PhoneVerificationCUCC --cli-unfold-argument  \
    --IdCard 11204416541220243X \
    --Name 韦小宝 \
    --Phone 16137688175
```

Output: 
```
{
    "Response": {
        "Description": "信息不一致",
        "Isp": "联通",
        "RequestId": "74182f34-cc90-40b6-b96d-e4189726f0ba",
        "Result": "-4"
    }
}
```

