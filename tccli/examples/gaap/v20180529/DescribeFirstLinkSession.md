**Example 1: 查询接入段加速会话信息**



Input: 

```
tccli gaap DescribeFirstLinkSession --cli-unfold-argument  \
    --SessionId MTYzMjczNDYyNDU0MWE5OWY3MWMzYTQ3OGZhMjJkY2NlNDU0NDE2YzE3-3-65537
```

Output: 
```
{
    "Response": {
        "Status": 1,
        "DestIpv4": [
            "143.244.174.31"
        ],
        "Duration": 1771,
        "SuiteType": "T100K",
        "RequestId": "q708a7c6-db58-4729-8e09-2ea6b727109p",
        "SrcPublicIpv4": "211.97.129.234"
    }
}
```

