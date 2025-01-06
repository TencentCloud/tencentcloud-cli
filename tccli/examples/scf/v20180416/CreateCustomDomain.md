**Example 1: 示例1**

创建一个自定义域名，关闭了waf防护，路由配置开启重写策略，该策略是通配符匹配替换。

Input: 

```
tccli scf CreateCustomDomain --cli-unfold-argument  \
    --Domain www.ccc.com \
    --Protocol HTTP&HTTPS \
    --CertConfig.CertificateId BxxJ3DK7 \
    --EndpointsConfig.0.PathMatch /aa/* \
    --EndpointsConfig.0.Namespace default \
    --EndpointsConfig.0.FunctionName test1 \
    --EndpointsConfig.0.Qualifier $LATEST \
    --EndpointsConfig.0.PathRewrite.0.Path /aa/bb/* \
    --EndpointsConfig.0.PathRewrite.0.Type WildcardRules \
    --EndpointsConfig.0.PathRewrite.0.Rewrite /$ \
    --WafConfig.WafOpen CLOSE \
    --WafConfig.WafInstanceId waf_2kzh3vlq0umkkha9
```

Output: 
```
{
    "Response": {
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

**Example 2: 示例2**

创建一个自定义域名，开启了waf 防护，路由配置开启重写策略，该策略是精确路径匹配替换。

Input: 

```
tccli scf CreateCustomDomain --cli-unfold-argument  \
    --Domain www.ccc.com \
    --Protocol HTTP&HTTPS \
    --CertConfig.CertificateId BxxJ3DK7 \
    --EndpointsConfig.0.PathMatch /aa/ \
    --EndpointsConfig.0.Namespace default \
    --EndpointsConfig.0.FunctionName test1 \
    --EndpointsConfig.0.Qualifier 1 \
    --EndpointsConfig.0.PathRewrite.0.Path /aa/ \
    --EndpointsConfig.0.PathRewrite.0.Type WildcardRules \
    --EndpointsConfig.0.PathRewrite.0.Rewrite /$ \
    --WafConfig.WafOpen OPEN \
    --WafConfig.WafInstanceId waf_2kzh3vlq0umkkha9
```

Output: 
```
{
    "Response": {
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

