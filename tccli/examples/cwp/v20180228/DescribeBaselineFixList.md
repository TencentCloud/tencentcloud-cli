**Example 1: 全部修复**

全部修复

Input: 

```
tccli cwp DescribeBaselineFixList --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "List": [
            {
                "MachineExtraInfo": {
                    "HostName": "demo-instance",
                    "InstanceID": "ins-1002",
                    "NetworkName": "vpc-1002",
                    "NetworkType": 1,
                    "PrivateIP": "1.1.1.1",
                    "WanIP": "1.1.1.1"
                },
                "Id": 334525,
                "ItemName": "Memcached UDP 端口可被利用为 DDOS 放大攻击",
                "HostIp": "172.16.64.15",
                "CreateTime": "2022-05-18 00:12:20",
                "ModifyTime": "2022-07-28 15:02:32",
                "FixTime": "2022-06-13 16:00:03"
            },
            {
                "MachineExtraInfo": {
                    "HostName": "demo-instance",
                    "InstanceID": "ins-1002",
                    "NetworkName": "vpc-1002",
                    "NetworkType": 1,
                    "PrivateIP": "1.1.1.1",
                    "WanIP": "1.1.1.1"
                },
                "Id": 335549,
                "ItemName": "确保在/tmp分区上设置nodev选项",
                "HostIp": "10.0.22.10",
                "CreateTime": "2022-05-26 16:14:51",
                "ModifyTime": "2022-07-28 15:02:32",
                "FixTime": "2022-06-15 17:02:55"
            }
        ],
        "RequestId": "8a667d00-bc48-4ab7-8725-cd6728e121ca",
        "Total": 1402
    }
}
```

