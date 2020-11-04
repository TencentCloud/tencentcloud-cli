**Example 1: 维修任务配置获取**



Input: 

```
tccli bm DescribeRepairTaskConstant --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "3b14a9b3-82c5-45fa-906d-0aa07fc07fd7",
        "TaskTypeSet": [
            {
                "TypeId": 30,
                "TypeName": "硬盘故障（有冗余）",
                "TaskSubType": "redundancy"
            },
            {
                "TypeId": 31,
                "TypeName": "RAID卡电池故障",
                "TaskSubType": "nonredundancy"
            },
            {
                "TypeId": 32,
                "TypeName": "RAID卡缓存故障",
                "TaskSubType": "nonredundancy"
            },
            {
                "TypeId": 34,
                "TypeName": "硬盘故障（无冗余）",
                "TaskSubType": "nonredundancy"
            },
            {
                "TypeId": 36,
                "TypeName": "逻辑盘只读",
                "TaskSubType": "nonredundancy"
            },
            {
                "TypeId": 37,
                "TypeName": "硬盘即将故障（有冗余）",
                "TaskSubType": "redundancy"
            },
            {
                "TypeId": 38,
                "TypeName": "操作系统硬盘故障（无冗余）",
                "TaskSubType": "nonredundancy"
            },
            {
                "TypeId": 40,
                "TypeName": "硬盘故障（有冗余，槽位未知）",
                "TaskSubType": "redundancy"
            },
            {
                "TypeId": 41,
                "TypeName": "电源故障（有冗余）",
                "TaskSubType": "redundancy"
            },
            {
                "TypeId": 42,
                "TypeName": "风扇故障",
                "TaskSubType": "nonredundancy"
            },
            {
                "TypeId": 43,
                "TypeName": "硬盘故障（无冗余，在线换盘）",
                "TaskSubType": "nonredundancy"
            },
            {
                "TypeId": 44,
                "TypeName": "Ping不可达",
                "TaskSubType": "unconfirmed"
            },
            {
                "TypeId": 47,
                "TypeName": "SSD硬盘故障（无冗余）",
                "TaskSubType": "nonredundancy"
            },
            {
                "TypeId": 48,
                "TypeName": "网卡故障",
                "TaskSubType": "nonredundancy"
            },
            {
                "TypeId": 49,
                "TypeName": "内存故障",
                "TaskSubType": "nonredundancy"
            },
            {
                "TypeId": 53,
                "TypeName": "主板故障",
                "TaskSubType": "nonredundancy"
            },
            {
                "TypeId": 55,
                "TypeName": "CPU故障",
                "TaskSubType": "nonredundancy"
            },
            {
                "TypeId": 60,
                "TypeName": "SSD硬盘寿命耗尽",
                "TaskSubType": "nonredundancy"
            },
            {
                "TypeId": 61,
                "TypeName": "SSD硬盘温度过高（关机换盘）",
                "TaskSubType": "nonredundancy"
            },
            {
                "TypeId": 62,
                "TypeName": "SSD硬盘坏块率过高（关机换盘）",
                "TaskSubType": "nonredundancy"
            },
            {
                "TypeId": 63,
                "TypeName": "电源故障（无冗余）",
                "TaskSubType": "nonredundancy"
            },
            {
                "TypeId": 94,
                "TypeName": "GPU故障",
                "TaskSubType": "nonredundancy"
            },
            {
                "TypeId": 124,
                "TypeName": "硬盘掉线",
                "TaskSubType": "nonredundancy"
            },
            {
                "TypeId": 58,
                "TypeName": "自助重启失败",
                "TaskSubType": "unconfirmed"
            }
        ]
    }
}
```

