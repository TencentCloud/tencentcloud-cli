**Example 1: 网络攻击日志列表**

网络攻击日志列表

Input: 

```
tccli cwp DescribeAttackLogs --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "AttackLogs": [
            {
                "Id": 1,
                "Uuid": "abc",
                "SrcIp": "abc",
                "SrcPort": 1,
                "HttpMethod": "abc",
                "HttpCgi": "abc",
                "HttpParam": "abc",
                "VulType": "abc",
                "CreatedAt": "abc",
                "MachineIp": "abc",
                "MachineName": "abc",
                "DstIp": "abc",
                "DstPort": 1,
                "HttpContent": "abc",
                "MachineExtraInfo": {
                    "WanIP": "abc",
                    "PrivateIP": "abc",
                    "NetworkType": 0,
                    "NetworkName": "abc",
                    "InstanceID": "abc",
                    "HostName": "abc"
                }
            }
        ],
        "TotalCount": 1,
        "RequestId": "abc"
    }
}
```

