**Example 1: 经验库列表**

查询经验库列表

Input: 

```
tccli cfg DescribeTemplateList --cli-unfold-argument  \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "RequestId": "0c06dc9d-1e90-4062-a038-74abf2bbd43d",
        "TemplateList": [
            {
                "TemplateId": 511,
                "TemplateTitle": "测试经验",
                "TemplateDescription": "测试",
                "TemplateTag": null,
                "TemplateIsUsed": 1,
                "TemplateCreateTime": "2021-10-12 17:28:13",
                "TemplateUpdateTime": "2021-10-12 17:48:16",
                "TemplateUsedNum": 0
            },
            {
                "TemplateId": 509,
                "TemplateTitle": "test",
                "TemplateDescription": "test",
                "TemplateTag": "test",
                "TemplateIsUsed": 2,
                "TemplateCreateTime": "2021-09-28 15:38:00",
                "TemplateUpdateTime": "2021-10-11 16:26:45",
                "TemplateUsedNum": 0
            }
        ],
        "Total": 2
    }
}
```

**Example 2: 查询经验列表**

查询经验列表

Input: 

```
tccli cfg DescribeTemplateList --cli-unfold-argument  \
    --Limit 10 \
    --Offset 1
```

Output: 
```
{
    "Response": {
        "RequestId": "6775138e-92c5-40cb-ab0e-a61a5c63b5fa",
        "TemplateList": [
            {
                "TemplateCreateTime": "2023-06-06 15:05:18",
                "TemplateDescription": "3",
                "TemplateId": 914,
                "TemplateIsUsed": 1,
                "TemplateSource": 0,
                "TemplateTag": "",
                "TemplateTitle": "3",
                "TemplateUpdateTime": "2023-06-06 15:05:18",
                "TemplateUsedNum": 0
            },
            {
                "TemplateCreateTime": "2023-06-05 14:43:42",
                "TemplateDescription": "从接入层、逻辑层、数据层模拟单AZ故障，进而验证架构跨可用区容灾的有效性",
                "TemplateId": 913,
                "TemplateIsUsed": 1,
                "TemplateSource": 1,
                "TemplateTag": "",
                "TemplateTitle": "跨可用区容灾演练",
                "TemplateUpdateTime": "2023-06-05 14:43:42",
                "TemplateUsedNum": 0
            },
            {
                "TemplateCreateTime": "2023-06-05 14:42:31",
                "TemplateDescription": "从接入层、逻辑层、数据层模拟单AZ故障，进而验证架构跨可用区容灾的有效性",
                "TemplateId": 912,
                "TemplateIsUsed": 1,
                "TemplateSource": 1,
                "TemplateTag": "",
                "TemplateTitle": "跨可用区容灾演练",
                "TemplateUpdateTime": "2023-06-05 14:42:31",
                "TemplateUsedNum": 0
            },
            {
                "TemplateCreateTime": "2023-06-05 11:48:02",
                "TemplateDescription": "从接入层、逻辑层、数据层模拟单AZ故障，进而验证架构跨可用区容灾的有效性",
                "TemplateId": 910,
                "TemplateIsUsed": 1,
                "TemplateSource": 1,
                "TemplateTag": "",
                "TemplateTitle": "跨可用区容灾演练",
                "TemplateUpdateTime": "2023-06-05 11:48:02",
                "TemplateUsedNum": 0
            },
            {
                "TemplateCreateTime": "2023-06-05 11:48:02",
                "TemplateDescription": "从接入层、逻辑层、数据层模拟单AZ故障，进而验证架构跨可用区容灾的有效性",
                "TemplateId": 911,
                "TemplateIsUsed": 1,
                "TemplateSource": 1,
                "TemplateTag": "",
                "TemplateTitle": "跨可用区容灾演练",
                "TemplateUpdateTime": "2023-06-05 11:48:02",
                "TemplateUsedNum": 0
            },
            {
                "TemplateCreateTime": "2023-06-02 17:38:34",
                "TemplateDescription": "从接入层、逻辑层、数据层模拟单AZ故障，进而验证架构跨可用区容灾的有效性",
                "TemplateId": 904,
                "TemplateIsUsed": 1,
                "TemplateSource": 1,
                "TemplateTag": "",
                "TemplateTitle": "跨可用区容灾演练",
                "TemplateUpdateTime": "2023-06-02 17:38:34",
                "TemplateUsedNum": 0
            },
            {
                "TemplateCreateTime": "2023-06-02 17:38:34",
                "TemplateDescription": "从接入层、逻辑层、数据层模拟单AZ故障，进而验证架构跨可用区容灾的有效性",
                "TemplateId": 905,
                "TemplateIsUsed": 1,
                "TemplateSource": 1,
                "TemplateTag": "",
                "TemplateTitle": "跨可用区容灾演练",
                "TemplateUpdateTime": "2023-06-02 17:38:34",
                "TemplateUsedNum": 0
            },
            {
                "TemplateCreateTime": "2023-06-02 17:38:34",
                "TemplateDescription": "从接入层、逻辑层、数据层模拟单AZ故障，进而验证架构跨可用区容灾的有效性",
                "TemplateId": 906,
                "TemplateIsUsed": 1,
                "TemplateSource": 1,
                "TemplateTag": "",
                "TemplateTitle": "跨可用区容灾演练",
                "TemplateUpdateTime": "2023-06-02 17:38:34",
                "TemplateUsedNum": 0
            },
            {
                "TemplateCreateTime": "2023-06-02 17:38:34",
                "TemplateDescription": "从接入层、逻辑层、数据层模拟单AZ故障，进而验证架构跨可用区容灾的有效性",
                "TemplateId": 907,
                "TemplateIsUsed": 1,
                "TemplateSource": 1,
                "TemplateTag": "",
                "TemplateTitle": "跨可用区容灾演练",
                "TemplateUpdateTime": "2023-06-02 17:38:34",
                "TemplateUsedNum": 0
            },
            {
                "TemplateCreateTime": "2023-06-02 17:38:34",
                "TemplateDescription": "从接入层、逻辑层、数据层模拟单AZ故障，进而验证架构跨可用区容灾的有效性",
                "TemplateId": 908,
                "TemplateIsUsed": 2,
                "TemplateSource": 1,
                "TemplateTag": "",
                "TemplateTitle": "跨可用区容灾演练",
                "TemplateUpdateTime": "2023-06-13 16:30:37",
                "TemplateUsedNum": 0
            }
        ],
        "Total": 43
    }
}
```

