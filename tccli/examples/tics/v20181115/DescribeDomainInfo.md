**Example 1: 查询域名信誉度**

根据域名查询相关的基础信息以及与攻击事件（团伙、家族）、恶意文件等相关联信息。

Input: 

```
tccli tics DescribeDomainInfo --cli-unfold-argument  \
    --Key 003143.sdyintong.com
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
        "Intelligences": [],
        "Context": "",
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

