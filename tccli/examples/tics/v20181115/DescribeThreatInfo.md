**Example 1: 查询域名是否失陷**

根据域名，查询该域名是否失陷及相关信息

Input: 

```
tccli tics DescribeThreatInfo --cli-unfold-argument  \
    --Key 003143.sdyintong.com \
    --Type domain \
    --Option 0
```

Output: 
```
{
    "Response": {
        "ReturnCode": 0,
        "Result": "black",
        "Confidence": 90,
        "ThreatTypes": [
            "malware site"
        ],
        "Tags": [],
        "Status": "inactive",
        "Context": "",
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

