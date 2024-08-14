**Example 1: 配置SAML身份提供商信息**

配置SAML身份提供商信息

Input: 

```
tccli organization SetExternalSAMLIdentityProvider --cli-unfold-argument  \
    --ZoneId z-d3ideodm*** \
    --EncodedMetadataDocument JTNDJTNGeG1sJTIwdmVyc2lvbiUzRCUyMjEuMCUyMiUyMGVuY29kaW5****** \
    --SSOStatus Enabled \
    --EntityId http://www.okta.com/xd83nd83nd**** \
    --LoginUrl https://dev-xxxxxx.okta.com/app/dev-xxxxxx_cloudssodemo_1/xd83nd83nd****/sso/saml \
    --X509Certificate MIIC8DCCAdigAwIBAgIQP9eomUYGeoND****
```

Output: 
```
{
    "Response": {
        "RequestId": "2ccd7ed1-24b4-4882-8f4a-5580b430bce7"
    }
}
```

