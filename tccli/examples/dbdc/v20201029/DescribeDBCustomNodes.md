**Example 1: 查询 DB Custom 节点列表**



Input: 

```
tccli dbdc DescribeDBCustomNodes --cli-unfold-argument  \
    --NodeIds dbcn-wamuy21e \
    --Filters.0.Name cluster-id \
    --Filters.0.Values dbcc-jnfqi1b9 \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "NodeSet": [
            {
                "AutoRenew": 2,
                "CPU": 4,
                "ChargeType": "PREPAID",
                "ClusterId": "dbcc-jnfqi1b9",
                "CreatedTime": "2026-06-01T14:14:40Z",
                "DataDisks": [
                    {
                        "DiskName": "ImageDisk",
                        "DiskSize": 10,
                        "DiskType": "CLOUD_HSSD"
                    }
                ],
                "ExpireTime": "2026-08-01T14:14:40Z",
                "HostIp": "7E87DEECE245155C880A7CF5355CD81F",
                "ImageId": "img-1tmhysjj",
                "IsolatedTime": "",
                "LanIP": "10.0.0.1",
                "Memory": 8,
                "NodeId": "dbcn-wamuy21e",
                "NodeName": "测试节点",
                "NodeType": "DB.AT5.8XLARGE128",
                "OsName": "TencentOS Server 3.2 with Driver",
                "RackId": "3E5BA837F9B5FFD91DCC02DBF501C7A7",
                "SSHEndpoint": "10.0.0.100:36000",
                "Status": "Running",
                "SubnetId": "subnet-clk8il4i",
                "SwitchId": "3E7A16039D8E141849DE7C837DE70ECC",
                "SystemDisk": {
                    "DiskSize": 100,
                    "DiskType": "CLOUD_BSSD"
                },
                "Tags": [
                    {
                        "Key": "test-key1",
                        "Value": "test-key1-value"
                    }
                ],
                "VpcId": "vpc-evvog2gd",
                "Zone": "ap-shanghai-5"
            }
        ],
        "TotalCount": 1,
        "RequestId": "e8841f33-dc54-4c5f-a1d4-b940bc09e1df"
    }
}
```

**Example 2: 查询 DB Custom 节点列表（按标签筛选）**



Input: 

```
tccli dbdc DescribeDBCustomNodes --cli-unfold-argument  \
    --Tags.0.Key 产品 \
    --Tags.0.Value DBCustom \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "NodeSet": [
            {
                "AutoRenew": 2,
                "CPU": 2,
                "ChargeType": "PREPAID",
                "ClusterId": "",
                "CreatedTime": "2026-06-05T12:52:38Z",
                "DataDisks": [
                    {
                        "DiskName": "ImageDisk",
                        "DiskSize": 200,
                        "DiskType": "CLOUD_HSSD"
                    }
                ],
                "ExpireTime": "2026-07-05T12:52:38Z",
                "HostIp": "7E9DD09DDF2FFB1FFA0E7430F1DF9085",
                "ImageId": "img-1tmhysjj",
                "IsolatedTime": "",
                "LanIP": "172.16.64.16",
                "Memory": 2,
                "NodeId": "dbcn-7avvxiri",
                "NodeName": "DBCustomPRE2",
                "NodeType": "DB.AT5.8XLARGE128",
                "OsName": "TencentOS Server 3.2 with Driver",
                "RackId": "9BD3E57A3DBE1201ACC65A0D06749DB8",
                "SSHEndpoint": "172.16.64.12:22",
                "Status": "Running",
                "SubnetId": "subnet-huka6qhj",
                "SwitchId": "1708E3E3DB05DE76DBEF337046C07BAE",
                "SystemDisk": {
                    "DiskSize": 100,
                    "DiskType": "CLOUD_HSSD"
                },
                "Tags": [
                    {
                        "Key": "产品",
                        "Value": "DBCustom"
                    }
                ],
                "VpcId": "vpc-cseo7req",
                "Zone": "ap-shanghai-5"
            }
        ],
        "TotalCount": 2,
        "RequestId": "60214b3e-4b60-432f-851e-150c0465ed04"
    }
}
```

**Example 3: 查询 DB Custom 节点列表(包含磁盘ID)**



Input: 

```
tccli dbdc DescribeDBCustomNodes --cli-unfold-argument  \
    --Limit 1
```

Output: 
```
{
    "Response": {
        "NodeSet": [
            {
                "AutoRenew": 1,
                "CPU": 32,
                "ChargeType": "PREPAID",
                "ClusterId": "",
                "CreatedTime": "2026-08-12T02:30:04Z",
                "DataDisks": [
                    {
                        "DiskId": "disk-m447xu3b",
                        "DiskName": "DataDisk",
                        "DiskSize": 200,
                        "DiskType": "CLOUD_HSSD"
                    }
                ],
                "DisasterRecoverGroupId": "",
                "EniIP": "",
                "ExpireTime": "2026-08-05T02:30:04Z",
                "HostIp": "",
                "ImageId": "img-1tmhysjj",
                "IsolatedTime": "2026-08-02T03:12:45Z",
                "LanIP": "10.0.0.1",
                "LatestRunningTaskType": "",
                "Memory": 128,
                "NetworkMode": "privatelink",
                "NodeId": "dbcn-a3ik6qc0",
                "NodeName": "dbcn-a3ik6qc0",
                "NodeType": "DB.SA5.2XLARGE32",
                "OsName": "TencentOS Server 3.2 with Driver",
                "RackId": "",
                "SSHEndpoint": "10.0.0.100:22",
                "SecurityGroupIds": [],
                "Status": "Running",
                "SubnetId": "subnet-qqgp4e31",
                "SwitchId": "",
                "SystemDisk": {
                    "DiskId": "disk-zj773km4",
                    "DiskSize": 100,
                    "DiskType": "CLOUD_HSSD"
                },
                "Tags": null,
                "VpcId": "vpc-alj2c14k",
                "Zone": "ap-shanghai-5"
            }
        ],
        "TotalCount": 1,
        "RequestId": "1a1c1cc4-a498-43a0-b02d-2af3c37df39c"
    }
}
```

