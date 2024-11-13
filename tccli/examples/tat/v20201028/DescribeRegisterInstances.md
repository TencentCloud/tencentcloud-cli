**Example 1: 根据Filters查询托管实例**

根据Filters查询托管实例。

Input: 

```
tccli tat DescribeRegisterInstances --cli-unfold-argument  \
    --Filters.0.Name instance-name \
    --Filters.0.Values WebServer-01 \
    --Offset 0 \
    --Limit 0
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "RegisterInstanceSet": [
            {
                "RegisterCodeId": "4a0f151f-a07a-494d-a2f2-8ea2ec4639eb488f31f9-b656-4f45-823d-5a90b07c7116",
                "InstanceId": "rins-uf673dgi",
                "InstanceName": "WebServer-01",
                "MachineId": "m-i2345678",
                "SystemName": "Windows",
                "HostName": "webserver01",
                "LocalIp": "10.0.0.1",
                "PublicKey": "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQC... user@hostname",
                "Status": "RUNNING",
                "CreatedTime": "2020-09-22T08:00:00Z",
                "UpdatedTime": "2020-09-22T08:00:00Z"
            }
        ],
        "RequestId": "e28b9a8c-d7d3-4a12-bf8a-0123456789ab"
    }
}
```

**Example 2: 根据托管实例ID查询托管实例**

根据托管实例ID查询托管实例。

Input: 

```
tccli tat DescribeRegisterInstances --cli-unfold-argument  \
    --InstanceIds rins-uf673dgi \
    --Offset 0 \
    --Limit 0
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "RegisterInstanceSet": [
            {
                "RegisterCodeId": "4a0f151f-a07a-494d-a2f2-8ea2ec4639eb488f31f9-b656-4f45-823d-5a90b07c7116",
                "InstanceId": "rins-uf673dgi",
                "InstanceName": "WebServer-01",
                "MachineId": "m-i2345678",
                "SystemName": "Windows",
                "HostName": "webserver01",
                "LocalIp": "10.0.0.1",
                "PublicKey": "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQC... user@hostname",
                "Status": "RUNNING",
                "CreatedTime": "2020-09-22T08:00:00Z",
                "UpdatedTime": "2020-09-22T08:00:00Z"
            }
        ],
        "RequestId": "e28b9a8c-d7d3-4a12-bf8a-0123456789ab"
    }
}
```

