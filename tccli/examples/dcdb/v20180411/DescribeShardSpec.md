**Example 1: 查询分布式数据库可售卖分片规格**

查询可创建的分布式数据库可售卖的分片规格配置。

Input: 

```
tccli dcdb DescribeShardSpec --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "SpecConfig": [
            {
                "Machine": "TS85",
                "SpecConfigInfos": [
                    {
                        "SuitInfo": "日独立用户数上百万人的中型应用",
                        "Pid": 10820,
                        "MaxStorage": 3000000,
                        "Memory": 64000,
                        "NodeCount": 3,
                        "Qps": 33000,
                        "MinStorage": 10000,
                        "Cpu": 0
                    },
                    {
                        "SuitInfo": "日独立用户数上百万人的中型应用",
                        "Pid": 10890,
                        "MaxStorage": 3000000,
                        "Memory": 64000,
                        "NodeCount": 2,
                        "Qps": 33000,
                        "MinStorage": 10000,
                        "Cpu": 0
                    }
                ]
            }
        ],
        "RequestId": "a4ad50e3-ba73-4736-b207-954c2976613c"
    }
}
```

