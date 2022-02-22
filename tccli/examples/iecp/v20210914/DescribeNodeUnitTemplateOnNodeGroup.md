**Example 1: 查询指定NodeGroup下NodeUnit模板列表**



Input: 

```
tccli iecp DescribeNodeUnitTemplateOnNodeGroup --cli-unfold-argument  \
    --EdgeUnitId 8367274 \
    --NodeGroupName test-group
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
                "CreateTime": "2021-08-11 08:52:40",
                "Relation": true
            },
            {
                "ID": 100002,
                "Name": "auto-code",
                "Namespace": "default",
                "Description": "Description",
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
                "CreateTime": "2021-08-11 08:50:27",
                "Relation": true
            }
        ]
    }
}
```

