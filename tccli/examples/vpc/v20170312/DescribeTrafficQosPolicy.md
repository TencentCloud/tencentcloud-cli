**Example 1: 查询流量调度规则**



Input: 

```
tccli vpc DescribeTrafficQosPolicy --cli-unfold-argument  \
    --CcnId ccn-mo8mumi7 \
    --LocalRegion ap-guangzhou \
    --RemoteRegion ap-chengdu
```

Output: 
```
{
    "Response": {
        "TrafficQosPolicySet": [
            {
                "CcnId": "ccn-0puqax1n",
                "QosId": 1,
                "QosPolicyDescription": "1",
                "QosPolicyName": "1",
                "Bandwidth": 1
            }
        ],
        "RequestId": "e052b088-c3a4-4efa-96e6-8af897abb369"
    }
}
```

