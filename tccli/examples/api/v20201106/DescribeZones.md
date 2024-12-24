**Example 1: 查询可用区信息（可用区中文名称）**



Input: 

```
tccli api DescribeZones --cli-unfold-argument  \
    --Product cvm
```

Output: 
```
{
    "Response": {
        "RequestId": "7285e882-98f7-4b03-8ae0-a186d186e78e",
        "TotalCount": 4,
        "ZoneSet": [
            {
                "MachineRoomTypeMC": null,
                "ParentZone": "",
                "ParentZoneId": "",
                "ParentZoneName": "",
                "Zone": "ap-beijing-3",
                "ZoneId": "800003",
                "ZoneIdMC": null,
                "ZoneName": "北京三区",
                "ZoneState": "AVAILABLE",
                "ZoneType": "availability-zone"
            },
            {
                "MachineRoomTypeMC": null,
                "ParentZone": "",
                "ParentZoneId": "",
                "ParentZoneName": "",
                "Zone": "ap-beijing-6",
                "ZoneId": "800006",
                "ZoneIdMC": null,
                "ZoneName": "北京六区",
                "ZoneState": "AVAILABLE",
                "ZoneType": "availability-zone"
            },
            {
                "MachineRoomTypeMC": null,
                "ParentZone": "",
                "ParentZoneId": "",
                "ParentZoneName": "",
                "Zone": "ap-beijing-7",
                "ZoneId": "800007",
                "ZoneIdMC": null,
                "ZoneName": "北京七区",
                "ZoneState": "AVAILABLE",
                "ZoneType": "availability-zone"
            },
            {
                "MachineRoomTypeMC": null,
                "ParentZone": "",
                "ParentZoneId": "",
                "ParentZoneName": "",
                "Zone": "ap-beijing-8",
                "ZoneId": "800008",
                "ZoneIdMC": null,
                "ZoneName": "北京八区",
                "ZoneState": "AVAILABLE",
                "ZoneType": "availability-zone"
            }
        ]
    }
}
```

