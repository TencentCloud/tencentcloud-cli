**Example 1: 创建app**



Input: 

```
tccli wedata CreateApp --cli-unfold-argument  \
    --WorkspaceId 17678671667189298 \
    --AppName test3 \
    --Description sadf \
    --AppType AGENT \
    --Resources.0.ResourceType MLFlow \
    --Resources.0.ResourceKey mlkey \
    --Resources.0.ResourceValue mlvalue \
    --Resources.0.ResourceName mlname \
    --Resources.0.Permission edit
```

Output: 
```
{
    "Response": {
        "Data": {
            "Key": "e6b9382c177426510481606633469"
        },
        "RequestId": "8dd1cb06-bd60-4954-9287-cc3353247c1b"
    }
}
```

