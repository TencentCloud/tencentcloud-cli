**Example 1: 创建MCP工具**



Input: 

```
tccli cngw CreateCloudNativeAPIGatewayMCPTool --cli-unfold-argument  \
    --GatewayId gateway-99761825 \
    --ServerId 5483b23c-690f-494b-949c-a2a969e02561 \
    --Name echo_500 \
    --Description echo tool for echo_500 \
    --Method POST \
    --Path /echo500 \
    --ContentType application/json \
    --InputParams.0.Name note \
    --InputParams.0.Type string \
    --InputParams.0.Required False \
    --InputParams.0.Position query \
    --InputParams.0.Description optional note
```

Output: 
```
{
    "Response": {
        "Result": {
            "Success": true,
            "ID": "7fae6228-c9c6-4d8a-9a63-8b4cd678f3f4"
        },
        "RequestId": "09f1adda-fdfd-4cb7-848d-5d6dfdeb2819"
    }
}
```

