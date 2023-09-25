**Example 1: 查询资产管理启动服务列表**

查询资产管理启动服务列表

Input: 

```
tccli cwp DescribeAssetInitServiceList --cli-unfold-argument  \
    --Uuid 01fa34d3-db26-48ab-9f14-e8d3a48be951 \
    --Limit 1 \
    --Quuid 01fa34d3-db26-48ab-9f14-e8d3a48be951 \
    --Filters.0.Values 1 \
    --Filters.0.Name IsAutoRun \
    --Filters.0.ExactMatch True \
    --Offset 1
```

Output: 
```
{
    "Response": {
        "RequestId": "b7b8a9cd-2470-4ea2-87fb-dd6fea05c32a",
        "Services": [
            {
                "Quuid": "01fa34d3-db26-48ab-9f14-e8d3a48be95e",
                "Uuid": "01fa34d3-db26-48ab-9f14-e8d3a48be95e",
                "Name": "efslsaext.dll",
                "Type": 7,
                "Status": 1,
                "User": "",
                "Path": "C:\\Windows\\System32\\efslsaext.dll",
                "MachineIp": "172.16.0.1",
                "MachineWanIp": "43.138.242.17",
                "MachineName": "win-test",
                "OsInfo": "Windows Server 2016 数据中心版 64位中文版",
                "UpdateTime": "2023-09-20 10:40:21",
                "FirstTime": "2023-09-20 10:40:29",
                "IsAutoRun": 1,
                "IsNew": 1,
                "MachineExtraInfo": {
                    "WanIP": "43.138.242.17",
                    "PrivateIP": "172.16.0.1",
                    "NetworkType": 0,
                    "NetworkName": "",
                    "InstanceID": "ins-4b90g85x",
                    "HostName": ""
                }
            }
        ],
        "Total": 1
    }
}
```

