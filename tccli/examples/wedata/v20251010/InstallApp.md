**Example 1: 安装应用**



Input: 

```
tccli wedata InstallApp --cli-unfold-argument  \
    --WorkspaceId 17678671667189298 \
    --AppName app1234567 \
    --Description 这是app \
    --AppType AGENT \
    --Resources.0.ResourceType mlflow \
    --Resources.0.ResourceKey rk \
    --Resources.0.ResourceValue rv \
    --Resources.0.ResourceName rn \
    --Resources.0.Permission edit \
    --TemplateKey 5139ea16-26b4-11f1-a6da-00f100004023
```

Output: 
```
{
    "Response": {
        "Data": {
            "Key": "62bac6d11774269180455f6376c7a"
        },
        "RequestId": "a82f209b-2a57-42a5-b842-b8860ef8dc89"
    }
}
```

