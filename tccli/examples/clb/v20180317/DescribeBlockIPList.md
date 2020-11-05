**Example 1: Querying the list of blocked IPs (blacklist) of a CLB instance**



Input: 

```
tccli clb DescribeBlockIPList --cli-unfold-argument  \
    --LoadBalancerId lb-6efswuxa
```

Output: 
```
{
    "Response": {
        "BlockedIPCount": 1,
        "BlockedIPList": [
            {
                "IP": "192.1.2.3",
                "CreateTime": "2019-01-10 10:55:40",
                "ExpireTime": "2019-01-10 11:12:19"
            }
        ],
        "ClientIPField": "test",
        "RequestId": "83329908-a282-4f9f-82ab-033a3025baff"
    }
}
```

