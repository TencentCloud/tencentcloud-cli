**Example 1: 修改终端接节点组**



Input: 

```
tccli ga2 ModifyEndpointGroup --cli-unfold-argument  \
    --GlobalAcceleratorId ga-lb2dx0f4 \
    --ListenerId lsr-7sadofix \
    --EndpointGroupId epg-poo6fkq2 \
    --Name moify
```

Output: 
```
{
    "Response": {
        "RequestId": "82c22f64-a8e3-4958-9655-e5a425e1e046",
        "TaskId": "0668dba1-f4fa-4edc-84c5-f8bf91ba7b5f"
    }
}
```

