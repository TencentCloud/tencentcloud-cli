**Example 1: 绑定高防弹性公网IP到实例上**



Input: 

```
tccli antiddos AssociateDDoSEipAddress --cli-unfold-argument  \
    --InstanceId bgpip-0000011x \
    --Eip 1.1.1.1 \
    --CvmInstanceID ins-11112222 \
    --CvmRegion ap-hongkong
```

Output: 
```
{
    "Response": {
        "RequestId": "5063ab0a-a8a7-41e8-ace2-263b2c1c8794"
    }
}
```

