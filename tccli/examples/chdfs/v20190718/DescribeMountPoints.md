**Example 1: 查看挂载点列表**

查看挂载点列表

Input: 

```
tccli chdfs DescribeMountPoints --cli-unfold-argument  \
    --AccessGroupId ag-fmfpk1hk
```

Output: 
```
{
    "Response": {
        "MountPoints": [
            {
                "MountPointId": "f4mnvilzmdd-Tx5f",
                "MountPointName": "test",
                "FileSystemId": "f4mnvilzmdd",
                "AccessGroupId": "ag-fmfpk1hk",
                "VpcId": "vpc-967aipkx",
                "VpcType": 1,
                "Status": 2,
                "CreateTime": "2019-07-30T18:19:18+08:00"
            },
            {
                "MountPointId": "f4mnvilzmdd-fj7A",
                "MountPointName": "test",
                "FileSystemId": "f4mnvilzmdd",
                "AccessGroupId": "ag-fmfpk1hk",
                "VpcId": "vpc-967aipkx",
                "VpcType": 1,
                "Status": 1,
                "CreateTime": "2019-07-30T18:14:45+08:00"
            },
            {
                "MountPointId": "f4mnvilzmdd-k2tC",
                "MountPointName": "test",
                "FileSystemId": "f4mnvilzmdd",
                "AccessGroupId": "ag-fmfpk1hk",
                "VpcId": "vpc-967aipkx",
                "VpcType": 1,
                "Status": 1,
                "CreateTime": "2019-07-30T18:15:53+08:00"
            }
        ],
        "RequestId": "ff98aad2-e290-4512-af5c-ab24993591e3"
    }
}
```

