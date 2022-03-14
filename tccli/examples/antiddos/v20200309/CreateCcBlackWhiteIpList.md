**Example 1: 新建CC四层黑白名单**



Input: 

```
tccli antiddos CreateCcBlackWhiteIpList --cli-unfold-argument  \
    --Domain xx \
    --Protocol xx \
    --InstanceId xx \
    --Ip xx \
    --IpList.0.Ip xx \
    --IpList.0.Mask 1 \
    --Type xx
```

Output: 
```
{
    "Response": {
        "RequestId": "b7739a1e-837d-4248-bf9f-16a9bf77db22"
    }
}
```

