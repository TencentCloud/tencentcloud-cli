**Example 1: 指定云数据库实例的所属项目**

调整实例的所属项目

Input: 

```
tccli mongodb AssignProject --cli-unfold-argument  \
    --InstanceIds cmgo-eqmo**** \
    --ProjectId 12
```

Output: 
```
{
    "Response": {
        "FlowIds": [
            1081
        ],
        "RequestId": "8e2a339e-5ba9-4da3-8dc2-65a0a6314811"
    }
}
```

