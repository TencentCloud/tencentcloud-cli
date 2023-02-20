**Example 1: 获取产品事件列表**

获取产品事件列表

Input: 

```
tccli monitor DescribeProductEventList --cli-unfold-argument  \
    --Module monitor \
    --TimeOrder DESC \
    --Limit 20 \
    --StartTime 1572624000 \
    --Offset 0 \
    --EndTime 1573228799
```

Output: 
```
{
    "Response": {
        "Events": [
            {
                "AdditionMsg": [],
                "Dimensions": [
                    {
                        "Key": "deviceLanIp",
                        "Name": "内网IP",
                        "Value": "172.0.0.1"
                    },
                    {
                        "Key": "deviceWanIp",
                        "Name": "外网IP",
                        "Value": null
                    },
                    {
                        "Key": "uniqVpcId",
                        "Name": "私有网络ID",
                        "Value": null
                    }
                ],
                "EventCName": "机器重启",
                "EventEName": "GuestReboot",
                "EventId": 43,
                "EventName": "guest_reboot",
                "InstanceId": "ins-19708ino",
                "InstanceName": "qta_test",
                "ProductCName": "云服务器",
                "ProductEName": "Cloud Virtual Machine",
                "ProductName": "cvm",
                "ProjectId": 0,
                "Region": "gz",
                "StartTime": 1573110201,
                "Status": "-",
                "SupportAlarm": 1,
                "Type": "abnormal",
                "UpdateTime": 1573081401
            },
            {
                "AdditionMsg": [],
                "Dimensions": [
                    {
                        "Key": "deviceLanIp",
                        "Name": "内网IP",
                        "Value": "172.0.0.1"
                    },
                    {
                        "Key": "deviceWanIp",
                        "Name": "外网IP",
                        "Value": null
                    },
                    {
                        "Key": "uniqVpcId",
                        "Name": "私有网络ID",
                        "Value": null
                    }
                ],
                "EventCName": "机器重启",
                "EventEName": "GuestReboot",
                "EventId": 43,
                "EventName": "guest_reboot",
                "InstanceId": "ins-19708ino",
                "InstanceName": "qta_test",
                "ProductCName": "云服务器",
                "ProductEName": "Cloud Virtual Machine",
                "ProductName": "cvm",
                "ProjectId": 0,
                "Region": "gz",
                "StartTime": 1573023802,
                "Status": "-",
                "SupportAlarm": 1,
                "Type": "abnormal",
                "UpdateTime": 1572995002
            },
            {
                "AdditionMsg": [],
                "Dimensions": [
                    {
                        "Key": "deviceLanIp",
                        "Name": "内网IP",
                        "Value": "172.0.0.1"
                    },
                    {
                        "Key": "deviceWanIp",
                        "Name": "外网IP",
                        "Value": null
                    },
                    {
                        "Key": "uniqVpcId",
                        "Name": "私有网络ID",
                        "Value": null
                    }
                ],
                "EventCName": "机器重启",
                "EventEName": "GuestReboot",
                "EventId": 43,
                "EventName": "guest_reboot",
                "InstanceId": "ins-19708ino",
                "InstanceName": "qta_test",
                "ProductCName": "云服务器",
                "ProductEName": "Cloud Virtual Machine",
                "ProductName": "cvm",
                "ProjectId": 0,
                "Region": "gz",
                "StartTime": 1572937414,
                "Status": "-",
                "SupportAlarm": 1,
                "Type": "abnormal",
                "UpdateTime": 1572908614
            },
            {
                "AdditionMsg": [],
                "Dimensions": [
                    {
                        "Key": "deviceLanIp",
                        "Name": "内网IP",
                        "Value": "172.0.0.1"
                    },
                    {
                        "Key": "deviceWanIp",
                        "Name": "外网IP",
                        "Value": null
                    },
                    {
                        "Key": "uniqVpcId",
                        "Name": "私有网络ID",
                        "Value": null
                    }
                ],
                "EventCName": "机器重启",
                "EventEName": "GuestReboot",
                "EventId": 43,
                "EventName": "guest_reboot",
                "InstanceId": "ins-19708ino",
                "InstanceName": "qta_test",
                "ProductCName": "云服务器",
                "ProductEName": "Cloud Virtual Machine",
                "ProductName": "cvm",
                "ProjectId": 0,
                "Region": "gz",
                "StartTime": 1572851042,
                "Status": "-",
                "SupportAlarm": 1,
                "Type": "abnormal",
                "UpdateTime": 1572822242
            },
            {
                "AdditionMsg": [],
                "Dimensions": [
                    {
                        "Key": "deviceLanIp",
                        "Name": "内网IP",
                        "Value": "172.0.0.1"
                    },
                    {
                        "Key": "deviceWanIp",
                        "Name": "外网IP",
                        "Value": null
                    },
                    {
                        "Key": "uniqVpcId",
                        "Name": "私有网络ID",
                        "Value": null
                    }
                ],
                "EventCName": "机器重启",
                "EventEName": "GuestReboot",
                "EventId": 43,
                "EventName": "guest_reboot",
                "InstanceId": "ins-19708ino",
                "InstanceName": "qta_test",
                "ProductCName": "云服务器",
                "ProductEName": "Cloud Virtual Machine",
                "ProductName": "cvm",
                "ProjectId": 0,
                "Region": "gz",
                "StartTime": 1572764569,
                "Status": "-",
                "SupportAlarm": 1,
                "Type": "abnormal",
                "UpdateTime": 1572735769
            },
            {
                "AdditionMsg": [],
                "Dimensions": [
                    {
                        "Key": "deviceLanIp",
                        "Name": "内网IP",
                        "Value": "172.0.0.1"
                    },
                    {
                        "Key": "deviceWanIp",
                        "Name": "外网IP",
                        "Value": null
                    },
                    {
                        "Key": "uniqVpcId",
                        "Name": "私有网络ID",
                        "Value": null
                    }
                ],
                "EventCName": "机器重启",
                "EventEName": "GuestReboot",
                "EventId": 43,
                "EventName": "guest_reboot",
                "InstanceId": "ins-19708ino",
                "InstanceName": "qta_test",
                "ProductCName": "云服务器",
                "ProductEName": "Cloud Virtual Machine",
                "ProductName": "cvm",
                "ProjectId": 0,
                "Region": "gz",
                "StartTime": 1572678255,
                "Status": "-",
                "SupportAlarm": 1,
                "Type": "abnormal",
                "UpdateTime": 1572649455
            }
        ],
        "OverView": {
            "StatusChangeAmount": 0,
            "UnConfigAlarmAmount": 6,
            "UnNormalEventAmount": 6,
            "UnRecoverAmount": 0
        },
        "RequestId": "313bac2f-04eb-477e-af2b-b4d58cbe5d08",
        "Total": 6
    }
}
```

