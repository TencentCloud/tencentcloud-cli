**Example 1: 删除终端节点组**



Input: 

```
tccli ga2 DeleteEndpointGroups --cli-unfold-argument  \
    --GlobalAcceleratorId ga-80bzejka \
    --ListenerId lsr-kzjzfs7n \
    --EndpointGroupIds epg-5lkfesga
```

Output: 
```
{
    "Response": {
        "RequestId": "f536f297-f2a9-466f-b54d-2ab56285e4c7",
        "TaskId": "bbf56063-b48e-4caa-a721-11139fb63344"
    }
}
```

