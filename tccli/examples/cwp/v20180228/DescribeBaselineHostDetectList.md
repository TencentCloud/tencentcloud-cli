**Example 1: 主机视角检测列表**



Input: 

```
tccli cwp DescribeBaselineHostDetectList --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "List": [
            {
                "HostId": "a0770b41-9697-4a1d-8150-b8fa247b6189",
                "HostIp": "172.23.16.10",
                "HostName": "功能测试ubuntu20漏洞修复v_txmitan",
                "WanIp": "10.104.9.1",
                "DetectStatus": 0,
                "PassedItemCount": 188,
                "NotPassedItemCount": 202,
                "ItemCount": 390,
                "FirstTime": "2022-05-11 17:11:32",
                "LastTime": "2022-08-23 14:28:51",
                "MachineExtraInfo": {
                    "WanIP": "146.56.21****",
                    "PrivateIP": "10.206****",
                    "NetworkType": 0,
                    "NetworkName": "vpc-3gov****",
                    "InstanceID": "ins-bask****",
                    "HostName": "demo_****"
                },
                "Uuid": "a0770b41-9697-4a1d-8150-b8fa247b6189"
            }
        ],
        "RequestId": "fca17381-b0fa-45c4-8568-82c186be9dc0",
        "Total": 36
    }
}
```

