**Example 1: 成功响应**



Input: 

```
tccli wedata GetCodeFileSessionInfo --cli-unfold-argument  \
    --CodeFileId 2929edf7-998a-4086-8f70-b2f27f4cf84 \
    --WorkspaceId workspaceId_test \
    --ExtensionType ide
```

Output: 
```
{
    "Response": {
        "Data": {
            "CodeFileId": "2929edf7-998a-4086-8f70-b2f27f4cf84",
            "CodeFileSession": {
                "EngineGatewayUrl": "http://10.255.0.52:8888",
                "EngineId": "DataEngine-ge4ayz1s",
                "EngineName": "wedata30",
                "EngineRegion": "ap-guangzhou",
                "KernelArgs": [
                    {
                        "CurrentValue": "medium(2CU)",
                        "DefaultValue": "medium(2CU)",
                        "Key": "KERNEL_CONTAINER_POD_SPARK-DRIVER_SIZE",
                        "Name": "Spark driver CU数",
                        "Options": [
                            "small(1CU)",
                            "medium(2CU)",
                            "large(4CU)",
                            "xlarge(8CU)",
                            "4xlarge(16CU)"
                        ],
                        "Required": false,
                        "Type": "Option",
                        "ValueType": "string"
                    },
                    {
                        "CurrentValue": "medium(2CU)",
                        "DefaultValue": "medium(2CU)",
                        "Key": "KERNEL_CONTAINER_POD_SPARK-EXECUTOR_SIZE",
                        "Name": "Spark executor CU数",
                        "Options": [
                            "small(1CU)",
                            "medium(2CU)",
                            "large(4CU)",
                            "xlarge(8CU)",
                            "4xlarge(16CU)"
                        ],
                        "Required": false,
                        "Type": "Option",
                        "ValueType": "string"
                    },
                    {
                        "CurrentValue": "2",
                        "DefaultValue": "2",
                        "Key": "KERNEL_CONTAINER_POD_SPARK-EXECUTOR_NUM",
                        "Name": "Spark executor个数",
                        "Options": [],
                        "Required": false,
                        "Type": "Text",
                        "ValueType": "int"
                    },
                    {
                        "CurrentValue": "1",
                        "DefaultValue": "1",
                        "Key": "KERNEL_CONTAINER_POD_SPARK-EXECUTOR_NUM_MIN",
                        "Name": "Spark executor最小个数",
                        "Options": [],
                        "Required": false,
                        "Type": "Text",
                        "ValueType": "int"
                    },
                    {
                        "CurrentValue": "2",
                        "DefaultValue": "2",
                        "Key": "KERNEL_CONTAINER_POD_SPARK-EXECUTOR_NUM_MAX",
                        "Name": "Spark executor最大个数",
                        "Options": [],
                        "Required": false,
                        "Type": "Text",
                        "ValueType": "int"
                    }
                ],
                "ResourceId": "resource_002",
                "ResourceName": "数据计算型计算资源用这个"
            },
            "WorkspaceId": "workspaceId_test"
        },
        "RequestId": "ef5765e3-872f-4c51-a160-61d704d0e1e9"
    }
}
```

