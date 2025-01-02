**Example 1: 辅诊登录**

获取访问token

Input: 

```
tccli aca LoginHisTool --cli-unfold-argument  \
    --Header.HospitalId test001 \
    --Header.PartnerId 1 \
    --Header.Timestamp 1731555285331 \
    --Header.Signature c5146247bc621087037e41952de50ccdcee0a69972cbd8a9cd3631ce79ed91ba \
    --Header.PlatformId 800035384 \
    --Data.DoctorId 001 \
    --Data.DoctorName 张三
```

Output: 
```
{
    "Response": {
        "Code": 0,
        "Data": {
            "ExpiresIn": 72000,
            "Timestamp": 0,
            "Token": "tai.4d563878587a67774d44417a4e544d344e413d3d.3ab846e50ec343249fdacba4c79e5ff1"
        },
        "Message": "success",
        "RequestId": "643e3fe3-4ea0-4fcb-b539-f60f7d428bac"
    }
}
```

