**Example 1: 获取机器详情**

本接口（DescribeMachineInfo）用于获取机器详细情况。

Input: 

```
tccli cwp DescribeMachineInfo --cli-unfold-argument  \
    --Uuid UUID
```

Output: 
```
{
    "Response": {
        "AgentVersion": "",
        "FreeMalwaresLeft": 0,
        "FreeVulsLeft": 0,
        "HasAssetScan": 0,
        "InstanceId": "ins-ivkx06mb",
        "IsProVersion": true,
        "MachineIp": "172.16.255.2",
        "MachineName": "tke_cls-kjg9r3fh_master_etcd1",
        "MachineOs": "TencentOS Server 3.1 (TK4)",
        "MachineRegion": "ap-shanghai",
        "MachineStatus": "ONLINE",
        "MachineType": "CVM",
        "MachineWanIp": "124.222.61.130",
        "PayMode": "PREPAY",
        "ProVersionDeadline": "2024-01-10 10:51:11",
        "ProVersionOpenDate": "2023-08-07 14:54:29",
        "ProtectDays": 98,
        "ProtectType": "Flagship",
        "Quuid": "a081a69d-b7cb-4362-b456-59f381de839b",
        "RequestId": "111",
        "Uuid": "a081a69d-b7cb-4362-b456-59f381de839b"
    }
}
```

