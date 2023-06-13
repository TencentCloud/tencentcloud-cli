**Example 1: 一键接入**

一键接入 waf

Input: 

```
tccli waf AccessSpartaProtection --cli-unfold-argument  \
    --Domains abc \
    --InstanceID abc \
    --AppIdInner 0 \
    --UinInner abc
```

Output: 
```
{
    "Response": {
        "FailedMsg": "abc",
        "RequestId": "abc"
    }
}
```

