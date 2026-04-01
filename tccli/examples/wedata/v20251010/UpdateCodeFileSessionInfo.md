**Example 1: 成功响应**



Input: 

```
tccli wedata UpdateCodeFileSessionInfo --cli-unfold-argument  \
    --CodeFileId a640c746-f24c-474a-b684-9c15742b9f06 \
    --WorkspaceId workspaceId_test \
    --CodeFileSession.EngineName spark-test-engine \
    --CodeFileSession.EngineRegion ap-guangzhou \
    --CodeFileSession.KernelArgs.0.DefaultValue 1 \
    --CodeFileSession.KernelArgs.0.Key KERNEL_CONTAINER_POD_SPARK-EXECUTOR_NUM \
    --CodeFileSession.KernelArgs.0.Name Executor数量 \
    --CodeFileSession.KernelArgs.0.Required True \
    --CodeFileSession.KernelArgs.0.Type Text \
    --CodeFileSession.KernelArgs.0.ValueType int \
    --CodeFileSession.KernelArgs.0.CurrentValue 1 \
    --CodeFileSession.KernelArgs.1.DefaultValue 1 \
    --CodeFileSession.KernelArgs.1.Key KERNEL_CONTAINER_POD_SPARK-EXECUTOR_NUM_MIN \
    --CodeFileSession.KernelArgs.1.Name Executor最小数量 \
    --CodeFileSession.KernelArgs.1.Required False \
    --CodeFileSession.KernelArgs.1.Type Text \
    --CodeFileSession.KernelArgs.1.ValueType int \
    --CodeFileSession.KernelArgs.1.CurrentValue 1 \
    --CodeFileSession.KernelArgs.2.DefaultValue 1 \
    --CodeFileSession.KernelArgs.2.Key KERNEL_CONTAINER_POD_SPARK-EXECUTOR_NUM_MAX \
    --CodeFileSession.KernelArgs.2.Name Executor最大数量 \
    --CodeFileSession.KernelArgs.2.Required False \
    --CodeFileSession.KernelArgs.2.Type Text \
    --CodeFileSession.KernelArgs.2.ValueType int \
    --CodeFileSession.KernelArgs.2.CurrentValue 1 \
    --CodeFileSession.KernelArgs.3.DefaultValue medium(2CU) \
    --CodeFileSession.KernelArgs.3.Key KERNEL_CONTAINER_POD_SPARK-DRIVER_SIZE \
    --CodeFileSession.KernelArgs.3.Name Driver大小 \
    --CodeFileSession.KernelArgs.3.Required False \
    --CodeFileSession.KernelArgs.3.Type Text \
    --CodeFileSession.KernelArgs.3.ValueType string \
    --CodeFileSession.KernelArgs.3.CurrentValue medium(2CU) \
    --CodeFileSession.KernelArgs.4.DefaultValue medium(2CU) \
    --CodeFileSession.KernelArgs.4.Key KERNEL_CONTAINER_POD_SPARK-EXECUTOR_SIZE \
    --CodeFileSession.KernelArgs.4.Name Executor大小 \
    --CodeFileSession.KernelArgs.4.Required False \
    --CodeFileSession.KernelArgs.4.Type Text \
    --CodeFileSession.KernelArgs.4.ValueType string \
    --CodeFileSession.KernelArgs.4.CurrentValue medium(2CU)
```

Output: 
```
{
    "Response": {
        "Data": {
            "Status": true
        },
        "RequestId": "69ec683a-b20d-470e-bbaa-81da6a602fea"
    }
}
```

