**Example 1: 检查免费证书申请结果，免费证书申请失败**

针对站点（ZoneId 为 zone-28v607hq8d3m）下的域名（cc.xzone.cloud）在触发申请免费证书后，检查免费证书是否申请成功。

Input: 

```
tccli teo CheckFreeCertificateVerification --cli-unfold-argument  \
    --ZoneId zone-28v607hq8d3m \
    --Domain cc.xzone.cloud
```

Output: 
```
{
    "Response": {
        "Error": {
            "Code": "ResourceUnavailable.RecordUnExpected",
            "Message": "无法正确检测到验证值，请检查当前域名是否配置了分区域解析或者安全策略拦截。"
        },
        "RequestId": "ed93f3cb-f35e-473f-b9f3-0d451b8b79c6"
    }
}
```

**Example 2: 检查免费证书申请结果，免费证书申请成功**

针对站点（ZoneId 为 zone-28v607hq8d3m）下的域名（aa.xzone.cloud）在触发申请免费证书后，检查免费证书是否申请成功。

Input: 

```
tccli teo CheckFreeCertificateVerification --cli-unfold-argument  \
    --ZoneId zone-28v607hq8d3m \
    --Domain aa.xzone.cloud
```

Output: 
```
{
    "Response": {
        "RequestId": "dc1ba58b-4e4e-4a71-bed6-2b777c48d17e",
        "CommonName": "aa.xzone.cloud",
        "SignatureAlgorithm": "RSA 2048",
        "ExpireTime": "2025-07-31T07:06:57Z"
    }
}
```

