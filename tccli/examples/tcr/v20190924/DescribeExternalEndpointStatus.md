**Example 1: 查询开启公网实例的状态**



Input: 

```
tccli tcr DescribeExternalEndpointStatus --cli-unfold-argument  \
    --RegistryId tcr-xxxx
```

Output: 
```
{
    "Response": {
        "Status": "Opened",
        "Reason": "",
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

