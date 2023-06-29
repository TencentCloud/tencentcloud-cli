**Example 1: 服务修改自定义域名**

服务修改自定义域名

Input: 

```
tccli apigateway ModifySubDomain --cli-unfold-argument  \
    --ServiceId service-19c5fnhy \
    --SubDomain doagkfrf.flyfly.wang \
    --CertificateId '' \
    --IsDefaultMapping false \
    --Protocol http \
    --NetType OUTER \
    --PathMappingSet.0.Path / \
    --PathMappingSet.0.Environment release
```

Output: 
```
{
    "Response": {
        "Result": true,
        "RequestId": "d7f6116b-8184-4bdd-8fbe-1ecbcfa1ea30"
    }
}
```

