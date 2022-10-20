**Example 1: 查询木马自动隔离样本详情**



Input: 

```
tccli tcss DescribeVirusAutoIsolateSampleDetail --cli-unfold-argument  \
    --MD5 dskaldjskld
```

Output: 
```
{
    "Response": {
        "Tags": [
            "xx"
        ],
        "RiskLevel": "xx",
        "VirusName": "xx",
        "RequestId": "xx",
        "ReferenceLink": "xx",
        "MD5": "xx",
        "KillEngine": [
            "xx"
        ],
        "HarmDescribe": "xx",
        "SuggestScheme": "xx",
        "Size": 1
    }
}
```

