**Example 1: 创建终端节点**

输入终端节点名称，客户自己的终端节点服务ID，以及终端节点服务对应的地域来创建一个终端节点

Input: 

```
tccli privatedns CreateEndPoint --cli-unfold-argument  \
    --EndPointName 终端节点名 \
    --EndPointServiceId vpcsvc-gtd4gxa1 \
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

