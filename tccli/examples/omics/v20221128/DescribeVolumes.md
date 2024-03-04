**Example 1: 查询缓存卷列表**

查询缓存卷列表。

Input: 

```
tccli omics DescribeVolumes --cli-unfold-argument  \
    --EnvironmentId menv-ry46eloh
```

Output: 
```
{
    "Response": {
        "RequestId": "f5020059-1511-4f45-ab7e-5188a78bda4b",
        "TotalCount": 1,
        "Volumes": [
            {
                "BandwidthLimit": 380,
                "Capacity": 32768,
                "DefaultMountPath": "/vol-8w7rfq4b",
                "Description": "",
                "EnvironmentId": "menv-ry46eloh",
                "IsDefault": true,
                "Name": "默认缓存卷（menv-ry46eloh）",
                "Spec": "HP",
                "Status": "AVAILABLE",
                "Type": "SHARED",
                "Usage": 973150879744,
                "VolumeId": "vol-8w7rfq4b"
            }
        ]
    }
}
```

