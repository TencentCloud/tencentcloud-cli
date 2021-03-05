**Example 1: 查询IP信誉度**

根据IP查询相关的基础信息以及与攻击事件（团伙、家族）、恶意文件等相关联信息。

Input: 

```
tccli tics DescribeIpInfo --cli-unfold-argument  \
    --Key 8.8.8.8
```

Output: 
```
{
    "Response": {
        "ReturnCode": 0,
        "Result": "white",
        "Confidence": 90,
        "ThreatTypes": [
            "whitelist",
            "IDC"
        ],
        "Tags": [],
        "Intelligences": [
            {}
        ],
        "Context": "",
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

