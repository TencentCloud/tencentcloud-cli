**Example 1: 续费参数转换-成功返回**

续费参数转换

Input: 

```
tccli lighthouse SwitchParameterRenewInstances --cli-unfold-argument  \
    --InstanceChargePrepaid.RenewFlag NOTIFY_AND_AUTO_RENEW \
    --InstanceChargePrepaid.Period 1 \
    --InstanceIds lhins-11110001
```

Output: 
```
{
    "Response": {
        "InstanceOrder": "{\"ownerUin\": \"700000164995\", \"uin\": \"700000181909\", \"appId\": 251202221, \"projectId\": 0, \"goods\": [{\"goodsCategoryId\": 1024533, \"goodsNum\": 1, \"goodsDetail\": {\"productCode\": \"p_lighthouse\", \"subProductCode\": \"sp_lighthouse_bundle_excl01_linux_01\", \"pid\": 1012247, \"sv_lighthouse_compute_e_linux_med2_50_100\": 1, \"sv_lighthouse_rootdisk_e_ssd_linux_med2_50_100\": 1, \"sv_lighthouse_trafficpkg_e_linux_med2_50_100\": 1, \"productInfo\": [{\"name\": \"\\u8fd0\\u7b97\\u7ec4\\u4ef6\", \"value\": \"2\\u6838CPU\\u30012GB\\u5185\\u5b58 (\\u4e13\\u5c5e\\u578bLinux-2\\u68382G-50G-100G)\"}, {\"name\": \"\\u4e91SSD\\u7cfb\\u7edf\\u76d8\", \"value\": \"50GB SSD\\u4e91\\u786c\\u76d8 (\\u4e13\\u5c5e\\u578bLinux-2\\u68382G-50G-100G)\"}, {\"name\": \"\\u6d41\\u91cf\\u5305\", \"value\": \"100GB/\\u6708\\u6d41\\u91cf\\u5305 (\\u4e13\\u5c5e\\u578bLinux-2\\u68382G-50G-100G)\"}, {\"name\": \"\\u5730\\u57df\", \"value\": \"\\u4e2d\\u56fd\\u9999\\u6e2f\"}], \"resourceId\": \"lhins-atqh8y7p\", \"autoRenewFlag\": 0, \"timeUnit\": \"m\", \"timeSpan\": 1, \"curDeadline\": \"2023-01-11 10:23:20\", \"signature\": \"620d9e29793449cd0b591f111964b1d4\"}, \"regionId\": 5, \"payMode\": 1}, {\"goodsCategoryId\": 102850, \"goodsNum\": 1, \"payMode\": 1, \"regionId\": 5, \"goodsDetail\": {\"pid\": 1010456, \"productCode\": \"p_lighthouse\", \"subProductCode\": \"sp_lighthouse_disk\", \"productInfo\": [{\"name\": \"\\u4e91\\u786c\\u76d8\\u7c7b\\u578b\", \"value\": \"\\u6570\\u636e\\u76d8\"}, {\"name\": \"\\u4e91\\u786c\\u76d8\\u4ecb\\u8d28\\u7c7b\\u578b\", \"value\": \"\\u9ad8\\u6027\\u80fd\\u4e91\\u786c\\u76d8\"}, {\"name\": \"\\u4e91\\u786c\\u76d8\\u5927\\u5c0f\", \"value\": \"20\"}, {\"name\": \"\\u5730\\u57df\", \"value\": \"\\u4e2d\\u56fd\\u9999\\u6e2f\"}], \"sv_lighthouse_disk_premium_01\": 20, \"resourceId\": \"lhdisk-ffyrsb6q\", \"autoRenewFlag\": 0, \"timeUnit\": \"m\", \"timeSpan\": 1, \"curDeadline\": \"2023-02-11 10:58:58\", \"signature\": \"82fa227ce7977c4cfcb0ca9ad175b9b7\"}}], \"zoneId\": 0}",
        "RequestId": "abf344d9-7d32-4b2c-9912-c154f233ec74"
    }
}
```

