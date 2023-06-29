**Example 1: 创建边缘单元EdgeUnit模板**



Input: 

```
tccli iecp DescribeEdgeUnitNodeUnitTemplates --cli-unfold-argument  \
    --EdgeUnitId 8367274 \
    --Namespace default \
    --NameFilter 
```

Output: 
```
{
    "Response": {
        "RequestId": "5ebf13a2-f925-4ba7-adff-ddbc21d355e3",
        "Total": 2,
        "NodeUnitTemplates": [
            {
                "ID": 100003,
                "Name": "auto-code1",
                "Namespace": "default",
                "Description": "Description",
                "NodeGroups": [
                    "dsdsdsd-group"
                ],
                "NodeList": [
                    {
                        "ID": 82955,
                        "NodeName": "test-node1"
                    },
                    {
                        "ID": 82956,
                        "NodeName": "dev00311"
                    },
                    {
                        "ID": 82957,
                        "NodeName": "dev005"
                    }
                ],
                "UpdateTime": "2021-08-11 08:52:40",
                "CreateTime": "2021-08-11 08:52:40"
            },
            {
                "ID": 100002,
                "Name": "auto-code",
                "Namespace": "default",
                "Description": "Description",
                "NodeGroups": [
                    "dsdsdsd-group"
                ],
                "NodeList": [
                    {
                        "ID": 82958,
                        "NodeName": "logofox"
                    },
                    {
                        "ID": 82956,
                        "NodeName": "dev00311"
                    }
                ],
                "UpdateTime": "2021-08-11 08:50:27",
                "CreateTime": "2021-08-11 08:50:27"
            }
        ]
    }
}
```

