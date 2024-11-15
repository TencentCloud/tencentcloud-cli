**Example 1: 查询引擎升级详情**

查询引擎升级详情

Input: 

```
tccli cfw DescribeEngineUpdateDetail --cli-unfold-argument  \
    --SelectedVersion 
```

Output: 
```
{
    "Response": {
        "EngineVersionLst": [
            {
                "Version": "cfw_v4.2.0.1099",
                "Detail": "{\"details\": [{\"items\": [\"【新增】新增模拟拨测功能\", \"【新增】新增支持透明模式\", \"【优化】优化防火墙满载状态判定\", \"【优化】优化地址模板的匹配效率\", \"【优化】优化IP地址不存在默认路由到防火墙的场景\"], \"subtitle\": \"版本更新说明:\"}, {\"items\": [\"升级过程可能需要若干分钟，期间无法操作防火墙开关和规则\", \"升级完成后，会自动复原开关和规则的状态\"], \"subtitle\": \"说明:\"}], \"summary\": \"引擎更新\"}",
                "State": "",
                "UpdateTime": "2024-01-05 18:54:24",
                "AbleUpdateCnt": 3,
                "AbleBackCnt": 0
            },
            {
                "Version": "cfw_v4.2.0.1098",
                "Detail": "{\"details\": [{\"items\": [\"【新增】新增模拟拨测功能\", \"【新增】新增支持透明模式\", \"【优化】优化防火墙满载状态判定\", \"【优化】优化地址模板的匹配效率\", \"【优化】优化IP地址不存在默认路由到防火墙的场景\"], \"subtitle\": \"版本更新说明:\"}, {\"items\": [\"升级过程可能需要若干分钟，期间无法操作防火墙开关和规则\", \"升级完成后，会自动复原开关和规则的状态\"], \"subtitle\": \"说明:\"}], \"summary\": \"引擎更新\"}",
                "State": "",
                "UpdateTime": "2024-01-05 09:51:23",
                "AbleUpdateCnt": 4,
                "AbleBackCnt": 0
            },
            {
                "Version": "cfw_v4.1.2.1091",
                "Detail": "{\"details\": [{\"items\": [\"【新增】新增模拟拨测功能\", \"【新增】新增支持透明模式\", \"【优化】优化防火墙满载状态判定\", \"【优化】优化地址模板的匹配效率\", \"【优化】优化IP地址不存在默认路由到防火墙的场景\"], \"subtitle\": \"版本更新说明:\"}, {\"items\": [\"升级过程可能需要若干分钟，期间无法操作防火墙开关和规则\", \"升级完成后，会自动复原开关和规则的状态\"], \"subtitle\": \"说明:\"}], \"summary\": \"引擎更新\"}",
                "State": "",
                "UpdateTime": "2024-01-05 18:01:06",
                "AbleUpdateCnt": 0,
                "AbleBackCnt": 3
            }
        ],
        "FwInsVersionLst": [
            {
                "Region": "",
                "CfwInsId": "cfwnat-f0f1c7c0",
                "CfwInsName": "[autotest][勿删]自动化测试",
                "FwType": "nat",
                "CurVersion": "cfw_v4.2.0.1097",
                "UpdateStatus": 0,
                "UpdateEnable": 1,
                "BackEnable": 0,
                "ReserveTime": "",
                "ReserveVersion": "",
                "ReserveVersionState": "",
                "ReserveId": 0
            },
            {
                "Region": "",
                "CfwInsId": "cfwnat-305fe046",
                "CfwInsName": "bj1",
                "FwType": "nat",
                "CurVersion": "cfw_v4.2.0.1097",
                "UpdateStatus": 0,
                "UpdateEnable": 1,
                "BackEnable": 0,
                "ReserveTime": "",
                "ReserveVersion": "",
                "ReserveVersionState": "",
                "ReserveId": 0
            },
            {
                "Region": "",
                "CfwInsId": "cfwew-091fafd3",
                "CfwInsName": "[autotest]【勿动】自动化测试-上海",
                "FwType": "ew",
                "CurVersion": "cfw_v4.master.0.1093",
                "UpdateStatus": 0,
                "UpdateEnable": 1,
                "BackEnable": 0,
                "ReserveTime": "",
                "ReserveVersion": "",
                "ReserveVersionState": "",
                "ReserveId": 0
            },
            {
                "Region": "",
                "CfwInsId": "cfwew-835e3d29",
                "CfwInsName": "云联网出公网-广州",
                "FwType": "ew",
                "CurVersion": "cfw_v4.1.2.1091",
                "UpdateStatus": 1,
                "UpdateEnable": 1,
                "BackEnable": 0,
                "ReserveTime": "",
                "ReserveVersion": "",
                "ReserveVersionState": "",
                "ReserveId": 0
            }
        ],
        "RequestId": "68e20852-10ef-4f7c-bef4-aadcf66447a3"
    }
}
```

