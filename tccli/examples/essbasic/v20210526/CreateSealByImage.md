**Example 1: 第三方应用平台通过图片为第三方平台子客企业代创建印章**

第三方应用平台通过图片为第三方平台子客企业代创建印章，需要电子签人工审核

Input: 

```
tccli essbasic CreateSealByImage --cli-unfold-argument  \
    --SealImage base64 \
    --SealName 测试 \
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

