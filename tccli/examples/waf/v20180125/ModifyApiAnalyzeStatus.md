**Example 1: api分析页面开关**

api分析页面开关

Input: 

```
tccli waf ModifyApiAnalyzeStatus --cli-unfold-argument  \
    --Status 1 \
    --Domain qcloudwaf.com
```

Output: 
```
{
    "Response": {
        "Count": 0,
        "UnSupportedList": [
            "qcloudwaf.com"
        ],
        "FailDomainList": [
            "qcloudwaf.com"
        ],
        "RequestId": "asdqwweqxczca1231vszdfas"
    }
}
```

