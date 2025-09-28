**Example 1: 创建七层加速规则**

创建一条七层加速规则。

Input: 

```
tccli teo CreateL7AccRules --cli-unfold-argument  \
    --ZoneId zone-27q0p0bali12 \
    --Rules.0.RuleName 测试规则 \
    --Rules.0.Status disable \
    --Rules.0.Description '注释 1' '注释 2' \
    --Rules.0.Branches.0.Condition ${http.request.host} in ['www.example.com'] \
    --Rules.0.Branches.0.Actions.0.Name ModifyOrigin \
    --Rules.0.Branches.0.Actions.0.ModifyOriginParameters.OriginType IPDomain \
    --Rules.0.Branches.0.Actions.0.ModifyOriginParameters.Origin 1.1.1.1 \
    --Rules.0.Branches.0.Actions.0.ModifyOriginParameters.OriginProtocol follow \
    --Rules.0.Branches.0.Actions.0.ModifyOriginParameters.HTTPOriginPort 80 \
    --Rules.0.Branches.0.Actions.0.ModifyOriginParameters.HTTPSOriginPort 443 \
    --Rules.0.Branches.0.SubRules.0.Description 节点缓存TTL示例 \
    --Rules.0.Branches.0.SubRules.0.Branches.0.Condition ${http.request.host} in ['www.example.com'] \
    --Rules.0.Branches.0.SubRules.0.Branches.0.Actions.0.Name Cache \
    --Rules.0.Branches.0.SubRules.0.Branches.0.Actions.0.CacheParameters.FollowOrigin.Switch on \
    --Rules.0.Branches.0.SubRules.0.Branches.0.Actions.0.CacheParameters.FollowOrigin.DefaultCache on \
    --Rules.0.Branches.0.SubRules.0.Branches.0.Actions.0.CacheParameters.FollowOrigin.DefaultCacheStrategy on \
    --Rules.0.Branches.0.SubRules.0.Branches.0.Actions.0.CacheParameters.FollowOrigin.DefaultCacheTime 0 \
    --Rules.0.Branches.0.SubRules.1.Description 浏览器缓存TTL示例 \
    --Rules.0.Branches.0.SubRules.1.Branches.0.Condition ${http.request.host} in ['www.example.com'] \
    --Rules.0.Branches.0.SubRules.1.Branches.0.Actions.0.Name MaxAge \
    --Rules.0.Branches.0.SubRules.1.Branches.0.Actions.0.MaxAgeParameters.FollowOrigin off \
    --Rules.0.Branches.0.SubRules.1.Branches.0.Actions.0.MaxAgeParameters.CacheTime 0 \
    --Rules.0.Branches.0.SubRules.2.Description 自定义CacheKey示例 \
    --Rules.0.Branches.0.SubRules.2.Branches.0.Condition ${http.request.host} in ['www.example.com'] \
    --Rules.0.Branches.0.SubRules.2.Branches.0.Actions.0.Name CacheKey \
    --Rules.0.Branches.0.SubRules.2.Branches.0.Actions.0.CacheKeyParameters.FullURLCache off \
    --Rules.0.Branches.0.SubRules.2.Branches.0.Actions.0.CacheKeyParameters.QueryString.Switch on \
    --Rules.0.Branches.0.SubRules.2.Branches.0.Actions.0.CacheKeyParameters.QueryString.Action includeCustom \
    --Rules.0.Branches.0.SubRules.2.Branches.0.Actions.0.CacheKeyParameters.QueryString.Values name1 name2 \
    --Rules.0.Branches.0.SubRules.2.Branches.0.Actions.0.CacheKeyParameters.IgnoreCase on \
    --Rules.0.Branches.0.SubRules.2.Branches.0.Actions.0.CacheKeyParameters.Header.Switch on \
    --Rules.0.Branches.0.SubRules.2.Branches.0.Actions.0.CacheKeyParameters.Header.Values EO-Client-Device EO-Client-OS \
    --Rules.0.Branches.0.SubRules.2.Branches.0.Actions.0.CacheKeyParameters.Scheme on \
    --Rules.0.Branches.0.SubRules.2.Branches.0.Actions.0.CacheKeyParameters.Cookie.Switch off \
    --Rules.0.Branches.0.SubRules.3.Description 状态码缓存TTL示例 \
    --Rules.0.Branches.0.SubRules.3.Branches.0.Condition ${http.request.host} in ['www.example.com'] \
    --Rules.0.Branches.0.SubRules.3.Branches.0.Actions.0.Name StatusCodeCache \
    --Rules.0.Branches.0.SubRules.3.Branches.0.Actions.0.StatusCodeCacheParameters.StatusCodeCacheParams.0.StatusCode 400 \
    --Rules.0.Branches.0.SubRules.3.Branches.0.Actions.0.StatusCodeCacheParameters.StatusCodeCacheParams.0.CacheTime 4 \
    --Rules.0.Branches.0.SubRules.3.Branches.0.Actions.0.StatusCodeCacheParameters.StatusCodeCacheParams.1.StatusCode 401 \
    --Rules.0.Branches.0.SubRules.3.Branches.0.Actions.0.StatusCodeCacheParameters.StatusCodeCacheParams.1.CacheTime 180 \
    --Rules.0.Branches.0.SubRules.3.Branches.0.Actions.0.StatusCodeCacheParameters.StatusCodeCacheParams.2.StatusCode 403 \
    --Rules.0.Branches.0.SubRules.3.Branches.0.Actions.0.StatusCodeCacheParameters.StatusCodeCacheParams.2.CacheTime 7200 \
    --Rules.0.Branches.0.SubRules.3.Branches.0.Actions.0.StatusCodeCacheParameters.StatusCodeCacheParams.3.StatusCode 404 \
    --Rules.0.Branches.0.SubRules.3.Branches.0.Actions.0.StatusCodeCacheParameters.StatusCodeCacheParams.3.CacheTime 86400 \
    --Rules.0.Branches.0.SubRules.4.Description 缓存预刷新示例 \
    --Rules.0.Branches.0.SubRules.4.Branches.0.Condition ${http.request.host} in ['www.example.com'] \
    --Rules.0.Branches.0.SubRules.4.Branches.0.Actions.0.Name CachePrefresh \
    --Rules.0.Branches.0.SubRules.4.Branches.0.Actions.0.CachePrefreshParameters.Switch on \
    --Rules.0.Branches.0.SubRules.4.Branches.0.Actions.0.CachePrefreshParameters.CacheTimePercent 80 \
    --Rules.0.Branches.0.SubRules.5.Description 离线缓存示例 \
    --Rules.0.Branches.0.SubRules.5.Branches.0.Condition ${http.request.host} in ['www.example.com'] \
    --Rules.0.Branches.0.SubRules.5.Branches.0.Actions.0.Name OfflineCache \
    --Rules.0.Branches.0.SubRules.5.Branches.0.Actions.0.OfflineCacheParameters.Switch on \
    --Rules.0.Branches.0.SubRules.6.Description HTTP2示例 \
    --Rules.0.Branches.0.SubRules.6.Branches.0.Condition ${http.request.host} in ['www.example.com'] \
    --Rules.0.Branches.0.SubRules.6.Branches.0.Actions.0.Name HTTP2 \
    --Rules.0.Branches.0.SubRules.6.Branches.0.Actions.0.HTTP2Parameters.Switch on \
    --Rules.0.Branches.0.SubRules.7.Description QUIC示例 \
    --Rules.0.Branches.0.SubRules.7.Branches.0.Condition ${http.request.host} in ['www.example.com'] \
    --Rules.0.Branches.0.SubRules.7.Branches.0.Actions.0.Name QUIC \
    --Rules.0.Branches.0.SubRules.7.Branches.0.Actions.0.QUICParameters.Switch on \
    --Rules.0.Branches.0.SubRules.8.Description WebSocket示例 \
    --Rules.0.Branches.0.SubRules.8.Branches.0.Condition ${http.request.host} in ['www.example.com'] \
    --Rules.0.Branches.0.SubRules.8.Branches.0.Actions.0.Name WebSocket \
    --Rules.0.Branches.0.SubRules.8.Branches.0.Actions.0.WebSocketParameters.Switch on \
    --Rules.0.Branches.0.SubRules.8.Branches.0.Actions.0.WebSocketParameters.Timeout 30 \
    --Rules.0.Branches.0.SubRules.9.Description 最大上传大小示例 \
    --Rules.0.Branches.0.SubRules.9.Branches.0.Condition ${http.request.host} in ['www.example.com'] \
    --Rules.0.Branches.0.SubRules.9.Branches.0.Actions.0.Name PostMaxSize \
    --Rules.0.Branches.0.SubRules.9.Branches.0.Actions.0.PostMaxSizeParameters.Switch on \
    --Rules.0.Branches.0.SubRules.9.Branches.0.Actions.0.PostMaxSizeParameters.MaxSize 524288000 \
    --Rules.0.Branches.0.SubRules.10.Description 智能压缩示例 \
    --Rules.0.Branches.0.SubRules.10.Branches.0.Condition ${http.request.host} in ['www.example.com'] \
    --Rules.0.Branches.0.SubRules.10.Branches.0.Actions.0.Name Compression \
    --Rules.0.Branches.0.SubRules.10.Branches.0.Actions.0.CompressionParameters.Switch on \
    --Rules.0.Branches.0.SubRules.10.Branches.0.Actions.0.CompressionParameters.Algorithms gzip \
    --Rules.0.Branches.0.SubRules.11.Description 智能加速示例 \
    --Rules.0.Branches.0.SubRules.11.Branches.0.Condition ${http.request.host} in ['www.example.com'] \
    --Rules.0.Branches.0.SubRules.11.Branches.0.Actions.0.Name SmartRouting \
    --Rules.0.Branches.0.SubRules.11.Branches.0.Actions.0.SmartRoutingParameters.Switch on \
    --Rules.0.Branches.0.SubRules.12.Description HTTP2回源示例 \
    --Rules.0.Branches.0.SubRules.12.Branches.0.Condition ${http.request.host} in ['www.example.com'] \
    --Rules.0.Branches.0.SubRules.12.Branches.0.Actions.0.Name UpstreamHTTP2 \
    --Rules.0.Branches.0.SubRules.12.Branches.0.Actions.0.UpstreamHTTP2Parameters.Switch off \
    --Rules.0.Branches.0.SubRules.13.Description 回源超时时间示例 \
    --Rules.0.Branches.0.SubRules.13.Branches.0.Condition ${http.request.host} in ['www.example.com'] \
    --Rules.0.Branches.0.SubRules.13.Branches.0.Actions.0.Name HTTPUpstreamTimeout \
    --Rules.0.Branches.0.SubRules.13.Branches.0.Actions.0.HTTPUpstreamTimeoutParameters.ResponseTimeout 15 \
    --Rules.0.Branches.0.SubRules.14.Description '强制 HTTPS示例' \
    --Rules.0.Branches.0.SubRules.14.Branches.0.Condition ${http.request.host} in ['www.example.com'] \
    --Rules.0.Branches.0.SubRules.14.Branches.0.Actions.0.Name ForceRedirectHTTPS \
    --Rules.0.Branches.0.SubRules.14.Branches.0.Actions.0.ForceRedirectHTTPSParameters.Switch on \
    --Rules.0.Branches.0.SubRules.14.Branches.0.Actions.0.ForceRedirectHTTPSParameters.RedirectStatusCode 302 \
    --Rules.0.Branches.0.SubRules.15.Description HSTS示例 \
    --Rules.0.Branches.0.SubRules.15.Branches.0.Condition ${http.request.host} in ['www.example.com'] \
    --Rules.0.Branches.0.SubRules.15.Branches.0.Actions.0.Name HSTS \
    --Rules.0.Branches.0.SubRules.15.Branches.0.Actions.0.HSTSParameters.Switch on \
    --Rules.0.Branches.0.SubRules.15.Branches.0.Actions.0.HSTSParameters.Timeout 1000 \
    --Rules.0.Branches.0.SubRules.15.Branches.0.Actions.0.HSTSParameters.IncludeSubDomains on \
    --Rules.0.Branches.0.SubRules.15.Branches.0.Actions.0.HSTSParameters.Preload on \
    --Rules.0.Branches.0.SubRules.16.Description 'SSL/TLS 安全配置示例' \
    --Rules.0.Branches.0.SubRules.16.Branches.0.Condition ${http.request.host} in ['www.example.com'] \
    --Rules.0.Branches.0.SubRules.16.Branches.0.Actions.0.Name TLSConfig \
    --Rules.0.Branches.0.SubRules.16.Branches.0.Actions.0.TLSConfigParameters.Version TLSv1 TLSv1.1 TLSv1.2 TLSv1.3 \
    --Rules.0.Branches.0.SubRules.16.Branches.0.Actions.0.TLSConfigParameters.CipherSuite loose-v2023 \
    --Rules.0.Branches.0.SubRules.17.Description 'OCSP 装订示例' 回源请求参数设置示例 回源跟随重定向示例 自定义错误页面示例 分片回源示例 \
    --Rules.0.Branches.0.SubRules.17.Branches.0.Condition ${http.request.host} in ['www.example.com'] \
    --Rules.0.Branches.0.SubRules.17.Branches.0.Actions.0.Name OCSPStapling \
    --Rules.0.Branches.0.SubRules.17.Branches.0.Actions.0.OCSPStaplingParameters.Switch on \
    --Rules.0.Branches.0.SubRules.17.Branches.0.Actions.1.Name UpstreamRequest \
    --Rules.0.Branches.0.SubRules.17.Branches.0.Actions.1.UpstreamRequestParameters.QueryString.Switch on \
    --Rules.0.Branches.0.SubRules.17.Branches.0.Actions.1.UpstreamRequestParameters.QueryString.Action includeCustom \
    --Rules.0.Branches.0.SubRules.17.Branches.0.Actions.1.UpstreamRequestParameters.QueryString.Values name1 name2 \
    --Rules.0.Branches.0.SubRules.17.Branches.0.Actions.1.UpstreamRequestParameters.Cookie.Switch on \
    --Rules.0.Branches.0.SubRules.17.Branches.0.Actions.1.UpstreamRequestParameters.Cookie.Action full \
    --Rules.0.Branches.0.SubRules.17.Branches.0.Actions.2.Name UpstreamFollowRedirect \
    --Rules.0.Branches.0.SubRules.17.Branches.0.Actions.2.UpstreamFollowRedirectParameters.Switch on \
    --Rules.0.Branches.0.SubRules.17.Branches.0.Actions.2.UpstreamFollowRedirectParameters.MaxTimes 3 \
    --Rules.0.Branches.0.SubRules.17.Branches.0.Actions.3.Name ErrorPage \
    --Rules.0.Branches.0.SubRules.17.Branches.0.Actions.3.ErrorPageParameters.ErrorPageParams.0.StatusCode 400 \
    --Rules.0.Branches.0.SubRules.17.Branches.0.Actions.3.ErrorPageParameters.ErrorPageParams.0.RedirectURL http://www.test-v.com/custom-page.html \
    --Rules.0.Branches.0.SubRules.17.Branches.0.Actions.3.ErrorPageParameters.ErrorPageParams.1.StatusCode 403 \
    --Rules.0.Branches.0.SubRules.17.Branches.0.Actions.3.ErrorPageParameters.ErrorPageParams.1.RedirectURL http://www.test-v.com/custom-page1.html \
    --Rules.0.Branches.0.SubRules.17.Branches.0.Actions.4.Name RangeOriginPull \
    --Rules.0.Branches.0.SubRules.17.Branches.0.Actions.4.RangeOriginPullParameters.Switch on \
    --Rules.0.Branches.0.SubRules.18.Description '回源 HTTPS示例' '修改 HTTP 回源请求头示例' 'Host Header 重写示例' '访问 URL 重定向示例' 'Token 鉴权示例' \
    --Rules.0.Branches.0.SubRules.18.Branches.0.Condition ${http.request.host} in ['www.example.com'] \
    --Rules.0.Branches.0.SubRules.18.Branches.0.Actions.0.Name OriginPullProtocol \
    --Rules.0.Branches.0.SubRules.18.Branches.0.Actions.0.OriginPullProtocolParameters.Protocol follow \
    --Rules.0.Branches.0.SubRules.18.Branches.0.Actions.1.Name ModifyRequestHeader \
    --Rules.0.Branches.0.SubRules.18.Branches.0.Actions.1.ModifyRequestHeaderParameters.HeaderActions.0.Action add \
    --Rules.0.Branches.0.SubRules.18.Branches.0.Actions.1.ModifyRequestHeaderParameters.HeaderActions.0.Name EO-Client-Browser \
    --Rules.0.Branches.0.SubRules.18.Branches.0.Actions.1.ModifyRequestHeaderParameters.HeaderActions.1.Action del \
    --Rules.0.Branches.0.SubRules.18.Branches.0.Actions.1.ModifyRequestHeaderParameters.HeaderActions.1.Name EO-Client-Device \
    --Rules.0.Branches.0.SubRules.18.Branches.0.Actions.1.ModifyRequestHeaderParameters.HeaderActions.2.Action set \
    --Rules.0.Branches.0.SubRules.18.Branches.0.Actions.1.ModifyRequestHeaderParameters.HeaderActions.2.Name EO-Client-OS \
    --Rules.0.Branches.0.SubRules.18.Branches.0.Actions.2.Name HostHeader \
    --Rules.0.Branches.0.SubRules.18.Branches.0.Actions.2.HostHeaderParameters.Action followOrigin \
    --Rules.0.Branches.0.SubRules.18.Branches.0.Actions.3.Name AccessURLRedirect \
    --Rules.0.Branches.0.SubRules.18.Branches.0.Actions.3.AccessURLRedirectParameters.StatusCode 302 \
    --Rules.0.Branches.0.SubRules.18.Branches.0.Actions.3.AccessURLRedirectParameters.Protocol follow \
    --Rules.0.Branches.0.SubRules.18.Branches.0.Actions.3.AccessURLRedirectParameters.HostName.Action follow \
    --Rules.0.Branches.0.SubRules.18.Branches.0.Actions.3.AccessURLRedirectParameters.URLPath.Action follow \
    --Rules.0.Branches.0.SubRules.18.Branches.0.Actions.3.AccessURLRedirectParameters.QueryString.Action full \
    --Rules.0.Branches.0.SubRules.18.Branches.0.Actions.4.Name Authentication \
    --Rules.0.Branches.0.SubRules.18.Branches.0.Actions.4.AuthenticationParameters.AuthType TypeA \
    --Rules.0.Branches.0.SubRules.18.Branches.0.Actions.4.AuthenticationParameters.Timeout 5 \
    --Rules.0.Branches.0.SubRules.18.Branches.0.Actions.4.AuthenticationParameters.SecretKey BCChgIM4o0k08Uk0Jgi3f27ir3 \
    --Rules.0.Branches.0.SubRules.18.Branches.0.Actions.4.AuthenticationParameters.BackupSecretKey 3deJ7O6CsqlIk \
    --Rules.0.Branches.0.SubRules.18.Branches.0.Actions.4.AuthenticationParameters.AuthParam test123QQ \
    --Rules.0.Branches.0.SubRules.19.Description '修改 HTTP 节点响应头示例' '客户端 IP 头部示例' '客户端 IP 地理位置头部示例' 'HTTP 应答示例' '回源 URL 重写示例' \
    --Rules.0.Branches.0.SubRules.19.Branches.0.Condition ${http.request.host} in ['www.example.com'] \
    --Rules.0.Branches.0.SubRules.19.Branches.0.Actions.0.Name ModifyResponseHeader \
    --Rules.0.Branches.0.SubRules.19.Branches.0.Actions.0.ModifyResponseHeaderParameters.HeaderActions.0.Action add \
    --Rules.0.Branches.0.SubRules.19.Branches.0.Actions.0.ModifyResponseHeaderParameters.HeaderActions.0.Name Access-Control-Allow-Methods \
    --Rules.0.Branches.0.SubRules.19.Branches.0.Actions.0.ModifyResponseHeaderParameters.HeaderActions.0.Value POST,GET \
    --Rules.0.Branches.0.SubRules.19.Branches.0.Actions.0.ModifyResponseHeaderParameters.HeaderActions.1.Action set \
    --Rules.0.Branches.0.SubRules.19.Branches.0.Actions.0.ModifyResponseHeaderParameters.HeaderActions.1.Name Access-Control-Allow-Origin \
    --Rules.0.Branches.0.SubRules.19.Branches.0.Actions.0.ModifyResponseHeaderParameters.HeaderActions.1.Value http://test.com,http://1.1.1.1 \
    --Rules.0.Branches.0.SubRules.19.Branches.0.Actions.0.ModifyResponseHeaderParameters.HeaderActions.2.Action del \
    --Rules.0.Branches.0.SubRules.19.Branches.0.Actions.0.ModifyResponseHeaderParameters.HeaderActions.2.Name Content-Disposition \
    --Rules.0.Branches.0.SubRules.19.Branches.0.Actions.1.Name ClientIPHeader \
    --Rules.0.Branches.0.SubRules.19.Branches.0.Actions.1.ClientIPHeaderParameters.Switch on \
    --Rules.0.Branches.0.SubRules.19.Branches.0.Actions.1.ClientIPHeaderParameters.HeaderName testheader \
    --Rules.0.Branches.0.SubRules.19.Branches.0.Actions.2.Name ClientIPCountry \
    --Rules.0.Branches.0.SubRules.19.Branches.0.Actions.2.ClientIPCountryParameters.Switch on \
    --Rules.0.Branches.0.SubRules.19.Branches.0.Actions.2.ClientIPCountryParameters.HeaderName EO-Client-IPCountry \
    --Rules.0.Branches.0.SubRules.19.Branches.0.Actions.3.Name HttpResponse \
    --Rules.0.Branches.0.SubRules.19.Branches.0.Actions.3.HttpResponseParameters.StatusCode 400 \
    --Rules.0.Branches.0.SubRules.19.Branches.0.Actions.3.HttpResponseParameters.ResponsePage p-30tcxgl8i0ls \
    --Rules.0.Branches.0.SubRules.19.Branches.0.Actions.4.Name UpstreamURLRewrite \
    --Rules.0.Branches.0.SubRules.19.Branches.0.Actions.4.UpstreamURLRewriteParameters.Type Path \
    --Rules.0.Branches.0.SubRules.19.Branches.0.Actions.4.UpstreamURLRewriteParameters.Action addPrefix \
    --Rules.0.Branches.0.SubRules.19.Branches.0.Actions.4.UpstreamURLRewriteParameters.Value /prefix
```

Output: 
```
{
    "Response": {
        "RuleIds": [
            "rule-sjuq23"
        ],
        "RequestId": "811d2583-310c-41f4-b5e7-abe407404sxsd"
    }
}
```

