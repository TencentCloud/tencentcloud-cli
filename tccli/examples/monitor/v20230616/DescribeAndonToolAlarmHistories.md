**Example 1: 查询**



Input: 

```
tccli monitor DescribeAndonToolAlarmHistories --cli-unfold-argument  \
    --Namespace qce/cvm \
    --StartTime 1688555385 \
    --EndTime 1688562586 \
    --ViewName cvm_device \
    --Dimensions.0.Key abc \
    --Dimensions.0.Value 123
```

Output: 
```
{
    "Response": {
        "Histories": [
            {
                "AlertID": "7fbea3c8-4c8f-4f60-a432-9ecff0cddb7d",
                "MonitorType": "MT_QCE",
                "Namespace": "cvm_device",
                "Region": "ap-guangzhou",
                "AlarmObject": "172.16.0.42 (内)  | ins-wv6if848 | monitor测试01-自动化告警使用勿动 | vpcId: vpc-n6sb0und",
                "Content": "CPU利用率 < 30%",
                "FirstOccurTime": 1688556600,
                "LastOccurTime": 1688556675,
                "AlarmStatus": "NO_CONF",
                "PolicyName": "Autodfhbccdhhghc",
                "ProjectName": "默认项目",
                "Dimensions": [
                    {
                        "Key": "unInstanceId",
                        "Value": "ins-wv6if848"
                    }
                ]
            },
            {
                "AlertID": "2861f771-955d-4123-93a5-9f8440a5be3e",
                "MonitorType": "MT_QCE",
                "Namespace": "cvm_device",
                "Region": "ap-guangzhou",
                "AlarmObject": "172.16.0.42 (内)  | ins-wv6if848 | monitor测试01-自动化告警使用勿动 | vpcId: vpc-n6sb0und",
                "Content": "CPU利用率 < 30%",
                "FirstOccurTime": 1688556600,
                "LastOccurTime": 1688556673,
                "AlarmStatus": "NO_CONF",
                "PolicyName": "Autodfhbccbfhiah",
                "ProjectName": "默认项目",
                "Dimensions": [
                    {
                        "Key": "unInstanceId",
                        "Value": "ins-wv6if848"
                    }
                ]
            },
            {
                "AlertID": "87a2e006-acf2-40fa-91a0-ecdf37902311",
                "MonitorType": "MT_QCE",
                "Namespace": "cvm_device",
                "Region": "ap-guangzhou",
                "AlarmObject": "172.16.0.42 (内)  | ins-wv6if848 | monitor测试01-自动化告警使用勿动 | vpcId: vpc-n6sb0und",
                "Content": "CPU利用率 < 30%",
                "FirstOccurTime": 1688559180,
                "LastOccurTime": 1688559266,
                "AlarmStatus": "NO_CONF",
                "PolicyName": "Autodfhbccedjhjg",
                "ProjectName": "默认项目",
                "Dimensions": [
                    {
                        "Key": "unInstanceId",
                        "Value": "ins-wv6if848"
                    }
                ]
            },
            {
                "AlertID": "8a872551-4dcb-47b0-a7d5-d84cf8a76185",
                "MonitorType": "MT_QCE",
                "Namespace": "cvm_device",
                "Region": "ap-guangzhou",
                "AlarmObject": "172.16.0.42 (内)  | ins-wv6if848 | monitor测试01-自动化告警使用勿动 | vpcId: vpc-n6sb0und",
                "Content": "CPU利用率 < 30%",
                "FirstOccurTime": 1688559060,
                "LastOccurTime": 1688559144,
                "AlarmStatus": "NO_CONF",
                "PolicyName": "Autodfhbcchjhecb",
                "ProjectName": "默认项目",
                "Dimensions": [
                    {
                        "Key": "unInstanceId",
                        "Value": "ins-wv6if848"
                    }
                ]
            },
            {
                "AlertID": "191e5f08-b3f3-4bd4-b09f-5ce07a790165",
                "MonitorType": "MT_QCE",
                "Namespace": "cvm_device",
                "Region": "ap-guangzhou",
                "AlarmObject": "172.16.0.42 (内)  | ins-wv6if848 | monitor测试01-自动化告警使用勿动 | vpcId: vpc-n6sb0und",
                "Content": "CPU利用率 < 30%",
                "FirstOccurTime": 1688556600,
                "LastOccurTime": 1688556681,
                "AlarmStatus": "NO_CONF",
                "PolicyName": "Autodfhbcccghiaj",
                "ProjectName": "默认项目",
                "Dimensions": [
                    {
                        "Key": "unInstanceId",
                        "Value": "ins-wv6if848"
                    }
                ]
            }
        ],
        "RequestId": "abc"
    }
}
```

**Example 2: cvm告警历史查询**

cvm告警历史查询

Input: 

```
tccli monitor DescribeAndonToolAlarmHistories --cli-unfold-argument  \
    --Namespace qce/cvm \
    --StartTime 1691557550 \
    --EndTime 1691653157 \
    --ViewName cvm_device \
    --Dimensions.0.Key vm_uuid \
    --Dimensions.0.Value 5245b964-3c0b-4ff0-b108-179f94265be7
```

