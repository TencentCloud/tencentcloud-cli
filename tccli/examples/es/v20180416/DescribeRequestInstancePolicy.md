**Example 1: 集群可访问API展示**



Input: 

```
tccli es DescribeRequestInstancePolicy --cli-unfold-argument  \
    --InstanceId ts-57zavbdv
```

Output: 
```
{
    "Response": {
        "GetPaths": [
            "_cat/.*"
        ],
        "IsDefault": false,
        "Operator": "************",
        "PostPaths": [
            "/.*/_open"
        ],
        "PutPaths": [
            "/.*/_settings"
        ],
        "UpdateTime": "2026-06-04 15:37:49",
        "RequestId": "f556db11-af0f-48df-9ada-b61569421411"
    }
}
```

