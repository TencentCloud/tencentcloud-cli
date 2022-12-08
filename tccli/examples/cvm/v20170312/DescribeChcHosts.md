**Example 1: 查看CHC物理服务器实例**

根据CHC物理服务器ID查看实例

Input: 

```
tccli cvm DescribeChcHosts --cli-unfold-argument  \
    --ChcIds chc-1a2b3c4d
```

Output: 
```
{
    "Response": {
        "ChcHostSet": [
            {
                "ChcId": "chc-1a2b3c4d",
                "InstanceName": "托管服务器",
                "SerialNumber": "sn34asdfabd",
                "InstanceState": "RUNNING",
                "DeviceType": "CHC_HS1",
                "Placement": {
                    "Zone": "ap-guangzhou-2"
                },
                "BmcVirtualPrivateCloud": {
                    "SubnetId": "subnet-a2676p0e",
                    "VpcId": "vpc-g7wzcv7n"
                },
                "BmcIp": "10.12.10.34",
                "BmcSecurityGroupIds": [
                    "sg-1a2b3c4d"
                ],
                "DeployVirtualPrivateCloud": {
                    "SubnetId": "subnet-a26734fs",
                    "VpcId": "vpc-g7wz234f"
                },
                "DeployIp": "10.12.20.34",
                "DeploySecurityGroupIds": [
                    "sg-1a2b34af"
                ],
                "CvmInstanceId": "ins-1a2bafst",
                "CreatedTime": "2020-03-10T02:43:51Z",
                "HardwareDescription": "50C 128G 12*4T",
                "Memory": 128,
                "DeployMAC": "52:54:00:68:CC:00",
                "BmcMAC": "52:54:00:68:CC:01",
                "Disk": "12*4T",
                "CPU": 50
            }
        ],
        "TotalCount": 2,
        "RequestId": "62DDFFC6-FDB5-44F7-20A6-59152E3D129A"
    }
}
```