Output: 
```
{
    "Response": {
        "Histories": [
            {
                "AlarmObject": "172.16.0.38 (内)  | ins-wvm5sfv0 | eb标签测试 | vpcId: vpc-7f1rezj5",
                "AlarmStatus": "NO_CONF",
                "AlertID": "24265b5b-6510-483a-89ab-bb75a762129f",
                "Content": "CPU利用率 <= 100%  &&  (CPU利用率 >= 100%  ||  内存利用率 >= 0%)",
                "Dimensions": [
                    {
                        "Key": "vm_uuid",
                        "Value": "5245b964-3c0b-4ff0-b108-179f94265be7"
                    },
                    {
                        "Key": "appid",
                        "Value": "251000916"
                    },
                    {
                        "Key": "projectid",
                        "Value": "0"
                    }
                ],
                "FirstOccurTime": 1691567700,
                "LastOccurTime": 1691567945,
                "MonitorType": "MT_QCE",
                "Namespace": "cvm_device",
                "PolicyId": "",
                "PolicyName": "复合告警回调测试",
                "ProjectId": 0,
                "ProjectName": "barad",
                "Region": "ap-guangzhou"
            }
        ],
        "RequestId": "52ac1ee5-8151-46eb-89a8-8d7e1be437b8"
    }
}
```

**Example 3: cvm测试查询多条返回记录**

cvm测试查询多条返回记录

Input: 

```
tccli monitor DescribeAndonToolAlarmHistories --cli-unfold-argument  \
    --Namespace qce/cvm \
    --StartTime 1691384750 \
    --EndTime 1691653157 \
    --ViewName cvm_device \
    --Dimensions.0.Key vm_uuid \
    --Dimensions.0.Value 5245b964-3c0b-4ff0-b108-179f94265be7
```

Output: 
```
{
    "Response": {
        "Histories": [
            {
                "AlarmObject": "172.16.0.38 (内)  | ins-wvm5sfv0 | eb标签测试 | vpcId: vpc-7f1rezj5",
                "AlarmStatus": "ALARM",
                "AlertID": "27a0560a-2009-4338-b5c8-4e6acf15d75d",
                "Content": "内存利用率 <= 90%",
                "Dimensions": [
                    {
                        "Key": "vm_uuid",
                        "Value": "5245b964-3c0b-4ff0-b108-179f94265be7"
                    },
                    {
                        "Key": "appid",
                        "Value": "251000916"
                    },
                    {
                        "Key": "projectid",
                        "Value": "0"
                    }
                ],
                "FirstOccurTime": 1691461560,
                "LastOccurTime": 1691641920,
                "MonitorType": "MT_QCE",
                "Namespace": "cvm_device",
                "PolicyId": "",
                "PolicyName": "测试发送",
                "ProjectId": 0,
                "ProjectName": "barad",
                "Region": "ap-guangzhou"
            },
            {
                "AlarmObject": "172.16.0.38 (内)  | ins-wvm5sfv0 | eb标签测试 | vpcId: vpc-7f1rezj5",
                "AlarmStatus": "ALARM",
                "AlertID": "38399ccc-bda9-4a0f-b3c9-81bd4d44777b",
                "Content": "磁盘利用率 <= 95%",
                "Dimensions": [
                    {
                        "Key": "projectid",
                        "Value": "0"
                    },
                    {
                        "Key": "vm_uuid",
                        "Value": "5245b964-3c0b-4ff0-b108-179f94265be7"
                    },
                    {
                        "Key": "appid",
                        "Value": "251000916"
                    }
                ],
                "FirstOccurTime": 1691461560,
                "LastOccurTime": 1691641920,
                "MonitorType": "MT_QCE",
                "Namespace": "cvm_device",
                "PolicyId": "",
                "PolicyName": "测试发送",
                "ProjectId": 0,
                "ProjectName": "barad",
                "Region": "ap-guangzhou"
            },
            {
                "AlarmObject": "172.16.0.38 (内)  | ins-wvm5sfv0 | eb标签测试 | vpcId: vpc-7f1rezj5",
                "AlarmStatus": "ALARM",
                "AlertID": "8b24c37a-686a-4aab-976f-003463b205e8",
                "Content": "CPU利用率 <= 80%",
                "Dimensions": [
                    {
                        "Key": "vm_uuid",
                        "Value": "5245b964-3c0b-4ff0-b108-179f94265be7"
                    },
                    {
                        "Key": "appid",
                        "Value": "251000916"
                    },
                    {
                        "Key": "projectid",
                        "Value": "0"
                    }
                ],
                "FirstOccurTime": 1691461320,
                "LastOccurTime": 1691641620,
                "MonitorType": "MT_QCE",
                "Namespace": "cvm_device",
                "PolicyId": "",
                "PolicyName": "测试发送",
                "ProjectId": 0,
                "ProjectName": "barad",
                "Region": "ap-guangzhou"
            },
            {
                "AlarmObject": "172.16.0.38 (内)  | ins-wvm5sfv0 | eb标签测试 | vpcId: vpc-7f1rezj5",
                "AlarmStatus": "NO_CONF",
                "AlertID": "24265b5b-6510-483a-89ab-bb75a762129f",
                "Content": "CPU利用率 <= 100%  &&  (CPU利用率 >= 100%  ||  内存利用率 >= 0%)",
                "Dimensions": [
                    {
                        "Key": "projectid",
                        "Value": "0"
                    },
                    {
                        "Key": "vm_uuid",
                        "Value": "5245b964-3c0b-4ff0-b108-179f94265be7"
                    },
                    {
                        "Key": "appid",
                        "Value": "251000916"
                    }
                ],
                "FirstOccurTime": 1691567700,
                "LastOccurTime": 1691567945,
                "MonitorType": "MT_QCE",
                "Namespace": "cvm_device",
                "PolicyId": "",
                "PolicyName": "复合告警回调测试",
                "ProjectId": 0,
                "ProjectName": "barad",
                "Region": "ap-guangzhou"
            }
        ],
        "RequestId": "ec008548-70cd-4b49-847c-05a6305b0d13"
    }
}
```

