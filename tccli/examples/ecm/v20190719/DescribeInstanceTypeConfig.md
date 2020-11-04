**Example 1: 查看机型配置列表**

查看机型配置列表

Input: 

```
tccli ecm DescribeInstanceTypeConfig --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "9d0f0dc6-8fec-44fc-82f1-0553144a000b",
        "InstanceTypeConfigSet": [
            {
                "InstanceFamilyConfig": {
                    "InstanceFamilyName": "标准网络优化型",
                    "InstanceFamily": "SN3ne"
                },
                "InstanceFamilyTypeConfig": {
                    "InstanceFamilyType": "S",
                    "InstanceFamilyTypeName": "标准型"
                },
                "InstanceType": "SN3ne.2XLARGE16",
                "Vcpu": 8,
                "Memory": 16,
                "Frequency": "2.5 GHz",
                "CpuModelName": "Intel Xeon Skylake 6133",
                "ExtInfo": ""
            },
            {
                "InstanceFamilyConfig": {
                    "InstanceFamilyName": "标准网络优化型",
                    "InstanceFamily": "SN3ne"
                },
                "InstanceFamilyTypeConfig": {
                    "InstanceFamilyType": "S",
                    "InstanceFamilyTypeName": "标准型"
                },
                "InstanceType": "SN3ne.2XLARGE32",
                "Vcpu": 8,
                "Memory": 32,
                "Frequency": "2.5 GHz",
                "CpuModelName": "Intel Xeon Skylake 6133",
                "ExtInfo": ""
            },
            {
                "InstanceFamilyConfig": {
                    "InstanceFamilyName": "标准网络优化型",
                    "InstanceFamily": "SN3ne"
                },
                "InstanceFamilyTypeConfig": {
                    "InstanceFamilyType": "S",
                    "InstanceFamilyTypeName": "标准型"
                },
                "InstanceType": "SN3ne.2XLARGE64",
                "Vcpu": 8,
                "Memory": 64,
                "Frequency": "2.5 GHz",
                "CpuModelName": "Intel Xeon Skylake 6133",
                "ExtInfo": ""
            },
            {
                "InstanceFamilyConfig": {
                    "InstanceFamilyName": "标准网络优化型",
                    "InstanceFamily": "SN3ne"
                },
                "InstanceFamilyTypeConfig": {
                    "InstanceFamilyType": "S",
                    "InstanceFamilyTypeName": "标准型"
                },
                "InstanceType": "SN3ne.4XLARGE32",
                "Vcpu": 16,
                "Memory": 32,
                "Frequency": "2.5 GHz",
                "CpuModelName": "Intel Xeon Skylake 6133",
                "ExtInfo": ""
            },
            {
                "InstanceFamilyConfig": {
                    "InstanceFamilyName": "标准网络优化型",
                    "InstanceFamily": "SN3ne"
                },
                "InstanceFamilyTypeConfig": {
                    "InstanceFamilyType": "S",
                    "InstanceFamilyTypeName": "标准型"
                },
                "InstanceType": "SN3ne.4XLARGE64",
                "Vcpu": 16,
                "Memory": 64,
                "Frequency": "2.5 GHz",
                "CpuModelName": "Intel Xeon Skylake 6133",
                "ExtInfo": ""
            },
            {
                "InstanceFamilyConfig": {
                    "InstanceFamilyName": "标准网络优化型",
                    "InstanceFamily": "SN3ne"
                },
                "InstanceFamilyTypeConfig": {
                    "InstanceFamilyType": "S",
                    "InstanceFamilyTypeName": "标准型"
                },
                "InstanceType": "SN3ne.6XLARGE48",
                "Vcpu": 24,
                "Memory": 48,
                "Frequency": "2.5 GHz",
                "CpuModelName": "Intel Xeon Skylake 6133",
                "ExtInfo": ""
            },
            {
                "InstanceFamilyConfig": {
                    "InstanceFamilyName": "标准网络优化型",
                    "InstanceFamily": "SN3ne"
                },
                "InstanceFamilyTypeConfig": {
                    "InstanceFamilyType": "S",
                    "InstanceFamilyTypeName": "标准型"
                },
                "InstanceType": "SN3ne.6XLARGE64",
                "Vcpu": 24,
                "Memory": 64,
                "Frequency": "2.5 GHz",
                "CpuModelName": "Intel Xeon Skylake 6133",
                "ExtInfo": ""
            },
            {
                "InstanceFamilyConfig": {
                    "InstanceFamilyName": "标准网络优化型",
                    "InstanceFamily": "SN3ne"
                },
                "InstanceFamilyTypeConfig": {
                    "InstanceFamilyType": "S",
                    "InstanceFamilyTypeName": "标准型"
                },
                "InstanceType": "SN3ne.8XLARGE64",
                "Vcpu": 32,
                "Memory": 64,
                "Frequency": "2.5 GHz",
                "CpuModelName": "Intel Xeon Skylake 6133",
                "ExtInfo": ""
            },
            {
                "InstanceFamilyConfig": {
                    "InstanceFamilyName": "标准网络优化型",
                    "InstanceFamily": "SN3ne"
                },
                "InstanceFamilyTypeConfig": {
                    "InstanceFamilyType": "S",
                    "InstanceFamilyTypeName": "标准型"
                },
                "InstanceType": "SN3ne.LARGE16",
                "Vcpu": 4,
                "Memory": 16,
                "Frequency": "2.5 GHz",
                "CpuModelName": "Intel Xeon Skylake 6133",
                "ExtInfo": ""
            },
            {
                "InstanceFamilyConfig": {
                    "InstanceFamilyName": "标准网络优化型",
                    "InstanceFamily": "SN3ne"
                },
                "InstanceFamilyTypeConfig": {
                    "InstanceFamilyType": "S",
                    "InstanceFamilyTypeName": "标准型"
                },
                "InstanceType": "SN3ne.LARGE32",
                "Vcpu": 4,
                "Memory": 32,
                "Frequency": "2.5 GHz",
                "CpuModelName": "Intel Xeon Skylake 6133",
                "ExtInfo": ""
            },
            {
                "InstanceFamilyConfig": {
                    "InstanceFamilyName": "标准网络优化型",
                    "InstanceFamily": "SN3ne"
                },
                "InstanceFamilyTypeConfig": {
                    "InstanceFamilyType": "S",
                    "InstanceFamilyTypeName": "标准型"
                },
                "InstanceType": "SN3ne.LARGE8",
                "Vcpu": 4,
                "Memory": 8,
                "Frequency": "2.5 GHz",
                "CpuModelName": "Intel Xeon Skylake 6133",
                "ExtInfo": ""
            },
            {
                "InstanceFamilyConfig": {
                    "InstanceFamilyName": "标准网络优化型",
                    "InstanceFamily": "SN3ne"
                },
                "InstanceFamilyTypeConfig": {
                    "InstanceFamilyType": "S",
                    "InstanceFamilyTypeName": "标准型"
                },
                "InstanceType": "SN3ne.MEDIUM16",
                "Vcpu": 2,
                "Memory": 16,
                "Frequency": "2.5 GHz",
                "CpuModelName": "Intel Xeon Skylake 6133",
                "ExtInfo": ""
            },
            {
                "InstanceFamilyConfig": {
                    "InstanceFamilyName": "标准网络优化型",
                    "InstanceFamily": "SN3ne"
                },
                "InstanceFamilyTypeConfig": {
                    "InstanceFamilyType": "S",
                    "InstanceFamilyTypeName": "标准型"
                },
                "InstanceType": "SN3ne.MEDIUM4",
                "Vcpu": 2,
                "Memory": 4,
                "Frequency": "2.5 GHz",
                "CpuModelName": "Intel Xeon Skylake 6133",
                "ExtInfo": ""
            },
            {
                "InstanceFamilyConfig": {
                    "InstanceFamilyName": "标准网络优化型",
                    "InstanceFamily": "SN3ne"
                },
                "InstanceFamilyTypeConfig": {
                    "InstanceFamilyType": "S",
                    "InstanceFamilyTypeName": "标准型"
                },
                "InstanceType": "SN3ne.MEDIUM8",
                "Vcpu": 2,
                "Memory": 8,
                "Frequency": "2.5 GHz",
                "CpuModelName": "Intel Xeon Skylake 6133",
                "ExtInfo": ""
            },
            {
                "InstanceFamilyConfig": {
                    "InstanceFamilyName": "标准网络优化型",
                    "InstanceFamily": "SN3ne"
                },
                "InstanceFamilyTypeConfig": {
                    "InstanceFamilyType": "S",
                    "InstanceFamilyTypeName": "标准型"
                },
                "InstanceType": "SN3ne.SMALL2",
                "Vcpu": 1,
                "Memory": 2,
                "Frequency": "2.5 GHz",
                "CpuModelName": "Intel Xeon Skylake 6133",
                "ExtInfo": ""
            },
            {
                "InstanceFamilyConfig": {
                    "InstanceFamilyName": "标准网络优化型",
                    "InstanceFamily": "SN3ne"
                },
                "InstanceFamilyTypeConfig": {
                    "InstanceFamilyType": "S",
                    "InstanceFamilyTypeName": "标准型"
                },
                "InstanceType": "SN3ne.SMALL4",
                "Vcpu": 1,
                "Memory": 4,
                "Frequency": "2.5 GHz",
                "CpuModelName": "Intel Xeon Skylake 6133",
                "ExtInfo": ""
            },
            {
                "InstanceFamilyConfig": {
                    "InstanceFamilyName": "标准网络优化型",
                    "InstanceFamily": "SN3ne"
                },
                "InstanceFamilyTypeConfig": {
                    "InstanceFamilyType": "S",
                    "InstanceFamilyTypeName": "标准型"
                },
                "InstanceType": "SN3ne.SMALL8",
                "Vcpu": 1,
                "Memory": 8,
                "Frequency": "2.5 GHz",
                "CpuModelName": "Intel Xeon Skylake 6133",
                "ExtInfo": ""
            }
        ],
        "TotalCount": 17
    }
}
```

