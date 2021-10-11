**Example 1: 管理内网接入**



Input: 

```
tccli tcr ManageInternalEndpoint --cli-unfold-argument  \
    --RegistryId tcr-xxx \
    --RegionName ap-beijing \
    --Operation Create \
    --VpcId xxx \
    --SubnetId xxx
```

Output: 
```
{
    "Response": {
        "RegistryId": "XXXX",
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

