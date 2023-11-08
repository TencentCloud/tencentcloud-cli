**Example 1: 修改模块状态**



Input: 

```
tccli waf ModifyModuleStatus --cli-unfold-argument  \
    --Domain zjm.qcloudwaf.com \
    --WebSecurity 1 \
    --AccessControl 1 \
    --CcProtection 1 \
    --AntiTamper 1 \
    --AntiLeakage 1 \
    --ApiProtection 1
```

Output: 
```
{
    "Response": {
        "RequestId": "abc-edf"
    }
}
```

