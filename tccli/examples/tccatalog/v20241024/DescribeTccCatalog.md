**Example 1: 获取Tcc数据目录详情**

获取Tcc数据目录详情

Input: 

```
tccli tccatalog DescribeTccCatalog --cli-unfold-argument  \
    --CatalogId b8sd7dd7-ekd4-4e5e-993e-e5db64fa21c1
```

Output: 
```
{
    "Response": {
        "TccCatalog": {
            "Id": "b8sd7dd7-ekd4-4e5e-993e-e5db64fa21c1",
            "Name": "TccHiveCatalog",
            "Type": "TCC-HIVE",
            "Comment": "测试数据目录",
            "Status": 2,
            "Connection": {
                "TccHive": {
                    "EndpointServiceId": "vpcsvc-6jsieksl3",
                    "MetaStoreUrl": "thrift://127.0.0.1:9083",
                    "NetWork": {
                        "VpcId": "vpc-test",
                        "VpcCidrBlock": "10.0.0.1/12",
                        "SubnetId": "subnet-test",
                        "SubnetCidrBlock": "10.0.0.1/24"
                    }
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

