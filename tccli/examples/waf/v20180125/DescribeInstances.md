**Example 1: 查询用户所有实例的详细信息**

查询用户所有实例的详细信息

Input: 

```
tccli waf DescribeInstances --cli-unfold-argument  \
    --Offset 1 \
    --Limit 20 \
    --Filters.0.Name Edition \
    --Filters.0.ExactMatch True \
    --Filters.1.Name Region \
    --Filters.1.Values ap-beijing ap-guangzhou \
    --Filters.1.ExactMatch True \
    --Filters.2.Name InstanceName \
    --Filters.2.Values 实例 \
    --Filters.2.ExactMatch False \
    --Filters.3.Name InstanceId \
    --Filters.3.Values waf \
    --Filters.3.ExactMatch False
```

Output: 
```
{
    "Response": {
        "RequestId": "b7984267-1b60-4979-accb-8f1ca497f827",
        "Total": 11,
        "Instances": [
            {
                "AppId": 251197211,
                "InstanceId": "waf_2kuj4t1k00awo4gp",
                "InstanceName": "gz-Default",
                "ResourceIds": "waf_2kuj4t1k00awo4gp",
                "Edition": "sparta-waf",
                "Region": "gz",
                "PayMode": 1,
                "RenewFlag": 1,
                "Level": 4,
                "ValidTime": "2021-11-09 10:37:20",
                "BeginTime": "0001-01-01 00:00:00",
                "SubDomainLimit": 40,
                "MainDomainLimit": 4,
                "Mode": 0,
                "DomainCount": 6,
                "MainDomainCount": 2,
                "MaxQPS": 0,
                "QPS": {
                    "ResourceIds": "",
                    "ValidTime": "",
                    "RenewFlag": 0,
                    "Count": 0,
                    "Region": ""
                },
                "DomainPkg": {
                    "ResourceIds": "",
                    "ValidTime": "",
                    "RenewFlag": 0,
                    "Count": 0,
                    "Region": ""
                },
                "BotPkg": {
                    "ResourceIds": "",
                    "Status": 0,
                    "Region": 0,
                    "BeginTime": "",
                    "EndTime": "",
                    "InquireNum": 0,
                    "UsedNum": 0
                },
                "FraudPkg": {
                    "ResourceIds": "",
                    "Status": "",
                    "Region": 0,
                    "BeginTime": "",
                    "EndTime": "",
                    "InquireNum": 0,
                    "UsedNum": 0
                }
            },
            {
                "AppId": 251197211,
                "InstanceId": "waf_2kui15ko00a19t0r",
                "InstanceName": "cd-Default",
                "ResourceIds": "waf_2kui15ko00a19t0r",
                "Edition": "sparta-waf",
                "Region": "cd",
                "PayMode": 1,
                "RenewFlag": 1,
                "Level": 4,
                "ValidTime": "2021-09-24 15:34:09",
                "BeginTime": "0001-01-01 00:00:00",
                "SubDomainLimit": 40,
                "MainDomainLimit": 4,
                "Mode": 0,
                "DomainCount": 7,
                "MainDomainCount": 1,
                "MaxQPS": 0,
                "QPS": {
                    "ResourceIds": "",
                    "ValidTime": "",
                    "RenewFlag": 0,
                    "Count": 0,
                    "Region": ""
                },
                "DomainPkg": {
                    "ResourceIds": "",
                    "ValidTime": "",
                    "RenewFlag": 0,
                    "Count": 0,
                    "Region": ""
                },
                "BotPkg": {
                    "ResourceIds": "",
                    "Status": 0,
                    "Region": 0,
                    "BeginTime": "",
                    "EndTime": "",
                    "InquireNum": 0,
                    "UsedNum": 0
                },
                "FraudPkg": {
                    "ResourceIds": "",
                    "Status": "",
                    "Region": 0,
                    "BeginTime": "",
                    "EndTime": "",
                    "InquireNum": 0,
                    "UsedNum": 0
                }
            },
            {
                "AppId": 251197211,
                "InstanceId": "waf_2kui15ko00a19pwt",
                "InstanceName": "gz-Default",
                "ResourceIds": "waf_2kui15ko00a19pwt",
                "Edition": "sparta-waf",
                "Region": "gz",
                "PayMode": 1,
                "RenewFlag": 1,
                "Level": 4,
                "ValidTime": "2021-09-24 15:30:15",
                "BeginTime": "0001-01-01 00:00:00",
                "SubDomainLimit": 40,
                "MainDomainLimit": 4,
                "Mode": 0,
                "DomainCount": 1,
                "MainDomainCount": 1,
                "MaxQPS": 0,
                "QPS": {
                    "ResourceIds": "",
                    "ValidTime": "",
                    "RenewFlag": 0,
                    "Count": 0,
                    "Region": ""
                },
                "DomainPkg": {
                    "ResourceIds": "",
                    "ValidTime": "",
                    "RenewFlag": 0,
                    "Count": 0,
                    "Region": ""
                },
                "BotPkg": {
                    "ResourceIds": "",
                    "Status": 0,
                    "Region": 0,
                    "BeginTime": "",
                    "EndTime": "",
                    "InquireNum": 0,
                    "UsedNum": 0
                },
                "FraudPkg": {
                    "ResourceIds": "",
                    "Status": "",
                    "Region": 0,
                    "BeginTime": "",
                    "EndTime": "",
                    "InquireNum": 0,
                    "UsedNum": 0
                }
            },
            {
                "AppId": 251197211,
                "InstanceId": "waf_2kui15ko00a19p7j",
                "InstanceName": "测试删除域名",
                "ResourceIds": "waf_2kui15ko00a19p7j",
                "Edition": "sparta-waf",
                "Region": "cd",
                "PayMode": 1,
                "RenewFlag": 1,
                "Level": 4,
                "ValidTime": "2022-09-24 15:28:34",
                "BeginTime": "0001-01-01 00:00:00",
                "SubDomainLimit": 40,
                "MainDomainLimit": 4,
                "Mode": 0,
                "DomainCount": 2,
                "MainDomainCount": 2,
                "MaxQPS": 0,
                "QPS": {
                    "ResourceIds": "",
                    "ValidTime": "",
                    "RenewFlag": 0,
                    "Count": 0,
                    "Region": ""
                },
                "DomainPkg": {
                    "ResourceIds": "",
                    "ValidTime": "",
                    "RenewFlag": 0,
                    "Count": 0,
                    "Region": ""
                },
                "BotPkg": {
                    "ResourceIds": "",
                    "Status": 0,
                    "Region": 0,
                    "BeginTime": "",
                    "EndTime": "",
                    "InquireNum": 0,
                    "UsedNum": 0
                },
                "FraudPkg": {
                    "ResourceIds": "",
                    "Status": "",
                    "Region": 0,
                    "BeginTime": "",
                    "EndTime": "",
                    "InquireNum": 0,
                    "UsedNum": 0
                }
            },
            {
                "AppId": 251197211,
                "InstanceId": "waf_2kuhdsiw008rwhxt",
                "InstanceName": "gz-Defaultssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss",
                "ResourceIds": "waf_2kuhdsiw008rwhxt",
                "Edition": "clb-waf",
                "Region": "",
                "PayMode": 1,
                "RenewFlag": 1,
                "Level": 4,
                "ValidTime": "2021-08-15 14:21:58",
                "BeginTime": "0001-01-01 00:00:00",
                "SubDomainLimit": 40,
                "MainDomainLimit": 4,
                "Mode": 0,
                "DomainCount": 0,
                "MainDomainCount": 0,
                "MaxQPS": 0,
                "QPS": {
                    "ResourceIds": "",
                    "ValidTime": "",
                    "RenewFlag": 0,
                    "Count": 0,
                    "Region": ""
                },
                "DomainPkg": {
                    "ResourceIds": "",
                    "ValidTime": "",
                    "RenewFlag": 0,
                    "Count": 0,
                    "Region": ""
                },
                "BotPkg": {
                    "ResourceIds": "",
                    "Status": 0,
                    "Region": 0,
                    "BeginTime": "",
                    "EndTime": "",
                    "InquireNum": 0,
                    "UsedNum": 0
                },
                "FraudPkg": {
                    "ResourceIds": "",
                    "Status": "",
                    "Region": 0,
                    "BeginTime": "",
                    "EndTime": "",
                    "InquireNum": 0,
                    "UsedNum": 0
                }
            },
            {
                "AppId": 251197211,
                "InstanceId": "waf_2kuhdkt4008qolw5",
                "InstanceName": "带服务实例",
                "ResourceIds": "waf_2kuhdkt4008qolw5",
                "Edition": "sparta-waf",
                "Region": "gz",
                "PayMode": 1,
                "RenewFlag": 1,
                "Level": 4,
                "ValidTime": "2021-08-14 15:14:55",
                "BeginTime": "0001-01-01 00:00:00",
                "SubDomainLimit": 40,
                "MainDomainLimit": 4,
                "Mode": 0,
                "DomainCount": 12,
                "MainDomainCount": 1,
                "MaxQPS": 0,
                "QPS": {
                    "ResourceIds": "waf_2kuhdkt4008qolw5_qps",
                    "ValidTime": "2021-08-14 15:15:01",
                    "RenewFlag": 1,
                    "Count": 1000,
                    "Region": "gz"
                },
                "DomainPkg": {
                    "ResourceIds": "waf_2kuhdkt4008qolw5_dmn",
                    "ValidTime": "2021-08-14 15:15:10",
                    "RenewFlag": 1,
                    "Count": 1,
                    "Region": "gz"
                },
                "BotPkg": {
                    "ResourceIds": "",
                    "Status": 0,
                    "Region": 0,
                    "BeginTime": "",
                    "EndTime": "",
                    "InquireNum": 0,
                    "UsedNum": 0
                },
                "FraudPkg": {
                    "ResourceIds": "",
                    "Status": "",
                    "Region": 0,
                    "BeginTime": "",
                    "EndTime": "",
                    "InquireNum": 0,
                    "UsedNum": 0
                }
            },
            {
                "AppId": 251197211,
                "InstanceId": "waf_2kuhdkt4008qnip1",
                "InstanceName": "gz-Default",
                "ResourceIds": "waf_2kuhdkt4008qnip1",
                "Edition": "clb-waf",
                "Region": "",
                "PayMode": 1,
                "RenewFlag": 1,
                "Level": 4,
                "ValidTime": "2021-08-14 15:10:38",
                "BeginTime": "0001-01-01 00:00:00",
                "SubDomainLimit": 40,
                "MainDomainLimit": 4,
                "Mode": 0,
                "DomainCount": 0,
                "MainDomainCount": 0,
                "MaxQPS": 0,
                "QPS": {
                    "ResourceIds": "waf_2kuhdkt4008qnip1_qps",
                    "ValidTime": "2021-08-14 15:10:38",
                    "RenewFlag": 1,
                    "Count": 1000,
                    "Region": "gz"
                },
                "DomainPkg": {
                    "ResourceIds": "",
                    "ValidTime": "",
                    "RenewFlag": 0,
                    "Count": 0,
                    "Region": ""
                },
                "BotPkg": {
                    "ResourceIds": "",
                    "Status": 0,
                    "Region": 0,
                    "BeginTime": "",
                    "EndTime": "",
                    "InquireNum": 0,
                    "UsedNum": 0
                },
                "FraudPkg": {
                    "ResourceIds": "",
                    "Status": "",
                    "Region": 0,
                    "BeginTime": "",
                    "EndTime": "",
                    "InquireNum": 0,
                    "UsedNum": 0
                }
            },
            {
                "AppId": 251197211,
                "InstanceId": "waf_2kuhdkt4008qnsr9",
                "InstanceName": "测试实例",
                "ResourceIds": "waf_2kuhdkt4008qnsr9",
                "Edition": "sparta-waf",
                "Region": "gz",
                "PayMode": 1,
                "RenewFlag": 1,
                "Level": 4,
                "ValidTime": "2022-09-14 14:24:02",
                "BeginTime": "2021-10-09 15:10:55",
                "SubDomainLimit": 40,
                "MainDomainLimit": 4,
                "Mode": 0,
                "DomainCount": 7,
                "MainDomainCount": 2,
                "MaxQPS": 5,
                "QPS": {
                    "ResourceIds": "",
                    "ValidTime": "",
                    "RenewFlag": 0,
                    "Count": 0,
                    "Region": ""
                },
                "DomainPkg": {
                    "ResourceIds": "",
                    "ValidTime": "",
                    "RenewFlag": 0,
                    "Count": 0,
                    "Region": ""
                },
                "BotPkg": {
                    "ResourceIds": "",
                    "Status": 0,
                    "Region": 0,
                    "BeginTime": "",
                    "EndTime": "",
                    "InquireNum": 0,
                    "UsedNum": 0
                },
                "FraudPkg": {
                    "ResourceIds": "",
                    "Status": "",
                    "Region": 0,
                    "BeginTime": "",
                    "EndTime": "",
                    "InquireNum": 0,
                    "UsedNum": 0
                }
            },
            {
                "AppId": 251197211,
                "InstanceId": "yuyuyuyuyu",
                "InstanceName": "ModifyNamessssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss",
                "ResourceIds": "waf_2kuf279k004v9eb7",
                "Edition": "sparta-waf",
                "Region": "cd",
                "PayMode": 1,
                "RenewFlag": 0,
                "Level": 4,
                "ValidTime": "2021-07-01 20:27:54",
                "BeginTime": "0001-01-01 00:00:00",
                "SubDomainLimit": 40,
                "MainDomainLimit": 4,
                "Mode": 0,
                "DomainCount": 38,
                "MainDomainCount": 4,
                "MaxQPS": 2,
                "QPS": {
                    "ResourceIds": "",
                    "ValidTime": "",
                    "RenewFlag": 0,
                    "Count": 0,
                    "Region": ""
                },
                "DomainPkg": {
                    "ResourceIds": "",
                    "ValidTime": "",
                    "RenewFlag": 0,
                    "Count": 0,
                    "Region": ""
                },
                "BotPkg": {
                    "ResourceIds": "",
                    "Status": 0,
                    "Region": 0,
                    "BeginTime": "",
                    "EndTime": "",
                    "InquireNum": 0,
                    "UsedNum": 0
                },
                "FraudPkg": {
                    "ResourceIds": "",
                    "Status": "",
                    "Region": 0,
                    "BeginTime": "",
                    "EndTime": "",
                    "InquireNum": 0,
                    "UsedNum": 0
                }
            },
            {
                "AppId": 251197211,
                "InstanceId": "waf_2kugqn6w007lhqhd",
                "InstanceName": "gz-Default",
                "ResourceIds": "waf_2kugqn6w007lhqhd",
                "Edition": "clb-waf",
                "Region": "gz",
                "PayMode": 1,
                "RenewFlag": 1,
                "Level": 4,
                "ValidTime": "2021-07-07 16:45:33",
                "BeginTime": "0001-01-01 00:00:00",
                "SubDomainLimit": 40,
                "MainDomainLimit": 4,
                "Mode": 1,
                "DomainCount": 2,
                "MainDomainCount": 2,
                "MaxQPS": 0,
                "QPS": {
                    "ResourceIds": "",
                    "ValidTime": "",
                    "RenewFlag": 0,
                    "Count": 0,
                    "Region": ""
                },
                "DomainPkg": {
                    "ResourceIds": "",
                    "ValidTime": "",
                    "RenewFlag": 0,
                    "Count": 0,
                    "Region": ""
                },
                "BotPkg": {
                    "ResourceIds": "",
                    "Status": 0,
                    "Region": 0,
                    "BeginTime": "",
                    "EndTime": "",
                    "InquireNum": 0,
                    "UsedNum": 0
                },
                "FraudPkg": {
                    "ResourceIds": "",
                    "Status": "",
                    "Region": 0,
                    "BeginTime": "",
                    "EndTime": "",
                    "InquireNum": 0,
                    "UsedNum": 0
                }
            }
        ]
    }
}
```

