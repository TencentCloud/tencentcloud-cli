**Example 1: 查询安全组关联实例列表**



Input: 

```
tccli cfw DescribeAssociatedInstanceList --cli-unfold-argument  \
    --Area ap-guangzhou \
    --Limit 10 \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "InstanceId": "eni-4ymwnaoe",
                "InstanceName": "test-private",
                "Type": 5,
                "VpcId": "vpc-406waega",
                "VpcName": "vpc---",
                "PublicIp": "1.1.1.1",
                "Ip": "192.168.0.13,192.168.0.3",
                "CdbId": "cdb-0cc13ab",
                "SecurityGroupRuleCount": 1,
                "SecurityGroupCount": 1
            },
            {
                "InstanceId": "eni-oskydbvm",
                "InstanceName": "privat-test",
                "Type": 5,
                "VpcId": "vpc-dvc0qmmm",
                "VpcName": "Dno",
                "PublicIp": "1.1.1.1",
                "Ip": "172.21.0.12",
                "CdbId": "cdb-0cc13ab",
                "SecurityGroupRuleCount": 1,
                "SecurityGroupCount": 0
            }
        ],
        "Total": 2,
        "RequestId": "8f563b4d-8151-4db0-a822-9bde279d2079"
    }
}
```

