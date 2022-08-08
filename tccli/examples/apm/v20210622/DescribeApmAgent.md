**Example 1: 获取Apm Agent信息**



Input: 

```
tccli apm DescribeApmAgent --cli-unfold-argument  \
    --InstanceId jYm6_leMg
```

Output: 
```
{
    "Response": {
        "ApmAgent": {
            "CollectorURL": "http://127.0.0.1:8080",
            "AgentDownloadURL": "https://agent.tapm.tencentyun.com/DownloadAgent",
            "Token": "14dac76ca10f4610f727ca68528758b43980251387493706d18988fa7d0621b7",
            "PublicCollectorURL": "http://127.0.0.1:8080",
            "InnerCollectorURL": "http://127.0.0.1:8080",
            "PrivateLinkCollectorURL": "http://127.0.0.1:8080"
        },
        "RequestId": "mzltx5whme-zl7je3p16tk5fwtb7ht61"
    }
}
```

