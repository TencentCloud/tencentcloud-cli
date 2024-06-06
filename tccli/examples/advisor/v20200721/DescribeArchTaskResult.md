**Example 1: 获取结果**

获取结果

Input: 

```
tccli advisor DescribeArchTaskResult --cli-unfold-argument  \
    --ArchTaskResultId e230bba2-xxx-4996-bbb2-62939bb43b7b
```

Output: 
```
{
    "Response": {
        "RequestId": "b90a5cc7-1a1e-4fcd-a7ee-46f767be7b38",
        "ArchId": "arch-jcxtbe9t",
        "ArchName": "架构图1",
        "CreateTime": "2023-11-14 10:29:04",
        "CreateUin": "123",
        "UpdateTime": "2023-11-14 10:29:04",
        "UpdateUin": "123",
        "VersionName": "版本1",
        "NodeList": [
            {
                "NodeId": 223120,
                "DiagramId": "diagramid",
                "NodeName": "CVM节点",
                "ProductType": "CVM",
                "ResourceList": [
                    {
                        "Attributes": "aaa",
                        "InstanceId": "ins-j7uxx5im"
                    },
                    {
                        "Attributes": "bbb",
                        "InstanceId": "ins-a8sxx5im"
                    }
                ]
            }
        ]
    }
}
```

