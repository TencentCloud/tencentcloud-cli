**Example 1: 删除DDoS防护的IP黑白名单**



Input: 

```
tccli antiddos DeleteBlackWhiteIpList --cli-unfold-argument  \
    --InstanceId bgpip-00001001 \
    --IpList 1.1.1.1 \
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

