**Example 1: 查询域名节点信息**



Input: 

```
tccli ecdn DescribeIpStatus --cli-unfold-argument  \
    --Domain www.test.com
```

Output: 
```
{
    "Response": {
        "RequestId": "b6e9964d-26a3-49d0-adab-993e17d2f950",
        "Ips": [
            {
                "Ip": "1.1.1.1",
                "District": "广东",
                "Isp": "电信",
                "City": "深圳",
                "Status": "online",
                "CreateTime": "2019-10-12 00:00:00"
            }
        ],
        "TotalCount": 0
    }
}
```

