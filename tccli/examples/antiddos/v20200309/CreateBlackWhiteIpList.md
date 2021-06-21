**Example 1: 添加DDoS防护的IP黑白名单**



Input: 

```
tccli antiddos CreateBlackWhiteIpList --cli-unfold-argument  \
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

