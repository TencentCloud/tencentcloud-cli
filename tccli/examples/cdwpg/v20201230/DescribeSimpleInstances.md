**Example 1: 集群列表new**

集群列表

Input: 

```
tccli cdwpg DescribeSimpleInstances --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "ErrorMsg": "",
        "InstancesList": [
            {
                "AccessInfo": "[{\"address\":\"10.0.16.19:9000\",\"protocol\":\"tcp\"}]",
                "CreateTime": "2025-03-19 16:37:38",
                "ExpireTime": "0000.00.00 00:00:00",
                "Region": "ap-beijing",
                "RegionId": 8,
                "RegionDesc": "ap-beijing",
                "Zone": "ap-beijing-6",
                "ZoneId": 800005,
                "ZoneDesc": "ap-beijing-6",
                "ID": 1094,
                "InstanceId": "cdwpg-rzshdeh1",
                "InstanceName": "hugogao_test",
                "PayMode": "POSTPAID_BY_HOUR",
                "RenewFlag": false,
                "SubnetId": "subnet-rdlodajk",
                "Version": "3.16.9.4",
                "VpcId": "vpc-1asw4o73"
            },
            {
                "AccessInfo": "[{\"address\":\"10.0.16.27:9000\",\"protocol\":\"tcp\"}]",
                "CreateTime": "2025-02-20 11:37:11",
                "ExpireTime": "0000.00.00 00:00:00",
                "ID": 1089,
                "InstanceId": "cdwpg-9jcyk7yp",
                "InstanceName": "demo_tim",
                "Region": "ap-beijing",
                "RegionId": 8,
                "RegionDesc": "ap-beijing",
                "Zone": "ap-beijing-6",
                "ZoneId": 800005,
                "ZoneDesc": "ap-beijing-6",
                "PayMode": "POSTPAID_BY_HOUR",
                "RenewFlag": false,
                "SubnetId": "subnet-rdlodajk",
                "Version": "3.16.9.4",
                "VpcId": "vpc-1asw4o73"
            }
        ],
        "RequestId": "ad9e5842-e932-47d1-83a0-a388ccc5c19e",
        "TotalCount": 2
    }
}
```

