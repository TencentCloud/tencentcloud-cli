**Example 1: 示例**

批量注册用户

Input: 

```
tccli lcic BatchRegister --cli-unfold-argument  \
    --Users.0.SdkAppId 190912 \
    --Users.0.Name test \
    --Users.0.OriginId use109 \
    --Users.0.Avatar http://user.com？pic=123
```

Output: 
```
{
    "Response": {
        "Users": [
            {
                "SdkAppId": 1091,
                "UserId": "58HJKL908",
                "OriginId": "58HJKL908"
            }
        ],
        "RequestId": "e574aae1-lp02-4225-a2f8-9032h7199f5f0"
    }
}
```

