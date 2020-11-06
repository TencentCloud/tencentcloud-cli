**Example 1: 认证通过示例 [前往调试工具](https://console.cloud.tencent.com/api/explorer?Product=faceid&Version=2018-03-01&Action=PhoneVerification&SignVe**



Input: 

```
tccli faceid PhoneVerification --cli-unfold-argument  \
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
        "RequestId": "a5fdb909-5ee6-43ff-a152-bb1b9744ee8b"
    }
}
```

