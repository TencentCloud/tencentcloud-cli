**Example 1: 删除DDoS防护的IP黑白名单**



Input: 

```
tccli antiddos DeleteDDoSBlackWhiteIpList --cli-unfold-argument  \
    --InstanceId bgpip-00001001 \
    --IpList.0.Ip 1.1.1.1 \
    --IpList.0.Mask 0 \
    --Type black
```

Output: 
```
{
    "Response": {
        "RequestId": "b7739a1e-837d-4248-bf9f-16a9bf77db22"
    }
}
```

