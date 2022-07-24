**Example 1: 查询域名节点信息**



Input: 

```
tccli cdn DescribeIpStatus --cli-unfold-argument  \
    --Domain www.test.com
```

Output: 
```
{
    "Response": {
        "RequestId": "b6e9964d-26a3-49d0-adab-993e17d2f950",
        "TotalCount": 1,
        "Ips": [
            {
                "Ip": "1.1.1.1",
                "District": "广东",
                "Isp": "电信",
                "City": "深圳",
                "Status": "online",
                "Ipv6": null
            }
        ]
    }
}
```

