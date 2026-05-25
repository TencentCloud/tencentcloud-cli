**Example 1: 查询预热资源池模版详情**



Input: 

```
tccli postgres DescribeWarmPoolTemplate --cli-unfold-argument  \
    --TemplateName test_my_template2
```

Output: 
```
{
    "Response": {
        "Template": {
            "AppId": 251242149,
            "Cpu": 1,
            "CreatedAt": "2026-05-22 15:27:11",
            "DBKernelVersion": "18",
            "Description": "测试模版用例",
            "Enabled": 1,
            "InstanceCategory": "normal",
            "MaxReady": 1,
            "Memory": 2048,
            "MinReady": 1,
            "Name": "test_my_template2",
            "PoolStatus": {
                "Assigned": 0,
                "Creating": 1,
                "Ready": 0,
                "Unhealthy": 0
            },
            "Priority": 10,
            "RegionId": 1,
            "Storage": 10,
            "StorageType": "PHYSICAL_LOCAL_SSD",
            "SubnetId": "subnet-3hekhnki",
            "Target": 1,
            "Uin": "700000733578",
            "UpdatedAt": "0000-00-00 00:00:00",
            "VpcId": "vpc-a27ykb0r",
            "ZoneKey": "ap-guangzhou-2,ap-guangzhou-3"
        },
        "RequestId": "6725e432-ab9f-4ed7-88e6-a35b78ff4aa2"
    }
}
```

