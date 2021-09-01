**Example 1: 获取实例登录所需要的凭据**

获取实例登录所需要的凭据

Input: 

```
tccli gse GetInstanceAccess --cli-unfold-argument  \
    --FleetId fleet-qp3g3caa-iectl8nb \
    --InstanceId ins-gi2lxw
```

Output: 
```
{
    "Response": {
        "InstanceAccess": {
            "Credentials": {
                "Secret": "w4bksrwe3gdbqwernmlvjioqeniovmlni3289t0123n42lfn892sjdfqwionv823bnvh2ljkvs",
                "UserName": "root"
            },
            "FleetId": "fleet-qp3g3caa-iectl8nb",
            "InstanceId": "ins-gi2lxw",
            "IpAddress": "9.12.5.87",
            "OperatingSystem": "centos6.7"
        },
        "RequestId": "c7bfcad5-3f20-472f-9afc-13a66faebad8"
    }
}
```

