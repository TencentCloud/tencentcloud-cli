**Example 1: 根据订单号获取资源信息**



Input: 

```
tccli tdcpg DescribeResourcesByDealName --cli-unfold-argument  \
    --DealName xx
```

Output: 
```
{
    "Response": {
        "ResourceIdInfoSet": [
            {
                "ClusterId": "tdcpg-xxx",
                "InstanceIdSet": [
                    "tdcpg-ins-xxx",
                    "tdcpg-ins-xxxx"
                ]
            }
        ],
        "RequestId": "005b862f-f408-4a95-a7e7-26f3e672e081"
    }
}
```

