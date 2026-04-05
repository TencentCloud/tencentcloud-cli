**Example 1: 成功**



Input: 

```
tccli wedata GetEngineKernelParameters --cli-unfold-argument  \
    --WorkspaceId workspace_id_test \
    --EngineName dlc-spark \
    --EngineRegion ap-guangzhou
```

Output: 
```
{
    "Response": {
        "Data": {
            "EngineName": "dlc-spark",
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
                    "CurrentValue": "4",
                    "DefaultValue": "4",
                    "Key": "KERNEL_CONTAINER_POD_SPARK-EXECUTOR_NUM_MAX",
                    "Name": "Spark executor最大个数",
                    "Options": [],
                    "Required": false,
                    "Type": "Text",
                    "ValueType": "int"
                }
            ]
        },
        "RequestId": "22e7dc5b-2acc-4474-9fe9-e73b86a0211c"
    }
}
```

