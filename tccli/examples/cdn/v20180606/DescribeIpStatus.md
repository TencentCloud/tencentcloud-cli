**Example 1: Querying domain name node information**



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
        "Ips": [
            {
                "Ip": "1.1.1.1",
                "District": "Guangdong",
                "Isp": "China Telecom",
                "City": "Shenzhen",
                "Status": "online"
            }
        ]
    }
}
```

