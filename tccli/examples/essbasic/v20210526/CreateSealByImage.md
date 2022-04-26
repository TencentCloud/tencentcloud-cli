**Example 1: 渠道通过图片为子客代创建印章**



Input: 

```
tccli essbasic CreateSealByImage --cli-unfold-argument  \
    --SealImage base64 \
    --SealName 测试 \
    --Agent.ProxyAppId c17bdf9c2a7bdcb32611f4d0200fef3d \
    --Agent.ProxyOrganizationId xx \
    --Agent.ProxyOperator.OpenId 00498cc8500be9cxxxxxxx3aff766cac \
    --Agent.ProxyOperator.ClientIp 8.8.8.8 \
    --Agent.ProxyOrganizationOpenId d7c13a8b81340cce9e3968c0ee248f04 \
    --Agent.AppId 65fb0c591044be8a1f60aa382cc5ed0e
```

Output: 
```
{
    "Response": {
        "SealId": "",
        "RequestId": "s1629442787650001803"
    }
}
```

