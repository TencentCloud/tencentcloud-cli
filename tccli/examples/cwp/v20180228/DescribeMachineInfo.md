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
        "AgentVersion": "1.0.1",
        "FreeMalwaresLeft": 0,
        "FreeVulsLeft": 0,
        "HasAssetScan": 0,
        "InstanceId": "ins-ivkxaaaa",
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
        "Quuid": "a081a69d-aaaa-bbbb-b456-59f381de839b",
        "RequestId": "8564b09e-0e04-4516-bb59-db09742503c2",
        "Uuid": "a081a69d-aaaa-bbbb-b456-59f381de839b"
    }
}
```

