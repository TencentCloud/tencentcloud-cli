**Example 1: 创建认证选项配置**

新建一个认证选项配置。

Input: 

```
tccli teo CreateSecurityClientAttester --cli-unfold-argument  \
    --ZoneId zone-123123322 \
    --ClientAttesters.0.Name test \
    --ClientAttesters.0.AttesterSource TC-RCE \
    --ClientAttesters.0.TCRCEOption.Channel 12399223 \
    --ClientAttesters.0.AttesterDuration 300s
```

Output: 
```
{
    "Response": {
        "ClientAttesterIds": [
            "attest-2184008405"
        ],
        "RequestId": "ddf831fc-cf45-40fe-81b0-2d9cdd4c1bd6"
    }
}
```

