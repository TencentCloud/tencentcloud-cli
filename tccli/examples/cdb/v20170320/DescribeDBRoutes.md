**Example 1: 查询云数据库实例的路由示例**



Input: 

```
tccli cdb DescribeDBRoutes --cli-unfold-argument  \
    --InstanceId cdb-q0ltezep
```

Output: 
```
{
    "Response": {
        "Routers": [
            {
                "VipType": 4,
                "VipList": [
                    {
                        "Vip": "100.99.102.3",
                        "Vport": 14257
                    }
                ]
            },
            {
                "VipType": 3,
                "VipList": [
                    {
                        "Vip": "10.66.133.177",
                        "Vport": 3306
                    }
                ]
            }
        ],
        "RequestId": "76c03fcf-6d45-4d18-a759-339638c1eaf1"
    }
}
```

