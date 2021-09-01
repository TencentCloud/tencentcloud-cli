**Example 1: 修改模块默认安全组**



Input: 

```
tccli ecm ModifyModuleSecurityGroups --cli-unfold-argument  \
    --SecurityGroupIdSet esg-2071nxxw esg-belgyqvu \
    --ModuleId em-06qmx7wa
```

Output: 
```
{
    "Response": {
        "RequestId": "0f092f2e-0ea2-4c20-9f22-ef4b629c99fa"
    }
}
```

