**Example 1: 修改CC四层黑白名单**



Input: 

```
tccli antiddos ModifyCcBlackWhiteIpList --cli-unfold-argument  \
    --InstanceId xx \
    --IpList.0.Ip xx \
    --IpList.0.Mask 1 \
    --Type xx \
    --PolicyId xx
```

Output: 
```
{
    "Response": {
        "RequestId": "5063ab0a-a8a7-41e8-ace2-263b2c1c8794"
    }
}
```

