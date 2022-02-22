**Example 1: 添加CC防护的区域封禁配置**



Input: 

```
tccli antiddos CreateCcGeoIPBlockConfig --cli-unfold-argument  \
    --InstanceId xx \
    --IP xx \
    --Domain xx \
    --Protocol xx \
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

