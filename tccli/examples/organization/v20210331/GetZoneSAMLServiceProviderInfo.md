**Example 1: 查询SAML服务提供商配置信息**

查询SAML服务提供商配置信息

Input: 

```
tccli organization GetZoneSAMLServiceProviderInfo --cli-unfold-argument  \
    --ZoneId z-di3d9em***
```

Output: 
```
{
    "Response": {
        "SAMLServiceProvider": {
            "EntityId": "https://tencentcloudsso.com/saml/sp/z-doekeie****",
            "ZoneId": "z-doekeie****",
            "EncodedMetadataDocument": "JTNDJTNGeG1sJTIwdmVyc2lvbiUzRCUyMjEuMCUyMiUyMGVuY29kaW5nJTNEJTIy***",
            "AcsUrl": "https://tencentcloudsso.com/saml/acs/d9wjd-d93je9-2me****"
        },
        "RequestId": "e297543a-80de-4039-83c8-9d324545"
    }
}
```

