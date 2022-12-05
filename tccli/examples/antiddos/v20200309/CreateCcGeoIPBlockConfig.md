**Example 1: 添加CC防护的区域封禁配置**



Input: 

```
tccli antiddos CreateCcGeoIPBlockConfig --cli-unfold-argument  \
    --InstanceId bgpip-0000011x \
    --IP 1.1.1.1 \
    --Domain www.test.com \
    --Protocol http \
    --CcGeoIPBlockConfig.Action drop \
    --CcGeoIPBlockConfig.Id 0 \
    --CcGeoIPBlockConfig.RegionType oversea \
    --CcGeoIPBlockConfig.AreaList 100025
```

Output: 
```
{
    "Response": {
        "RequestId": "54a41bf4-dca0-438b-a1cd-eb1f99e9a6b3"
    }
}
```

