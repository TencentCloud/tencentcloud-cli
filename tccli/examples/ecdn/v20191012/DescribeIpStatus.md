**Example 1: Querying node information of domain name**



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
                "District": "Guangdong",
                "Isp": "China Telecom",
                "City": "Shenzhen",
                "Status": "Online"
            }
        ],
        "TotalCount": 0
    }
}
```

