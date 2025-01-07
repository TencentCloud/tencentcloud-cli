**Example 1: 示例**

批量注册用户

Input: 

```
tccli lcic BatchRegister --cli-unfold-argument  \
    --Users.0.SdkAppId 13465287 \
    --Users.0.Name userName \
    --Users.0.OriginId use109 \
    --Users.0.Avatar http://user.com？pic=123
```

Output: 
```
{
    "Response": {
        "Users": [
            {
                "SdkAppId": 13465287,
                "UserId": "2i5WfUzRRC2Eb2uNmLNv96gzxCv",
                "OriginId": "use109"
            }
        ],
        "RequestId": "e574aae1-lp02-4225-a2f8-9032h7199f5f0"
    }
}
```

