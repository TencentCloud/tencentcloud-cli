**Example 1: 查询健康检测策略绑定关系**



Input: 

```
tccli tke DescribeHealthCheckPolicyBindings --cli-unfold-argument  \
    --ClusterId cls-4h43fuxj \
    --Limit 1 \
    --Offset 2
```

Output: 
```
{
    "RequestId": "9bd42c72-dd16-46bc-9d1e-b4020c59fab8",
    "Response": {
        "HealthCheckPolicyBindings": [
            {
                "CreatedAt": "2023-08-17 20:46:39",
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

