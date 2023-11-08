**Example 1: 查询某个domain的基础安全模块开关状态**



Input: 

```
tccli waf DescribeModuleStatus --cli-unfold-argument  \
    --Domain test.qcloudwaf.com
```

Output: 
```
{
    "Response": {
        "AccessControl": 1,
        "AntiLeakage": 1,
        "WebSecurity": 1,
        "ApiProtection": 1,
        "CcProtection": 1,
        "AntiTamper": 1,
        "RequestId": "46757c6e-786c-48ca-b5c4-9fa29ece1c9e"
    }
}
```

