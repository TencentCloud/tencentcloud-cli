**Example 1: 删除CC防护的区域封禁配置**



Input: 

```
tccli antiddos DeleteCcGeoIPBlockConfig --cli-unfold-argument  \
    --InstanceId bgpip-000000q0 \
    --CcGeoIPBlockConfig.Action drop \
    --CcGeoIPBlockConfig.Id ccGeoip-000000mm \
    --CcGeoIPBlockConfig.RegionType china \
    --CcGeoIPBlockConfig.AreaList 0
```

Output: 
```
{
    "Response": {
        "RequestId": "efc47bf5-b16a-410d-a993-0d4584446b6w"
    }
}
```

