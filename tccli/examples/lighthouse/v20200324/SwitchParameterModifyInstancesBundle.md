**Example 1: 修改实例套餐下单参数转换**

修改实例套餐下单参数转换

Input: 

```
tccli lighthouse SwitchParameterModifyInstancesBundle --cli-unfold-argument  \
    --InstanceIds lhins-8ogy0ktp \
    --BundleId bundle_ntp_medium8_2000
```

Output: 
```
{
    "Response": {
        "InstanceOrder": "{\"ownerUin\": \"123\", \"uin\": \"123\", \"appId\": 123, \"projectId\": 0, \"zoneId\": 0, \"goods\": [{\"goodsCategoryId\": 102035, \"action\": \"modify\", \"payMode\": 1, \"regionId\": 1, \"goodsNum\": 1, \"goodsDetail\": {\"resourceId\": \"lhins-8ogy0ktp\", \"oldConfig\": {\"timeUnit\": \"m\", \"productCode\": \"p_lighthouse\", \"subProductCode\": \"sp_lighthouse_bundle_ntp_medium8_2000\", \"pid\": 1002610, \"sv_lighthouse_compute_med8_2000\": 1, \"sv_lighthouse_rootdisk_cbsssd_med8_2000\": 1, \"sv_lighthouse_trafficpkg_med8_2000\": 1}, \"newConfig\": {\"timeUnit\": \"m\", \"productCode\": \"p_lighthouse\", \"subProductCode\": \"sp_lighthouse_bundle_ntp_medium8_2000\", \"pid\": 1002610, \"sv_lighthouse_compute_med8_2000\": 1, \"sv_lighthouse_rootdisk_cbsssd_med8_2000\": 1, \"sv_lighthouse_trafficpkg_med8_2000\": 1}, \"curDeadline\": \"2020-12-23 20:10:24\", \"productInfo\": [{\"name\": \"\\u8fd0\\u7b97\\u7ec4\\u4ef6\", \"value\": \"\\u8fd0\\u7b97\\u7ec4\\u4ef6 (MEDIUM8 | 2000GB)\"}, {\"name\": \"\\u4e91SSD\\u7cfb\\u7edf\\u76d8\", \"value\": \"\\u4e91SSD\\u7cfb\\u7edf\\u76d8 (MEDIUM8 | 2000GB)\"}, {\"name\": \"\\u6d41\\u91cf\\u5305\", \"value\": \"\\u6d41\\u91cf\\u5305 (MEDIUM8 | 2000GB)\"}]}}]}",
        "RequestId": "3e9526fa-b04c-4af8-a360-1e322d78107f"
    }
}
```

