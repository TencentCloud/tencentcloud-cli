**Example 1: 查询指定流量包**

查询指定ResourceId的流量包

Input: 

```
tccli mna GetFlowPackages --cli-unfold-argument  \
    --PageNumber 1 \
    --PageSize 10 \
    --ResourceId mpe-00ja9uc_2Z26M6JHHc0
```

Output: 
```
{
    "Response": {
        "PackageList": [
            {
                "ActiveTime": 1786523124,
                "AppId": 260126599,
                "CapacityRemain": 20000,
                "CapacityRemainPrecise": 20000,
                "CapacitySize": 20000,
                "CreateTime": 1786523120,
                "DeviceList": [
                    "mna-qz2oc2mbco"
                ],
                "ExpireTime": 1789201523,
                "ModifyStatus": 0,
                "PackageType": "DEVICE_1_FLOW_20G",
                "RenewFlag": true,
                "ResourceId": "mpe-00ja9uc_2Z26M6JHHc0",
                "Status": 1,
                "TruncFlag": false
            }
        ],
        "Total": 1,
        "RequestId": "b4e42802-7a24-4388-acb6-ec6ecb04d626"
    }
}
```

**Example 2: 查询指定生效时间之后的流量包**

查询指定生效时间之后的流量包

Input: 

```
tccli mna GetFlowPackages --cli-unfold-argument  \
    --PageNumber 1 \
    --PageSize 10 \
    --ActiveTimeStart 2026-08-12 16:25:23 \
    --ActiveTimeEnd 2026-08-13 16:25:23
```

Output: 
```
{
    "Response": {
        "PackageList": [
            {
                "ActiveTime": 1786523124,
                "AppId": 260126599,
                "CapacityRemain": 20000,
                "CapacityRemainPrecise": 20000,
                "CapacitySize": 20000,
                "CreateTime": 1786523120,
                "DeviceList": [
                    "mna-qz2oc2mbco"
                ],
                "ExpireTime": 1789201523,
                "ModifyStatus": 0,
                "PackageType": "DEVICE_1_FLOW_20G",
                "RenewFlag": true,
                "ResourceId": "mpe-00ja9uc_2Z26M6JHHc0",
                "Status": 1,
                "TruncFlag": false
            }
        ],
        "Total": 1,
        "RequestId": "9f591e4b-546a-4a8b-acb5-292c9651f62d"
    }
}
```

**Example 3: 查询生效中的流量包**

查询生效中的流量包

Input: 

```
tccli mna GetFlowPackages --cli-unfold-argument  \
    --PageNumber 1 \
    --PageSize 10 \
    --Status 1
```

Output: 
```
{
    "Response": {
        "PackageList": [
            {
                "ActiveTime": 1786523124,
                "AppId": 260126599,
                "CapacityRemain": 20000,
                "CapacityRemainPrecise": 20000,
                "CapacitySize": 20000,
                "CreateTime": 1786523120,
                "DeviceList": [
                    "mna-qz2oc2mbco"
                ],
                "ExpireTime": 1789201523,
                "ModifyStatus": 0,
                "PackageType": "DEVICE_1_FLOW_20G",
                "RenewFlag": true,
                "ResourceId": "mpe-00ja9uc_2Z26M6JHHc0",
                "Status": 1,
                "TruncFlag": false
            }
        ],
        "Total": 1,
        "RequestId": "56199b6d-980d-40b5-a0d5-c90d68ef8358"
    }
}
```

