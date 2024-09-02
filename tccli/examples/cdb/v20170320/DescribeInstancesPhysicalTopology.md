**Example 1: 查询实例的拓扑**

输入主实例 ID ，查询实例的拓扑信息

Input: 

```
tccli cdb DescribeInstancesPhysicalTopology --cli-unfold-argument  \
    --InstanceIds test
```

Output: 
```
{
    "Response": {
        "Items": [
            {
                "InstanceId": "cdb-testa",
                "MasterIp": "xxx.xxx.xxx.xxx",
                "RoInfo": [
                    {
                        "Ip": "xxx.xxx.xxx.xxx",
                        "RoInstanceId": "cdbro-testp"
                    },
                    {
                        "Ip": "xxx.xxx.xxx.xxx",
                        "RoInstanceId": "cdbro-testm"
                    }
                ],
                "Slaves": [
                    {
                        "Ip": "xxx.xxx.xxx.xxx",
                        "Status": "online"
                    }
                ]
            }
        ],
        "RequestId": "6c0e4bae-8297-41a5-9c37-5d9172134eff"
    }
}
```

