**Example 1: 获取机器详情**

本接口（DescribeMachineInfo）用于获取机器详细情况。

Input: 

```
tccli yunjing DescribeMachineInfo --cli-unfold-argument  \
    --Uuid UUID
```

Output: 
```
{
    "Response": {
        "MachineType": "CVM",
        "MachineRegion": "ap-guangzhou",
        "InstanceId": "ins-ibqb87x3",
        "MachineWanIp": "130.111.77.111",
        "MachineIp": "10.104.248.0",
        "MachineName": "开发机",
        "MachineOs": "3.10.0-327.36.3.el7.x86_64",
        "MachineStatus": "ONLINE",
        "ProtectDays": 120,
        "Quuid": "56af8eea-5a2a-4f0c-81ca-47208e7cd9b2",
        "Uuid": "e3fcbf68-3bd6-11e8-8954-0819a624c497",
        "IsProVersion": true,
        "PayMode": "PREPAY",
        "ProVersionOpenDate": "2018-07-30 12:34:22",
        "RequestId": "ad31cc35-8523-42a2-93e0-b733ad247daa"
    }
}
```

