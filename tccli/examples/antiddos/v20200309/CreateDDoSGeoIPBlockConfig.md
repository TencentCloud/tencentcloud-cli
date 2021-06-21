**Example 1: 添加DDoS防护的区域封禁配置**



Input: 

```
tccli antiddos CreateDDoSGeoIPBlockConfig --cli-unfold-argument  \
    --InstanceId bgpip-0000011x \
    --DDoSGeoIPBlockConfig.RegionType customized \
    --DDoSGeoIPBlockConfig.AreaList 100001 100002 \
    --DDoSGeoIPBlockConfig.Action drop
```

Output: 
```
{
    "Response": {
        "RequestId": "5063ab0a-a8a7-41e8-ace2-263b2c1c8794"
    }
}
```

