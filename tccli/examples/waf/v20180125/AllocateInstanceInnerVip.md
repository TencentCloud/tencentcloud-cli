**Example 1: 为SAASWAF实例分配内网VIP**



Input: 

```
tccli waf AllocateInstanceInnerVip --cli-unfold-argument  \
    --InstanceId waf_2l12yabe01d91pi9
```

Output: 
```
{
    "Response": {
        "VipInfo": [
            {
                "LoadBalancerId": "lb-duk6vy4i",
                "LbUin": "2252646423",
                "LbAppid": "1251316161",
                "Vip": "30.162.45.38",
                "VipType": "ipv4",
                "Region": "ap-guangzhou",
                "Isp": "INNER"
            }
        ],
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03"
    }
}
```

