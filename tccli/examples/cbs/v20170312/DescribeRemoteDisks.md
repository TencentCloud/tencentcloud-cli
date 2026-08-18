**Example 1: 按条件查询单副本SSD硬盘列表**

按状态过滤查询单副本SSD硬盘。

Input: 

```
tccli cbs DescribeRemoteDisks --cli-unfold-argument  \
    --Filters.0.Name remote-disk-state \
    --Filters.0.Values ATTACHED
```

Output: 
```
{
    "Response": {
        "RemoteDiskSet": [
            {
                "Placement": {
                    "CageId": "",
                    "CdcId": "",
                    "CdcName": "",
                    "DedicatedClusterId": "",
                    "ProjectId": 0,
                    "ProjectName": "",
                    "Zone": "ap-guangzhou-2"
                }
            }
        ],
        "TotalCount": 2,
        "RequestId": "55e81553-b057-4a64-8e63-590d84aa2d7f"
    }
}
```

**Example 2: 查询单副本SSD硬盘列表**



Input: 

```
tccli cbs DescribeRemoteDisks --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RemoteDiskSet": [
            {
                "Placement": {
                    "CageId": "",
                    "CdcId": "",
                    "CdcName": "",
                    "DedicatedClusterId": "",
                    "ProjectId": 0,
                    "ProjectName": "",
                    "Zone": "ap-guangzhou-2"
                }
            }
        ],
        "TotalCount": 1,
        "RequestId": "b15edc0e-549d-4160-8796-78881ea55d48"
    }
}
```

