**Example 1: 获取数据目录详情**



Input: 

```
tccli tccatalog DescribeCatalog --cli-unfold-argument  \
    --CatalogId b8sd7dd7-ekd4-4e5e-993e-e5db64fa21c1
```

Output: 
```
{
    "Response": {
        "Catalog": {
            "Id": "b8sd7dd7-ekd4-4e5e-993e-e5db64fa21c1",
            "Name": "HiveCatalog",
            "Type": "EMR-HIVE",
            "Comment": "Hive数据目录",
            "Status": 1,
            "Properties": [
                {
                    "Key": "url",
                    "Value": "http://1.0.0.1:10001"
                }
            ],
            "Connection": {
                "MysqlConnection": {
                    "InstanceId": "",
                    "InstanceName": "",
                    "JDBCUrl": "",
                    "User": "",
                    "Password": "",
                    "NetWork": {
                        "VpcId": "",
                        "VpcCidrBlock": "",
                        "SubnetId": "",
                        "SubnetCidrBlock": ""
                    }
                },
                "EmrHiveConnection": {
                    "InstanceId": "dsadhh-edsd-dsad-eew",
                    "InstanceName": "test-hive",
                    "MetaStoreUrl": "thrift://127.0.0.1:9083",
                    "NetWork": {
                        "VpcId": "vpc-test",
                        "VpcCidrBlock": "10.0.0.1/12",
                        "SubnetId": "subnet-test",
                        "SubnetCidrBlock": "10.0.0.1/24"
                    }
                },
                "DlcConnection": {
                    "InstanceId": "",
                    "InstanceName": ""
                },
                "VolumeConnection": {
                    "Location": ""
                },
                "TccHiveConnection": {
                    "EndpointServiceId": "",
                    "MetaStoreUrl": "",
                    "HiveVersion": "",
                    "Location": "",
                    "NetWork": {
                        "VpcId": "",
                        "VpcCidrBlock": "",
                        "SubnetId": "",
                        "SubnetCidrBlock": ""
                    }
                },
                "WeDataModelConnection": {
                    "ServerId": "",
                    "SyncInterval": "",
                    "TargetSchema": ""
                }
            },
            "Operator": "3783892123",
            "CreateTime": "2024-01-01 12:00:00",
            "UpdateTime": "2024-01-01 12:00:00"
        },
        "RequestId": "b8sd7dd7-ekd4-4e5e-993e-e5db64fa21c1"
    }
}
```

