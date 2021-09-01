**Example 1: 获取内网接入信息的列表**



Input: 

```
tccli tcr DescribeInternalEndpoints --cli-unfold-argument  \
    --RegistryId tcr-xxxx
```

Output: 
```
{
    "Response": {
        "AccessVpcSet": [],
        "TotalCount": 0,
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

