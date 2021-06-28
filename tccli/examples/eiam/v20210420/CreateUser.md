**Example 1: 请求示例**



Input: 

```
tccli eiam CreateUser --cli-unfold-argument  \
    --UserName 新建用户03 \
    --DisplayName 接口创建用户 \
    --Description 接口创建用户 \
    --Phone +86-13312546881 \
    --OrgNodeId 7999987a-c9dc-4dd2-b3e2-b52f53317aa6 \
    --ExpirationTime 2022-01-18T09:44:07.182+0000 \
    --Password qqWW22@@ \
    --Email 632542556@qq.com \
    --PwdNeedReset true
```

Output: 
```
{
    "Response": {
        "RequestId": "a31e9877-f195-45f9-9765-0f36e005ceea",
        "UserId": "2877f61b-3467-46f4-a6cb-eebd3cce660a"
    }
}
```

