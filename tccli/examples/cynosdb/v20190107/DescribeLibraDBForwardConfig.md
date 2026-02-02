**Example 1: 查询分析实例转发参数配置**



Input: 

```
tccli cynosdb DescribeLibraDBForwardConfig --cli-unfold-argument  \
    --InstanceId libradb-ins-ex0klgmh
```

Output: 
```
{
    "Response": {
        "ForwardList": [
            {
                "InstanceId": "cynosdbmysql-ins-62lfwjfx",
                "Region": "ap-qingyuan"
            }
        ],
        "ForwardMode": "AUTO",
        "RequestId": "64d9f1c8-3993-47be-bfea-d63943d08248"
    }
}
```

