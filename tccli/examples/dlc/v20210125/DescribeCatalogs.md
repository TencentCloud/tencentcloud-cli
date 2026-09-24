**Example 1: 示例1**



Input: 

```
tccli dlc DescribeCatalogs --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Catalogs": [
            {
                "Audit": {
                    "CreatedAt": 1788268042334,
                    "CreatedTime": "",
                    "Creator": "700002744585",
                    "LastModifiedAt": 1788511393388,
                    "LastModifiedTime": "",
                    "LastModifier": "700002744585"
                },
                "Comment": "test_1",
                "Connection": {
                    "LakeHouseConnection": {
                        "Location": "cosn://tcs-a54320701c-1785327710-251438733/260209337/warehouse/chenfan_test_1/"
                    }
                },
                "CreateTime": "2026-09-01 21:07:22",
                "Id": "be32d91c-9ea3-4397-982e-fc9578142942",
                "Message": "Create Catalog Connection Success",
                "Name": "chenfan_test_1",
                "Operator": "700002744585",
                "Properties": [
                    {
                        "Key": "tclake.cos.credentials.server.url",
                        "Value": "http://21.215.50.237:2030/v1/internal/GetTcLakeFsToken"
                    }
                ],
                "Status": 2,
                "Type": "LAKEHOUSE",
                "UpdateTime": "2026-09-04 16:43:13"
            }
        ],
        "Total": 5,
        "RequestId": "a4aafbf9-b18c-44bf-a840-6e6bd4cd9029"
    }
}
```

