**Example 1: 示例**

查询机器历史清理记录

Input: 

```
tccli cwp DescribeMachineClearHistory --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "962b0273-cc65-4d20-beac-7510a4dd4737",
        "TotalCount": 2,
        "List": [
            {
                "AgentLastOfflineTime": "2022-08-18 10:25:11",
                "CreateTime": "2022-12-06 18:31:59",
                "Id": 2,
                "InstanceId": "ins-df13****",
                "InstanceName": "new",
                "PrivateIp": "10.0.0.1",
                "PublicIp": "1.1.1.1"
            },
            {
                "AgentLastOfflineTime": "2022-08-29 16:08:03",
                "CreateTime": "2022-12-06 18:32:18",
                "Id": 3,
                "InstanceId": "ins-fmr1m***",
                "InstanceName": "vul-test-123",
                "PrivateIp": "10.0.0.2",
                "PublicIp": "1.1.1.1"
            }
        ]
    }
}
```

