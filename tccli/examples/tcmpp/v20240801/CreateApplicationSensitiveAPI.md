**Example 1: CreateApplicationSensitiveAPI**



Input: 

```
tccli tcmpp CreateApplicationSensitiveAPI --cli-unfold-argument  \
    --ApplicationId app-cc6g35711m \
    --APIList.0.APIDesc testState \
    --APIList.0.APIName testState \
    --APIList.0.APIType 2 \
    --PlatformId T04257DS9431720WTAG
```

Output: 
```
{
    "Response": {
        "Data": {
            "Result": true
        },
        "RequestId": "25fd4b4d-0395-42b6-8d55-6aefa62827c2"
    }
}
```

