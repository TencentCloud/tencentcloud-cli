**Example 1: 测试示例**



Input: 

```
tccli tchousex DescribeMCPInstance --cli-unfold-argument  \
    --EngineInstanceId instance-68rta19d \
    --EngineType TCHouseX
```

Output: 
```
{
    "Response": {
        "InstanceInfo": {
            "CreateTime": "2025-06-10 11:36:17",
            "EngineInstanceId": "instance-68rta19d",
            "EngineType": "TCHouseX",
            "EngineUserName": "fzx",
            "InstanceID": "mcp-zyarlx4v",
            "InstanceName": "test",
            "MCPHost": "9.0.0.52",
            "MCPPaasSubnetID": "",
            "MCPPaasVpcID": "vpc-3thzsvzr",
            "MCPPort": 31234,
            "SSEUrl": "http://10.0.3.50:31234/sse?key=efbmfI4hX0sMTpYRbQ7wjCO3sHzv3OlKFG18Qid%2BaRybgyS3%2FW8fGAoPiyiqCa8SlZJVQZ76uuHVZI9%2FNxeJcQ%3D%3D",
            "Status": 2,
            "Upgrade": false,
            "UserSubnetID": "subnet-ges7jtu0",
            "UserVpcID": "vpc-evtecfx3",
            "Version": ""
        },
        "RequestId": "fdd720c0-f4b6-49df-9154-14b7f7f53c38"
    }
}
```

