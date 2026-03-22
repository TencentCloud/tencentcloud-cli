**Example 1: CreateInferServiceByTemplate**



Input: 

```
tccli hai CreateInferServiceByTemplate --cli-unfold-argument  \
    --TemplateId tpl-ydcs88qr \
    --ServiceName hai-infer \
    --Replicas 1
```

Output: 
```
{
    "Response": {
        "ServiceId": "svc-bhbxouv0",
        "RequestId": "3cb9720e-c96c-47fc-be47-6463197641c2"
    }
}
```

