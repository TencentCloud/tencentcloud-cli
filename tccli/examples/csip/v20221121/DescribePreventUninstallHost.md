**Example 1: 获取卸载防护配置主机**

获取卸载防护配置主机

Input: 

```
tccli csip DescribePreventUninstallHost --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "List": [
            {
                "FunctionStatus": 1,
                "Id": 604721361,
                "InstanceId": "eks-gke2ehqw",
                "MachineExtraInfo": {
                    "HostName": "tke-np-5evz8w08-worker",
                    "InstanceID": "eks-gke2ehqw",
                    "NetworkName": "vpc-cwcsulhn",
                    "NetworkType": 1,
                    "PrivateIP": "172.17.1.183",
                    "WanIP": ""
                },
                "Message": "",
                "MessageDesc": "",
                "Name": "tke-np-5evz8w08-worker",
                "PrivateIp": "172.17.1.183",
                "PublicIp": "",
                "Quuid": "361b9679-7321-40ff-a520-7836112661ea",
                "RegionInfo": {
                    "Region": "ap-guangzhou",
                    "RegionCode": "gz",
                    "RegionId": 1,
                    "RegionName": "华南地区（广州）",
                    "RegionNameEn": "South China (Guangzhou)"
                },
                "Status": "OFFLINE",
                "VpcId": "vpc-cwcsulhn"
            },
            {
                "FunctionStatus": 1,
                "Id": 604721360,
                "InstanceId": "ins-hwi2xwnd",
                "MachineExtraInfo": {
                    "HostName": "tke_cls-mtdct307_worker",
                    "InstanceID": "ins-hwi2xwnd",
                    "NetworkName": "vpc-dwljk8d4",
                    "NetworkType": 1,
                    "PrivateIP": "10.255.255.189",
                    "WanIP": "43.136.185.218"
                },
                "Message": "",
                "MessageDesc": "",
                "Name": "tke_cls-mtdct307_worker",
                "PrivateIp": "10.255.255.189",
                "PublicIp": "43.136.185.218",
                "Quuid": "8a1b701c-1f7e-47bf-8e22-d5c3e5dcb1b1",
                "RegionInfo": {
                    "Region": "ap-chengdu",
                    "RegionCode": "cd",
                    "RegionId": 16,
                    "RegionName": "西南地区（成都）",
                    "RegionNameEn": "Southwestxa0China (Chengdu)"
                },
                "Status": "ONLINE",
                "VpcId": "vpc-dwljk8d4"
            }
        ],
        "RequestId": "17dbce4c-a9b3-473d-968a-bc82eaabfa73",
        "Total": 2
    }
}
```

