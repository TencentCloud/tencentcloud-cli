**Example 1: 请求示例**



Input: 

```
tccli eiam CreateUser --cli-unfold-argument  \
    --UserName 示例用户 \
    --DisplayName 创建示例用户 \
    --Description 接口创建的示例用户 \
    --Phone +86-133****6881 \
    --OrgNodeId 7999987a-****-4dd2-b3e2-b52f53317aa6 \
    --ExpirationTime 2022-01-18T09:44:07.182+0000 \
    --Password q6E7@#8 \
    --Email 63****2556@qq.com \
    --PwdNeedReset true
```

Output: 
```
{
    "Response": {
        "RequestId": "a31e9877-****-45f9-9765-0f36e005ceea",
        "UserId": "2877f61b-****-46f4-a6cb-eebd3cce660a"
    }
}
```

