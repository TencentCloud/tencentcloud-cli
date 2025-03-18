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
    --Limit 1 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "RequestId": "b96d80d2-51b4-4f0f-8501-90b5ed5f0cfc",
        "TemplateList": [
            {
                "TemplateCreateTime": "2024-07-01 15:26:46",
                "TemplateDescription": "test-descrition",
                "TemplateId": 1959,
                "TemplateIsUsed": 1,
                "TemplateSource": 0,
                "TemplateTag": "资源归属:研发组",
                "TemplateTitle": "经验库编辑",
                "TemplateUpdateTime": "2024-07-01 15:48:26",
                "TemplateUsedNum": 0
            }
        ],
        "Total": 22
    }
}
```

