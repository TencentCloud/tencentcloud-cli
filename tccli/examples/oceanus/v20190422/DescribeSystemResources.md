**Example 1: 查询系统资源配置列表示例**



Input: 

```
tccli oceanus DescribeSystemResources --cli-unfold-argument  \
    --ClusterId cluster-n8yaia0p
```

Output: 
```
{
    "Response": {
        "RequestId": "09250e9b-d3a1-4d37-b44f-de10e06ed52d",
        "ResourceSet": [
            {
                "ResourceId": "resource-abd503yt",
                "Name": "testjar",
                "ResourceType": 1,
                "Remark": "",
                "Region": "ap-guangzhou",
                "LatestResourceConfigVersion": 1
            }
        ],
        "TotalCount": 1
    }
}
```

