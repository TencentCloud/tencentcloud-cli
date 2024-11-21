**Example 1: 手机号三要素核验一致示例**



Input: 

```
tccli faceid PhoneVerification --cli-unfold-argument  \
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

**Example 2: 手机号三要素核验不一致示例**



Input: 

```
tccli faceid PhoneVerification --cli-unfold-argument  \
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
        "RequestId": "884a35af-289f-4b4e-a0b3-2315f02ab31e",
        "Result": "-4"
    }
}
```

