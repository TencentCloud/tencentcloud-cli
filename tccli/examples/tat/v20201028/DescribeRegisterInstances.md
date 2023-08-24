**Example 1: 根据Filters查询托管实例**

根据Filters查询托管实例。

Input: 

```
tccli tat DescribeRegisterInstances --cli-unfold-argument  \
    --Filters.0.Name instance-name \
    --Filters.0.Values abc \
    --Offset 0 \
    --Limit 0
```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "RegisterInstanceSet": [
            {
                "RegisterCodeId": "abc",
                "InstanceId": "abc",
                "InstanceName": "abc",
                "MachineId": "abc",
                "SystemName": "abc",
                "HostName": "abc",
                "LocalIp": "abc",
                "PublicKey": "abc",
                "Status": "abc",
                "CreatedTime": "2020-09-22T00:00:00+00:00",
                "UpdatedTime": "2020-09-22T00:00:00+00:00"
            }
        ],
        "RequestId": "abc"
    }
}
```

**Example 2: 根据托管实例ID查询托管实例**

根据托管实例ID查询托管实例。

Input: 

```
tccli tat DescribeRegisterInstances --cli-unfold-argument  \
    --InstanceIds abc \
    --Offset 0 \
    --Limit 0
```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "RegisterInstanceSet": [
            {
                "RegisterCodeId": "abc",
                "InstanceId": "abc",
                "InstanceName": "abc",
                "MachineId": "abc",
                "SystemName": "abc",
                "HostName": "abc",
                "LocalIp": "abc",
                "PublicKey": "abc",
                "Status": "abc",
                "CreatedTime": "2020-09-22T00:00:00+00:00",
                "UpdatedTime": "2020-09-22T00:00:00+00:00"
            }
        ],
        "RequestId": "abc"
    }
}
```

