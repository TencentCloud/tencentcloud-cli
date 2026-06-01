**Example 1: 查看七层转发策略**



Input: 

```
tccli ga2 DescribeForwardingPolicy --cli-unfold-argument  \
    --GlobalAcceleratorId ga-80bzejka \
    --ListenerId lsr-nd3qmz7h
```

Output: 
```
{
    "Response": {
        "ForwardingPolicySet": [
            {
                "ForwardingPolicyId": "dm-io46vpu6",
                "GlobalAcceleratorId": "ga-80bzejka",
                "Host": "www.aaac.com",
                "ListenerId": "lsr-nd3qmz7h",
                "DefaultHostFlag": true
            }
        ],
        "RequestId": "17b35c9f-79c9-4581-859a-5160c7884ef9",
        "TotalCount": 1
    }
}
```

