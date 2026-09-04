**Example 1: 列出同地域 CLB**

分页查询同地域负载均衡列表

Input: 

```
tccli dlc ListRegionLbs --cli-unfold-argument  \
    --ClusterId cls-xxxxxxxx \
    --Offset 0 \
    --Limit 20
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "Lbs": [
            {
                "LoadBalancerId": "lb-xxxxxxxx",
                "LoadBalancerName": "my-lb",
                "LoadBalancerType": "OPEN"
            }
        ],
        "RequestId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
    }
}
```

