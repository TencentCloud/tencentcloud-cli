**Example 1: 查看权限信息示例**



Input: 

```
tccli trro DescribePolicy --cli-unfold-argument  \
    --ProjectId f3glr49rc96pralw
```

Output: 
```
{
    "Response": {
        "PolicyMode": "black",
        "PolicyInfo": [
            {
                "RemoteDeviceId": "test1",
                "FieldDeviceIds": [
                    "dev1",
                    "dev2"
                ],
                "ModifyTime": "2020-09-22T00:00:00+00:00"
            }
        ],
        "PolicyEnabled": true,
        "Num": 1,
        "RequestId": "8979fc1e-9564-4fc9-bf7d-2958ce679b72",
        "Total": 1
    }
}
```

