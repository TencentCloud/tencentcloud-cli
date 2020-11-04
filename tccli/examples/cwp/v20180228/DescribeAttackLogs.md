**Example 1: 网络攻击日志列表**

网络攻击日志列表

Input: 

```
tccli cwp DescribeAttackLogs --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "354f4ac3-8546-4516-8c8a-69e3ab73aa8a",
        "AttackLogs": [
            {
                "Id": 2012,
                "Uuid": "b250fe94-75c8-11e8-9a9d-40f2e9f55cda",
                "SrcIp": "117.20.113.126",
                "SrcPort": 54326,
                "HttpMethod": "POST",
                "HttpCgi": "/index.php",
                "HttpParam": "action=im.cts.sync&body_format=json&lang=1",
                "VulType": "fastjson",
                "CreatedAt": {
                    "date": "2019-07-16 15:43:38.000000",
                    "timezone_type": 3,
                    "timezone": "Asia/Shanghai"
                },
                "MachineIp": "172.21.0.8",
                "MachineName": "v_minjzhao"
            }
        ],
        "TotalCount": 0
    }
}
```

