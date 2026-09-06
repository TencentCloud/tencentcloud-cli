**Example 1: 修改BYOK的ApiBase**



Input: 

```
tccli clb ModifyModelAttributes --cli-unfold-argument  \
    --ServiceProviderId byok-gr0ec33g \
    --ApiBases.0.Protocol chat \
    --ApiBases.0.ApiBase http://example11.com
```

Output: 
```
{
    "Response": {
        "RequestId": "e2df872c-1292-4252-8207-e9c9c11dce23"
    }
}
```

**Example 2: 修改BYOK的Name**



Input: 

```
tccli clb ModifyModelAttributes --cli-unfold-argument  \
    --ServiceProviderId byok-2a30o5mp \
    --ServiceProviderName panda
```

Output: 
```
{
    "Response": {
        "RequestId": "ee81f905-88fa-4ace-bcb9-cd9ea6fd7ef4"
    }
}
```

**Example 3: 非chat场景修改BYOK的ApiBase**



Input: 

```
tccli clb ModifyModelAttributes --cli-unfold-argument  \
    --ServiceProviderId byok-m8qfiaju \
    --ApiBase https://embedding-placeholder.example11.com \
    --EndpointPath /emt
```

Output: 
```
{
    "Response": {
        "RequestId": "e3cae64e-df42-4011-be0d-c9b651928648"
    }
}
```

