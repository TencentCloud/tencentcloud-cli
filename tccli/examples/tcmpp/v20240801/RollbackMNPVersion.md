**Example 1: RollbackMNPVersion**



Input: 

```
tccli tcmpp RollbackMNPVersion --cli-unfold-argument  \
    --MNPId mp0sbz01tzh2du7n \
    --MNPVersionId 2625 \
    --MNPVersion 1.0.1 \
    --PlatformId T04257DS9431720WTAG
```

Output: 
```
{
    "Response": {
        "Data": {
            "Result": true
        },
        "RequestId": "29008657-86cf-4315-92a8-90095c9eca5d"
    }
}
```

