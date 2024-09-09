**Example 1: YARN资源调度-变更详情**



Input: 

```
tccli emr DescribeResourceScheduleDiffDetail --cli-unfold-argument  \
    --InstanceId emr-xxx \
    --Scheduler fair
```

Output: 
```
{
    "Response": {
        "Details": [
            {
                "Count": 1,
                "Header": [
                    {
                        "Id": "Attribute",
                        "Name": "属性"
                    },
                    {
                        "Id": "InEffect",
                        "Name": "当前生效值"
                    },
                    {
                        "Id": "PendingEffectiveness",
                        "Name": "待生效值"
                    },
                    {
                        "Id": "Operation",
                        "Name": "操作"
                    }
                ],
                "Name": "全局配置",
                "Rows": [
                    {
                        "Attribute": "Scheduler",
                        "InEffect": "fair",
                        "Operation": "更新",
                        "PendingEffectiveness": "capacity"
                    }
                ]
            },
            {
                "Count": 1,
                "Header": [
                    {
                        "Id": "Attribute",
                        "Name": "属性"
                    },
                    {
                        "Id": "InEffect",
                        "Name": "当前生效值"
                    },
                    {
                        "Id": "PendingEffectiveness",
                        "Name": "待生效值"
                    },
                    {
                        "Id": "Operation",
                        "Name": "操作"
                    }
                ],
                "Name": "标签开关",
                "Rows": [
                    {
                        "Attribute": "LabelDir",
                        "InEffect": "",
                        "Operation": "更新",
                        "PendingEffectiveness": ""
                    }
                ]
            }
        ],
        "RequestId": "50ed72af-1cc9-4566-8080-3594994aea80"
    }
}
```

