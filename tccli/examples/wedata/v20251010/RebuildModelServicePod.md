**Example 1: 重建pod**



Input: 

```
tccli wedata RebuildModelServicePod --cli-unfold-argument  \
    --WorkspaceId 1464962169590902784 \
    --ServiceId 960ed2fc-f40e-4b34-b662-a3ed689e035b-1 \
    --PodName ms-6mvp5w9v-1-6d49b68644-j8jjs
```

Output: 
```
{
    "Response": {
        "Data": {
            "TiOneRebuildServiceRequestId": "c17f351e-dffe-43f3-970c-52c271c86559"
        },
        "RequestId": "70207a63-af4e-4a59-a05d-279825c46f6b"
    }
}
```

