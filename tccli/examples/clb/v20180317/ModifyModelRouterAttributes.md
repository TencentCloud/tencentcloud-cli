**Example 1: 修改CMR实例级别请求的L2路由算法近优带参数**

修改CMR实例级别请求的L2路由算法近优带参数

Input: 

```
tccli clb ModifyModelRouterAttributes --cli-unfold-argument  \
    --ModelRouterId cmr-mwmjm160 \
    --RouterSetting.NumRetries 4 \
    --RouterSetting.RoutingStrategyArgs.LeastBusyBuffer 0.1 \
    --RouterSetting.RoutingStrategyArgs.UsageBasedBuffer 0.1
```

Output: 
```
{
    "Response": {
        "RequestId": "4c407677-bd5b-4061-8af9-fa783ba3bcdb"
    }
}
```

**Example 2: 修改CMR实例级别请求的模型组内重试次数**

修改CMR实例级别请求的模型组内重试次数

Input: 

```
tccli clb ModifyModelRouterAttributes --cli-unfold-argument  \
    --ModelRouterId cmr-mwmjm160 \
    --RouterSetting.NumRetries 2
```

Output: 
```
{
    "Response": {
        "RequestId": "de181087-5d94-4bb3-8fe8-83127a0ed434"
    }
}
```

**Example 3: 修改模型路由实例名称**



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

**Example 4: 替换实例的 HTTPS 证书**

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

