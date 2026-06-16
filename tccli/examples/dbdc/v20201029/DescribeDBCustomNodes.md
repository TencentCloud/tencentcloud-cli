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

