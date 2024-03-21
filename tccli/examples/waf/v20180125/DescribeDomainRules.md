**Example 1: 拉取域名放回规则列表**

拉取域名放回规则列表

Input: 

```
tccli waf DescribeDomainRules --cli-unfold-argument  \
    --Domain test.qcloudwaf.com
```

Output: 
```
{
    "Response": {
        "Rules": [
            {
                "Id": 1,
                "Type": "XSS",
                "Level": "宽松",
                "Description": "test",
                "CVE": "CVE-2020-14568",
                "Status": 0,
                "ModifyTime": "2020-07-28 00:00:00",
                "AddTime": "2020-07-27 00:00:00"
            }
        ],
        "RequestId": "46757c6e-786c-48ca-b5c4-9fa29ece1c9e"
    }
}
```

