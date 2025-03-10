**Example 1: 根据Filters查询托管实例**

根据Filters查询托管实例。

Input: 

```
tccli tat DescribeRegisterInstances --cli-unfold-argument  \
    --Filters.0.Name instance-name \
    --Filters.0.Values WebServer-01 \
    --Offset 0 \
    --Limit 1
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "RegisterInstanceSet": [
            {
                "RegisterCodeId": "d0b7xxxx-a6xx-40x9-898x-44c9f508axxx",
                "InstanceId": "rins-uf673dgi",
                "InstanceName": "WebServer-01",
                "MachineId": "22c4dvvv-3ae9-4ff3-8331-d44147c96f8b",
                "SystemName": "Windows",
                "HostName": "webserver01",
                "LocalIp": "10.0.0.1",
                "PublicKey": "-----BEGIN RSA PUBLIC KEY-----\nAAAAAAAAAQEA1vVOon7U12dLFl7AOZjGnfWSMJ4rhHAagLne85Qbyn7rrow90bZF\ngsO9cpUfljliymtGAe1ZxkZZAWbwYeiS+x3KMO3rsbaXZtb9CiPSuMmyCcoyNRWy\nztLhIAHz6TFdoYYPdepY/HrL1rppGaVvUT6ufZrWIw2wF4KzPsIwGmfKYDrP+JOd\nfxkdewMwaFUP8xotqF+qi6YVbBMYSEGQyU9n42FTNxHMsLrBf1yPIcyaD+itWbWk\nyG0KcHTF2gbtgHqGV9wkc5jcqJYK3iJ1bQgEIWZ1lThRncOnHKHmSEnQ/XD5+6Hi\nLdVILVm0Gu8cnelE34kTcIqUAIQcB9wJBBBBBBBB\n-----END RSA PUBLIC KEY-----\n",
                "Status": "Online",
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
    --Limit 1
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "RegisterInstanceSet": [
            {
                "RegisterCodeId": "d0b7xxxx-a6xx-40x9-898x-44c9f508axxx",
                "InstanceId": "rins-uf673dgi",
                "InstanceName": "WebServer-01",
                "MachineId": "22c4dvvv-3ae9-4ff3-8331-d44147c96f8b",
                "SystemName": "Windows",
                "HostName": "webserver01",
                "LocalIp": "10.0.0.1",
                "PublicKey": "-----BEGIN RSA PUBLIC KEY-----\nAAAAAAAAAQEA1vVOon7U12dLFl7AOZjGnfWSMJ4rhHAagLne85Qbyn7rrow90bZF\ngsO9cpUfljliymtGAe1ZxkZZAWbwYeiS+x3KMO3rsbaXZtb9CiPSuMmyCcoyNRWy\nztLhIAHz6TFdoYYPdepY/HrL1rppGaVvUT6ufZrWIw2wF4KzPsIwGmfKYDrP+JOd\nfxkdewMwaFUP8xotqF+qi6YVbBMYSEGQyU9n42FTNxHMsLrBf1yPIcyaD+itWbWk\nyG0KcHTF2gbtgHqGV9wkc5jcqJYK3iJ1bQgEIWZ1lThRncOnHKHmSEnQ/XD5+6Hi\nLdVILVm0Gu8cnelE34kTcIqUAIQcB9wJBBBBBBBB\n-----END RSA PUBLIC KEY-----\n",
                "Status": "Online",
                "CreatedTime": "2020-09-22T08:00:00Z",
                "UpdatedTime": "2020-09-22T08:00:00Z"
            }
        ],
        "RequestId": "e28b9a8c-d7d3-4a12-bf8a-0123456789ab"
    }
}
```

