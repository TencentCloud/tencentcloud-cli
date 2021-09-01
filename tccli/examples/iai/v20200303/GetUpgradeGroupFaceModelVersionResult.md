**Example 1: 人员库升级结果查询（升级成功）**

人员库升级成功（Status返回1）

Input: 

```
tccli iai GetUpgradeGroupFaceModelVersionResult --cli-unfold-argument  \
    --JobId 251007453_upgrade_group_qta_1596529493_gjwh07X7
```

Output: 
```
{
    "Response": {
        "Progress": 100,
        "EndTimestamp": 1596529510000,
        "Status": 1,
        "StartTime": 1596529493217,
        "FromFaceModelVersion": "2.0",
        "GroupId": "100001testGroupUpgrade",
        "FailedFacesUrl": "",
        "ToFaceModelVersion": "3.0",
        "RequestId": "b0835106-e301-4959-90d5-f982007bb4c8"
    }
}
```

**Example 2: 人员库升级结果查询（升级失败）**

人员库升级失败（Status返回3），FailedFacesUrl包含失败人脸信息，需对失败人脸信息删除后进行重新升级。如果FailedFacesUrl返回值是空，可能是系统失败，可以重新发起一次升级。
失败人脸信息示例：
[{
face_id: "3758206365629500199",
person_id: "testGroupUpgradePerson1100001"
}, {
face_id: "3758206372549784459",
person_id: "testGroupUpgradePerson2100001"
}]

Input: 

```
tccli iai GetUpgradeGroupFaceModelVersionResult --cli-unfold-argument  \
    --JobId 251007453_upgrade_group_qta_1596529493_gjwh07X7
```

Output: 
```
{
    "Response": {
        "Progress": 100,
        "EndTimestamp": 1607058209000,
        "Status": 3,
        "StartTime": 1607058207375,
        "FromFaceModelVersion": "3.0",
        "GroupId": "test_2_upgrade",
        "FailedFacesUrl": "https://iaiface-upgradegroup-failedface-1254418846.cos.ap-guangzhou.myqcloud.com/1253657503/1253657503_upgrade_group_1607058207_qW6RX1UO.json",
        "ToFaceModelVersion": "2.0",
        "RequestId": "b667bf57-b40f-4618-9ef4-eb2d350eb068"
    }
}
```

**Example 3: 人员库升级结果查询（升级中）**

人员库升级中（Status返回0）

Input: 

```
tccli iai GetUpgradeGroupFaceModelVersionResult --cli-unfold-argument  \
    --JobId 251007453_upgrade_group_qta_1596529493_gjwh07X7
```

Output: 
```
{
    "Response": {
        "Progress": 77,
        "EndTimestamp": 1607091150000,
        "Status": 0,
        "StartTime": 1607073566782,
        "FromFaceModelVersion": "2.0",
        "GroupId": "965e41210ab6eaf56dee78bad4743b23",
        "FailedFacesUrl": "",
        "ToFaceModelVersion": "3.0",
        "RequestId": "3c834d55-967a-4795-9beb-4c877418cd79"
    }
}
```

