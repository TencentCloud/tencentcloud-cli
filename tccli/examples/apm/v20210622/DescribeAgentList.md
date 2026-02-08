**Example 1: 请求示例**

请求实例

Input: 

```
tccli apm DescribeAgentList --cli-unfold-argument  \
    --ServiceName java-order-service \
    --InstanceId apm-6xYKFXYxo
```

Output: 
```
{
    "Response": {
        "Agents": [
            {
                "Enable": false,
                "IP": "9.126.244.1",
                "RunningTime": 1211,
                "StartTime": 1689661909,
                "Status": 1,
                "Version": "v1.1.1"
            },
            {
                "Enable": false,
                "IP": "10.126.244.1",
                "RunningTime": 10000,
                "StartTime": 1689651909,
                "Status": 0,
                "Version": "v1.2.1"
            }
        ],
        "RequestId": "8fd3468e-a737-4058-84be-e14ada3a25a9"
    }
}
```

