**Example 1: 创建tool**



Input: 

```
tccli ags CreateSandboxTool --cli-unfold-argument  \
    --ToolName demo-tst \
    --ToolType waa \
    --NetworkConfiguration.NetworkMode PUBLIC
```

Output: 
```
{
    "Response": {
        "ToolId": "sdt-mm3241p7",
        "RequestId": "1d3f073a-3d3e-4a10-8628-f94020498665"
    }
}
```

**Example 2: 创建自定义镜像的tool**



Input: 

```
tccli ags CreateSandboxTool --cli-unfold-argument  \
    --ToolName tool_img_tst \
    --ToolType waa \
    --NetworkConfiguration.NetworkMode PUBLIC \
    --ComputerConfiguration.WAAConfiguration.ImageId img-pamebyja
```

Output: 
```
{
    "Response": {
        "ToolId": "sdt-p8auk8v3",
        "RequestId": "75310f95-d0ff-4756-891e-6c0e8b0c64f2"
    }
}
```

