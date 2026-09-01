**Example 1: 查询与目标应用存在调用关联的上下游服务**

查询与目标应用存在调用关联的上下游服务

Input: 

```
tccli apm DescribeRelatedServicesOnTrace --cli-unfold-argument  \
    --InstanceId apm-6xYKFXYxo \
    --StartTime 1764101580 \
    --EndTime 1764144780 \
    --ServiceName service-A \
    --IsServiceTopology False
```

Output: 
```
{
    "Response": {
        "SelectedTraces": 0,
        "ServiceRelations": [
            {
                "DownstreamServices": [],
                "ServiceName": "service-A",
                "UpstreamServices": []
            }
        ],
        "TotalServices": 1,
        "TotalTraces": 0,
        "RequestId": "434b0ac9-870c-43a9-b83f-40d930d24e77"
    }
}
```

