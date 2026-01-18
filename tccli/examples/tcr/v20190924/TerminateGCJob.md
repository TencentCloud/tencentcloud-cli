**Example 1: 终止制品清理任务**



Input: 

```
tccli tcr TerminateGCJob --cli-unfold-argument  \
    --RegistryId tcr-dc0*****
```

Output: 
```
{
    "Response": {
        "Message": "GC job stopped successfully",
        "Status": "success",
        "RequestId": "304c05d3-c87b-489e-ad19-eee7251d4dc3"
    }
}
```

