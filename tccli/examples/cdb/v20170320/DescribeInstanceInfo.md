**Example 1: 查询给定实例详情**

查询给定实例详情

Input: 

```
tccli cdb DescribeInstanceInfo --cli-unfold-argument  \
    --UInstanceIds cdb-test1 cdb-tests
```

Output: 
```
{
    "Response": {
        "Items": [
            {
                "AddTimeStamp": "2024-04-10 20:14:59",
                "AppId": 251237298,
                "CdbMem": 4000,
                "CdbType": "CLOUD_NATIVE_CLUSTER",
                "CdbVip": "",
                "CdbVolume": 200,
                "CdbVport": 0,
                "Cpu": 2,
                "Deadline": "0001-01-01 00:00:00",
                "InstType": 1,
                "InstanceNodes": 3,
                "IsolateTimeStamp": "0001-01-01 00:00:00",
                "ModTimeStamp": "2024-04-10 20:19:58",
                "OssClusterId": 628,
                "ParamVersionFlow": 800010001,
                "ProjectId": 0,
                "ResourceId": "7ccb8d85-01c8-48db-a29d-5dd6b495767a",
                "RouteName": "勿删_by_pxy",
                "Status": 1,
                "UInstanceId": "cdb-qy870gaz",
                "Vip": "172.16.0.82",
                "Vport": 3306
            }
        ],
        "RequestId": "4ee4303e-5c75-4c70-be5f-9f5b6a266abc",
        "TotalCount": 1
    }
}
```

