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
                "Uuid": "a0770b41-9697-4a1d-8150-b8fa247b6189"
            },
            {
                "HostId": "36a78a1e-7711-4e7f-9fbe-c7afab78cd78",
                "HostIp": "10.255.0.36",
                "HostName": "jaryzhou-编码测试",
                "WanIp": "10.104.9.1",
                "DetectStatus": 0,
                "PassedItemCount": 183,
                "NotPassedItemCount": 203,
                "ItemCount": 386,
                "FirstTime": "2022-08-17 12:53:15",
                "LastTime": "2022-08-17 12:53:15",
                "Uuid": "36a78a1e-7711-4e7f-9fbe-c7afab78cd78"
            },
            {
                "HostId": "cc0e8a25-7169-4b5c-a929-2b4cccbfce10",
                "HostIp": "172.23.16.4",
                "HostName": "功能测试ubuntu18漏洞修复v_txmitan",
                "WanIp": "10.104.9.1",
                "DetectStatus": 0,
                "PassedItemCount": 186,
                "NotPassedItemCount": 183,
                "ItemCount": 369,
                "FirstTime": "2022-05-11 17:11:16",
                "LastTime": "2022-08-23 10:48:21",
                "Uuid": "cc0e8a25-7169-4b5c-a929-2b4cccbfce10"
            },
            {
                "HostId": "59b8dd86-333a-4b4a-872f-2162614e5e97",
                "HostIp": "172.23.16.7",
                "HostName": "功能测试ubuntu14漏洞修复v_txmitan",
                "WanIp": "10.104.9.1",
                "DetectStatus": 0,
                "PassedItemCount": 225,
                "NotPassedItemCount": 132,
                "ItemCount": 357,
                "FirstTime": "2022-05-11 17:08:46",
                "LastTime": "2022-08-22 17:01:23",
                "Uuid": "59b8dd86-333a-4b4a-872f-2162614e5e97"
            },
            {
                "HostId": "044889f8-d6a2-4fc3-a8a8-c114b6f5266b",
                "HostIp": "172.23.16.14",
                "HostName": "功能测试ubuntu16漏洞修复v_txmitan",
                "WanIp": "10.104.9.1",
                "DetectStatus": 0,
                "PassedItemCount": 226,
                "NotPassedItemCount": 131,
                "ItemCount": 357,
                "FirstTime": "2022-08-03 14:10:06",
                "LastTime": "2022-08-22 21:37:14",
                "Uuid": "044889f8-d6a2-4fc3-a8a8-c114b6f5266b"
            },
            {
                "HostId": "d8feb20e-dcdd-461b-9b37-336c42d48657",
                "HostIp": "172.16.0.49",
                "HostName": "功能测试软件较多_ivon",
                "WanIp": "10.104.9.1",
                "DetectStatus": 0,
                "PassedItemCount": 176,
                "NotPassedItemCount": 160,
                "ItemCount": 336,
                "FirstTime": "2022-08-03 14:09:26",
                "LastTime": "2022-08-23 10:48:32",
                "Uuid": "7168bc08-c1b8-11ea-9053-48fd8e5f474c"
            },
            {
                "HostId": "346f0497-894c-492f-9afb-ccef1fdb3adc",
                "HostIp": "172.16.0.40",
                "HostName": "cwp性能测试_ivon",
                "WanIp": "10.104.9.1",
                "DetectStatus": 0,
                "PassedItemCount": 178,
                "NotPassedItemCount": 157,
                "ItemCount": 335,
                "FirstTime": "2022-08-17 12:52:39",
                "LastTime": "2022-08-17 17:24:13",
                "Uuid": "346f0497-894c-492f-9afb-ccef1fdb3adc"
            },
            {
                "HostId": "8c09e1b1-5611-45b3-9c02-737996011b81",
                "HostIp": "172.27.16.8",
                "HostName": "cos挂载验证_ivon",
                "WanIp": "10.104.9.1",
                "DetectStatus": 0,
                "PassedItemCount": 177,
                "NotPassedItemCount": 158,
                "ItemCount": 335,
                "FirstTime": "2022-08-03 14:11:35",
                "LastTime": "2022-08-23 10:48:21",
                "Uuid": "8c09e1b1-5611-45b3-9c02-737996011b81"
            },
            {
                "HostId": "bce5ff2e-8c8d-4077-9acc-80ce542a6937",
                "HostIp": "172.16.16.10",
                "HostName": "v_vxuebai",
                "WanIp": "10.104.9.1",
                "DetectStatus": 0,
                "PassedItemCount": 178,
                "NotPassedItemCount": 157,
                "ItemCount": 335,
                "FirstTime": "2022-05-10 20:14:37",
                "LastTime": "2022-08-17 12:52:37",
                "Uuid": "bce5ff2e-8c8d-4077-9acc-80ce542a6937"
            },
            {
                "HostId": "ea6ce403-d165-4ed4-8362-958667c9ae37",
                "HostIp": "172.16.16.33",
                "HostName": "v_vxuebai-1",
                "WanIp": "10.104.9.1",
                "DetectStatus": 0,
                "PassedItemCount": 178,
                "NotPassedItemCount": 156,
                "ItemCount": 334,
                "FirstTime": "2022-06-21 15:36:02",
                "LastTime": "2022-08-17 12:51:20",
                "Uuid": "ea6ce403-d165-4ed4-8362-958667c9ae37"
            }
        ],
        "RequestId": "fca17381-b0fa-45c4-8568-82c186be9dc0",
        "Total": 36
    }
}
```

