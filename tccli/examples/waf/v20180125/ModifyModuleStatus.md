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
        "RequestId": "46757c6e-786c-48ca-b5c4-9fa29ece1c9e"
    }
}
```

