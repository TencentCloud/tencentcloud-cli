**Example 1: 访问实例**

根据实例数字id查询实例信息


Input: 

```
tccli redis DescribeInstancesByIdsInternal --cli-unfold-argument  \
    --InstanceIds 40040052 2031210388
```

Output: 
```
{
    "Response": {
        "InstanceSet": [
            {
                "Appid": 1322111773,
                "AzMode": 2,
                "CreateTime": "",
                "CurrentProxyVersion": "5.8.10",
                "CurrentRedisVersion": "7.0.22",
                "InstanceId": 40040000,
                "InstanceName": "crs-0y59u***",
                "Locked": 0,
                "Locker": 0,
                "MonitorVersion": 1,
                "PolarisServer": "",
                "ProductVersion": "local",
                "RegionId": 16,
                "SerialId": "crs-0y59u***",
                "Status": 2,
                "SubnetId": 1702798,
                "Type": 17,
                "Uin": "100034079035",
                "UpdateTime": "2025-01-22 11:12:48",
                "UpgradeProxyVersion": "",
                "UpgradeRedisVersion": "",
                "VPort": 6379,
                "Vip": "172.27.0.12",
                "VpcId": 3606966,
                "WanAddress": "",
                "ZoneId": 160001
            }
        ],
        "RequestId": "e60cf466-8daa-4feb-a230-d938ef21*****",
        "TotalCount": 1
    }
}
```

