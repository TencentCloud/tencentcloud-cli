**Example 1: 1**



Input: 

```
tccli tke DescribeHealthCheckPolicyBindings --cli-unfold-argument  \
    --ClusterId cls-xxx \
    --Limit 1 \
    --Offset 2
```

Output: 
```
{
    "RequestId": "xx",
    "Response": {
        "HealthCheckPolicyBindings": [
            {
                "CreatedAt": "xx",
                "NodePools": [
                    "node-pool1",
                    "node-pool2"
                ],
                "Name": "NP1"
            }
        ],
        "RequestId": "372ba519-daa2-4abc-9da7-0857970c998c",
        "TotalCount": 1
    }
}
```

**Example 2: 查询健康检测策略绑定关系**



Input: 

```
tccli tke DescribeHealthCheckPolicyBindings --cli-unfold-argument  \
    --Limit 0 \
    --ClusterId xx \
    --Filter.0.Values xx \
    --Filter.0.Name xx \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "HealthCheckPolicyBindings": [
            {
                "NodePools": [
                    "xx"
                ],
                "Name": "xx",
                "CreatedAt": "xx"
            }
        ],
        "RequestId": "xx"
    }
}
```

