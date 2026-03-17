**Example 1: 获取扫码登录配置机器列表**

获取扫码登录配置机器列表

Input: 

```
tccli cwp DescribeLoginTypeHost --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "List": [
            {
                "FunctionStatus": 0,
                "Id": 534012791,
                "InstanceId": "lhins-lu9oiylm",
                "MachineExtraInfo": {
                    "HostName": "遵龙-开发测试用",
                    "InstanceID": "lhins-lu9oiylm",
                    "NetworkName": "",
                    "NetworkType": 2,
                    "PrivateIP": "10.2.20.2",
                    "WanIP": "82.156.42.223"
                },
                "Message": "",
                "MessageDesc": "",
                "Name": "遵龙-开发测试用",
                "PrivateIp": "10.2.20.2",
                "PublicIp": "82.156.42.223",
                "Quuid": "15c76928-e4e1-4f0d-8a2a-46c7de784744",
                "RegionInfo": {
                    "Region": "ap-beijing",
                    "RegionCode": "bj",
                    "RegionId": 8,
                    "RegionName": "华北地区 (北京)",
                    "RegionNameEn": "North China (Beijing)"
                },
                "Status": "ONLINE",
                "VpcId": ""
            },
            {
                "FunctionStatus": 0,
                "Id": 526087804,
                "InstanceId": "lhins-fp92s9zi",
                "MachineExtraInfo": {
                    "HostName": "jimmy-lh",
                    "InstanceID": "lhins-fp92s9zi",
                    "NetworkName": "",
                    "NetworkType": 2,
                    "PrivateIP": "10.2.24.2",
                    "WanIP": "81.70.142.244"
                },
                "Message": "",
                "MessageDesc": "",
                "Name": "jimmy-lh",
                "PrivateIp": "10.2.24.2",
                "PublicIp": "81.70.142.244",
                "Quuid": "d93eadd3-885b-4c2c-b223-65149d913cba",
                "RegionInfo": {
                    "Region": "ap-beijing",
                    "RegionCode": "bj",
                    "RegionId": 8,
                    "RegionName": "华北地区 (北京)",
                    "RegionNameEn": "North China (Beijing)"
                },
                "Status": "ONLINE",
                "VpcId": ""
            }
        ],
        "RequestId": "5b0a0e47-db60-40e9-8c58-170e4672e9b9",
        "Total": 2
    }
}
```

