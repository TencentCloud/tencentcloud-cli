**Example 1: 示例**

示例

Input: 

```
tccli iecp DescribeEdgeUnitNodeGroup --cli-unfold-argument  \
    --Namespace default \
    --EdgeUnitId 75 \
    --Offset 0 \
    --Limit 10 \
    --NameFilter 
```

Output: 
```
{
    "Response": {
        "RequestId": "a40873bd-dad3-4dd6-b3cc-5e939f467df6",
        "Total": 3,
        "NodeGroupInfo": [
            {
                "Description": "",
                "CreateTime": "2021-11-23 16:35:57",
                "NodeGroupName": "ddd2-group-ecp",
                "DeploymentGridList": [
                    {
                        "Name": "ccc",
                        "Id": 100553
                    }
                ],
                "StatefulSetGridList": [],
                "Protect": false
            },
            {
                "Description": "",
                "CreateTime": "2021-11-23 16:35:48",
                "NodeGroupName": "ddd-group-ecp",
                "DeploymentGridList": [],
                "StatefulSetGridList": [],
                "Protect": false
            },
            {
                "Description": "",
                "CreateTime": "2021-11-19 14:46:46",
                "NodeGroupName": "aa-group-ecp",
                "DeploymentGridList": [],
                "StatefulSetGridList": [
                    {
                        "Name": "aaa",
                        "Id": 100552
                    }
                ],
                "Protect": false
            }
        ]
    }
}
```

