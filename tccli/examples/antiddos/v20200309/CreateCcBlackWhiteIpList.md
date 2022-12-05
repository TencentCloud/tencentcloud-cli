**Example 1: 新建CC四层黑白名单**



Input: 

```
tccli antiddos CreateCcBlackWhiteIpList --cli-unfold-argument  \
    --Domain www.test.com \
    --Protocol http \
    --InstanceId bgpip-00001001 \
    --Ip 1.1.1.1 \
    --IpList.0.Ip 1.1.1.0 \
    --IpList.0.Mask 24 \
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

