**Example 1: 展示用户当前地域下的可用资源组（包括公共资源组）**



Input: 

```
tccli tiems DescribeResourceGroups --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "0e21c605-3d85-4fc0-bc91-4c61ca250ad5",
        "ResourceGroups": [
            {
                "Region": "ap-beijing",
                "Cluster": "ap-beijing",
                "Id": "ap-beijing",
                "Name": "公共资源组",
                "Description": "公共资源组",
                "Created": "",
                "Updated": "",
                "InstanceCount": 0,
                "ServiceCount": 0,
                "JobCount": 0,
                "InstanceType": "sv_tiems_instance_4c20g1p4",
                "Gpu": 0,
                "Cpu": 0,
                "Memory": 0,
                "Status": "Ready",
                "Zone": "ap-beijing-4",
                "GpuType": [
                    "P4"
                ],
                "Public": true
            },
            {
                "Cluster": "ap-beijing",
                "Cpu": 336,
                "Created": "2019-10-22T22:32:38+08:00",
                "Description": "",
                "Gpu": 0,
                "GpuType": [],
                "Id": "kd8rgp2qpxf5h46f",
                "InstanceCount": 14,
                "InstanceType": "sv_tiems_instance_24c48g",
                "JobCount": 2,
                "Memory": 0,
                "Name": "rsg-kd8rgp2qpxf5h46f",
                "Public": false,
                "Region": "ap-beijing",
                "ServiceCount": 10,
                "Status": "Ready",
                "Updated": "2019-10-22T22:32:38+08:00",
                "Zone": "ap-beijing-2"
            }
        ],
        "TotalCount": 2
    }
}
```

**Example 2: 展示用户当前地域下的可用资源组（不包括公共资源组）**



Input: 

```
tccli tiems DescribeResourceGroups --cli-unfold-argument  \
    --Filters.0.Name public
```

Output: 
```
{
    "Response": {
        "RequestId": "0e21c605-3d85-4fc0-bc91-4c61ca250ad5",
        "ResourceGroups": [
            {
                "Cluster": "ap-beijing",
                "Cpu": 336,
                "Created": "2019-10-22T22:32:38+08:00",
                "Description": "",
                "Gpu": 0,
                "GpuType": [],
                "Id": "kd8rgp2qpxf5h46f",
                "InstanceCount": 14,
                "InstanceType": "sv_tiems_instance_24c48g",
                "JobCount": 2,
                "Memory": 0,
                "Name": "rsg-kd8rgp2qpxf5h46f",
                "Public": false,
                "Region": "ap-beijing",
                "ServiceCount": 10,
                "Status": "Ready",
                "Updated": "2019-10-22T22:32:38+08:00",
                "Zone": "ap-beijing-2"
            }
        ],
        "TotalCount": 1
    }
}
```

