**Example 1: 通过一个后端实例ID获取一个传统型负载均衡的信息**



Input: 

```
tccli clb DescribeClassicalLBByInstanceId --cli-unfold-argument  \
    --InstanceIds ins-odjhn6vc
```

Output: 
```
{
    "Response": {
        "LoadBalancerInfoList": [
            {
                "InstanceId": "ins-odjhn6vc",
                "LoadBalancerIds": [
                    "lb-2zkbmcy4",
                    "lb-a3u5l5zc"
                ]
            }
        ],
        "RequestId": "e6dd52d7-d80d-49f1-85ef-24a4a8221370"
    }
}
```

