**Example 1: 删除CC防护的区域封禁配置**



Input: 

```
tccli antiddos DeleteCcGeoIPBlockConfig --cli-unfold-argument  \
    --InstanceId xx \
    --CcGeoIPBlockConfig.Action xx \
    --CcGeoIPBlockConfig.Id xx \
    --CcGeoIPBlockConfig.RegionType xx \
    --CcGeoIPBlockConfig.AreaList 0
```

Output: 
```
{
    "Response": {
        "RequestId": "xx"
    }
}
```

