**Example 1: 查询可用区信息（可用区中文名称）**

查询可用区信息（可用区中文名称）

Input: 

```
tccli region DescribeZones --cli-unfold-argument  \
    --Product cvm \
    --Scene 1
```

Output: 
```
{
    "Response": {
        "TotalCount": 7,
        "RequestId": "6c3323bd-c855-49d7-85fb-7d6e0d8e1c55",
        "ZoneSet": [
            {
                "Zone": "ap-beijing-2",
                "ZoneIdMC": null,
                "ZoneId": "800002",
                "ParentZoneName": "",
                "ParentZoneId": "",
                "ParentZone": "",
                "ZoneState": "AVAILABLE",
                "MachineRoomTypeMC": null,
                "ZoneType": "availability-zone",
                "ZoneName": "北京二区"
            },
            {
                "Zone": "ap-beijing-3",
                "ZoneIdMC": null,
                "ZoneId": "800003",
                "ParentZoneName": "",
                "ParentZoneId": "",
                "ParentZone": "",
                "ZoneState": "AVAILABLE",
                "MachineRoomTypeMC": null,
                "ZoneType": "availability-zone",
                "ZoneName": "北京三区"
            },
            {
                "Zone": "ap-beijing-4",
                "ZoneIdMC": null,
                "ZoneId": "800004",
                "ParentZoneName": "",
                "ParentZoneId": "",
                "ParentZone": "",
                "ZoneState": "AVAILABLE",
                "MachineRoomTypeMC": null,
                "ZoneType": "availability-zone",
                "ZoneName": "北京四区"
            },
            {
                "Zone": "ap-beijing-5",
                "ZoneIdMC": null,
                "ZoneId": "800005",
                "ParentZoneName": "",
                "ParentZoneId": "",
                "ParentZone": "",
                "ZoneState": "AVAILABLE",
                "MachineRoomTypeMC": null,
                "ZoneType": "availability-zone",
                "ZoneName": "北京五区"
            },
            {
                "Zone": "ap-beijing-6",
                "ZoneIdMC": null,
                "ZoneId": "800006",
                "ParentZoneName": "",
                "ParentZoneId": "",
                "ParentZone": "",
                "ZoneState": "AVAILABLE",
                "MachineRoomTypeMC": null,
                "ZoneType": "availability-zone",
                "ZoneName": "北京六区"
            },
            {
                "Zone": "ap-beijing-7",
                "ZoneIdMC": null,
                "ZoneId": "800007",
                "ParentZoneName": "",
                "ParentZoneId": "",
                "ParentZone": "",
                "ZoneState": "AVAILABLE",
                "MachineRoomTypeMC": null,
                "ZoneType": "availability-zone",
                "ZoneName": "北京七区"
            },
            {
                "Zone": "ap-beijing-tez-changchun-1",
                "ZoneIdMC": null,
                "ZoneId": "2100080001",
                "ParentZoneName": "北京三区",
                "ParentZoneId": "800003",
                "ParentZone": "ap-beijing-3",
                "ZoneState": "AVAILABLE",
                "MachineRoomTypeMC": null,
                "ZoneType": "edge-zone",
                "ZoneName": "长春边缘一区"
            }
        ]
    }
}
```

