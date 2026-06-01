**Example 1: 测试示例**



Input: 

```
tccli tchousex CreateMCPInstance --cli-unfold-argument  \
    --InstanceMCP.EngineType TCHouseX \
    --InstanceMCP.EngineInstanceId instance-o2tmhl57 \
    --InstanceMCP.UserVpcID vpc-evtecfx3 \
    --InstanceMCP.UserSubnetID subnet-ges7jtu0 \
    --InstanceMCP.UserPaasVpcID vpc-975qib7h \
    --InstanceMCP.EngineUserName bobpeng \
    --InstanceMCP.EnginePassword Abc123456 \
    --InstanceMCP.EngineHost 10.0.1.154 \
    --InstanceMCP.EnginePort 33060 \
    --InstanceMCP.EnginePaasHost 9.0.17.147 \
    --InstanceMCP.EnginePaasPort 33060 \
    --InstanceMCP.InstanceName mcp-bob-test
```

Output: 
```
{
    "Response": {
        "FlowId": 14767,
        "InstanceId": "mcp-em3t614q",
        "RequestId": "4ca944d8-015c-4fc6-9e64-0c4dc68737b2"
    }
}
```

**Example 2: 测试示例1**



Input: 

```
tccli tchousex CreateMCPInstance --cli-unfold-argument  \
    --InstanceMCP.EngineType TCHouseX \
    --InstanceMCP.EngineInstanceId instance-jqwy8wwl \
    --InstanceMCP.UserVpcID vpc-dvo1f851 \
    --InstanceMCP.UserSubnetID subnet-4hayacas \
    --InstanceMCP.UserPaasVpcID vpc-975qib7h \
    --InstanceMCP.EngineUserName bobpeng \
    --InstanceMCP.EnginePassword Abc123456 \
    --InstanceMCP.EngineHost 172.16.1.101 \
    --InstanceMCP.EnginePort 33060 \
    --InstanceMCP.EnginePaasHost 9.0.20.27 \
    --InstanceMCP.EnginePaasPort 33060 \
    --InstanceMCP.InstanceName bob-test
```

Output: 
```
{
    "Response": {
        "FlowId": 14786,
        "InstanceId": "mcp-8y8b8m1p",
        "RequestId": "283b690d-3cb5-40d5-8ff0-fb4a79872ac6"
    }
}
```

