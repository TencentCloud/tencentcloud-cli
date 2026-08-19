**Example 1: 查询进程守护配置**

查询进程守护配置

Input: 

```
tccli csip DescribeProcessDaemonHost --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "List": [],
        "RequestId": "c4d289f9-cfe6-45e7-b6f7-901a83a0da68",
        "Total": 0
    }
}
```

**Example 2: 进程守护配置情况查询**

进程守护配置情况查询

Input: 

```
tccli csip DescribeProcessDaemonHost --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "List": [
            {
                "FunctionStatus": 1,
                "Id": 608341582,
                "InstanceId": "ins-1bynwtd6",
                "InstanceStatus": "RUNNING",
                "MachineExtraInfo": {
                    "HostName": "tenoyu-win2025-test",
                    "InstanceID": "ins-1bynwtd6",
                    "NetworkName": "vpc-cwcsulhn",
                    "NetworkType": 1,
                    "PrivateIP": "172.17.17.9",
                    "WanIP": "123.207.16.139"
                },
                "Message": "NEED_UPGRADE",
                "MessageDesc": "需要升级主机安全Agent。",
                "Name": "tenoyu-win2025-test",
                "PrivateIp": "172.17.17.9",
                "PublicIp": "123.207.16.139",
                "Quuid": "d77ca669-e14c-4165-9b53-eb8f42f03609",
                "RegionInfo": {
                    "Region": "ap-guangzhou",
                    "RegionCode": "gz",
                    "RegionId": 1,
                    "RegionName": "华南地区（广州）",
                    "RegionNameEn": "South China (Guangzhou)"
                },
                "Status": "ONLINE",
                "VpcId": "vpc-cwcsulhn"
            }
        ],
        "RequestId": "3bcc8a98-9635-4ea9-9171-4715001a7b15",
        "Total": 1
    }
}
```

