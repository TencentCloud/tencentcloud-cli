**Example 1: 修改模型路由实例名称**



Input: 

```
tccli clb ModifyModelRouterAttributes --cli-unfold-argument  \
    --ModelRouterId cmr-h2tdbhtz \
    --ModelRouterName 测试模型路由名称
```

Output: 
```
{
    "Response": {
        "RequestId": "34c0e8fc-1ad7-4599-bcc4-f312f0ec22f1"
    }
}
```

**Example 2: 替换实例的 HTTPS 证书**

将企业型实例 HTTPS 服务端点绑定的证书替换为 SCkPG15A，替换后立即生效。仅企业型且服务端点为 HTTPS 的实例支持。

Input: 

```
tccli clb ModifyModelRouterAttributes --cli-unfold-argument  \
    --ModelRouterId cmr-h2tdbhtz \
    --CertId SCkPG15A
```

Output: 
```
{
    "Response": {
        "RequestId": "34c0e8fc-1ad7-4599-bcc4-f312f0ec22f1"
    }
}
```

