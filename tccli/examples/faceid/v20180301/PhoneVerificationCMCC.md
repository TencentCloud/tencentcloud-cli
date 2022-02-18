**Example 1: 示例**



Input: 

```
tccli faceid PhoneVerificationCMCC --cli-unfold-argument  \
    --IdCard 440111201903211111 \
    --Name 张三 \
    --Phone 13000000000
```

Output: 
```
{
    "Response": {
        "Result": "0",
        "Description": "认证通过",
        "Isp": "移动",
        "RequestId": "a5fdb909-5ee6-43ff-a152-bb1b9744ee8b"
    }
}
```

