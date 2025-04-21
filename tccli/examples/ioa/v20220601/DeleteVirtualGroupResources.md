**Example 1: 取消自定义用户组的资源授权**

取消自定义用户组的资源授权

Input: 

```
tccli ioa DeleteVirtualGroupResources --cli-unfold-argument  \
    --ResourceList.0.ResourceType 2 \
    --ResourceList.0.ResourceId 3684 \
    --VirtualGroupId 18895
```

Output: 
```
{
    "Response": {
        "RequestId": "4947ee19-b2b8-4f94-9c85-27a50d90c997"
    }
}
```

