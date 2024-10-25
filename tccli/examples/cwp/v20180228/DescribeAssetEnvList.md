**Example 1: 查询资产管理环境变量列表**



Input: 

```
tccli cwp DescribeAssetEnvList --cli-unfold-argument  \
    --Uuid 1c26308c-5493-4eaf-a817-112ec25f499e \
    --Limit 1 \
    --Quuid 1c26308c-5493-4eaf-a817-112ec25f499e \
    --Offset 1 \
    --Type 1
```

Output: 
```
{
    "Response": {
        "Envs": [
            {
                "Quuid": "1c26308c-5493-4eaf-a817-112ec25f499e",
                "Uuid": "1c26308c-5493-4eaf-a817-112ec25f499e",
                "Name": "ID",
                "Type": 0,
                "User": "root",
                "Value": "/run/user/0",
                "MachineIp": "xx.xx.xx.xx",
                "MachineWanIp": "1xx.xx.xx.xx",
                "MachineName": "销售许可测试机器",
                "OsInfo": "CentOS 7.9 64位",
                "UpdateTime": "2024-10-21 23:53:11",
                "FirstTime": "2024-10-18 14:27:56",
                "IsNew": 0,
                "MachineExtraInfo": {
                    "WanIP": "xx.xx.xx.xx",
                    "PrivateIP": "xx.xx.xx.xx",
                    "NetworkType": 0,
                    "NetworkName": "",
                    "InstanceID": "ins-wssasw",
                    "HostName": ""
                }
            }
        ],
        "Total": 1,
        "RequestId": "1703764f-b3ea-4d7f-99cb-cc3a6a62e2ec"
    }
}
```

