**Example 1: 一键接入**

一键接入 waf

Input: 

```
tccli waf AccessSpartaProtection --cli-unfold-argument  \
    --Domains txwaf.qcloudwaf.com \
    --InstanceID waf_2kuil2fm02vqm7z2 \
    --AppIdInner 1256704381 \
    --UinInner 100036087831
```

Output: 
```
{
    "Response": {
        "FailedMsg": "Success",
        "RequestId": "dec1ec15-eb62-485f-9f94-985a7f27c3b4"
    }
}
```

