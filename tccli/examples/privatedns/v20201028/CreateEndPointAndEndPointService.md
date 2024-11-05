**Example 1: 同时创建终端节点和终端节点服务**

输入vpcid，终端节点服务名称， 实例id，服务类型 创建终端节点服务，同时用终端节点名称，以及终端节点服务对应的地域来创建一个终端节点

Input: 

```
tccli privatedns CreateEndPointAndEndPointService --cli-unfold-argument  \
    --VpcId vpc-xxxxxxxx \
    --EndPointServiceName test001 \
    --AutoAcceptFlag True \
    --ServiceInstanceId lb-xxxxxxxx \
    --ServiceType clb \
    --EndPointName test001 \
    --EndPointRegion ap-guangzhou
```

Output: 
```
{
    "Response": {
        "RequestId": "5cd964e2-b5e6-8a35-9ce5a1085860c845",
        "EndPointId": "eid-scls023kfns",
        "EndPointName": "终端节点名",
        "EndPointServiceId": "vpcsvc-gtd4gxa1",
        "EndPointVipSet": [
            "10.0.0.13"
        ]
    }
}
```

