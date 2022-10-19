**Example 1: 渠道通过图片为子客代创建印章**



Input: 

```
tccli essbasic CreateSealByImage --cli-unfold-argument  \
    --SealImage base64 \
    --SealName 测试 \
    --Agent.ProxyAppId c17bdf*****200fef3d \
    --Agent.ProxyOperator.OpenId 00498cc8*********xxx3aff766cac \
    --Agent.ProxyOrganizationOpenId d7c13a8*********968c0ee248f04 \
    --Agent.AppId 65fb0c59*********382cc5ed0e
```

Output: 
```
{
    "Response": {
        "SealId": "",
        "RequestId": "s16294xxxxx0001803"
    }
}
```

