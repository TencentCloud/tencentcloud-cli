**Example 1: CreateApp**

我的

Input: 

```
tccli adp CreateApp --cli-unfold-argument  \
    --SpaceId default_space \
    --AppMode 1 \
    --Avatar https://cdn.xiaowei.qq.com/static/adp/app-default-avatar.png \
    --Description 我的描述 \
    --Name 测试的应用信息1
```

Output: 
```
{
    "Response": {
        "AppId": "206*************784",
        "RequestId": "c45d274d-35c9-4ef2-bd0e-33edec89096b"
    }
}
```

