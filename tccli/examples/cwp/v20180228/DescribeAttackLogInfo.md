**Example 1: 网络攻击日志详情**

网络攻击日志详情

Input: 

```
tccli cwp DescribeAttackLogInfo --cli-unfold-argument  \
    --Id 1023
```

Output: 
```
{
    "Response": {
        "HttpParam": "xx",
        "DstIp": "xx",
        "HttpCgi": "xx",
        "VulType": "xx",
        "CreatedAt": "xx",
        "SrcPort": 1,
        "HttpHead": "xx",
        "HttpUserAgent": "xx",
        "HttpMethod": "xx",
        "Quuid": "xx",
        "HttpReferer": "xx",
        "SrcIp": "xx",
        "DstPort": 1,
        "HttpContent": "xx",
        "Id": 1,
        "HttpHost": "xx",
        "RequestId": "xx"
    }
}
```

