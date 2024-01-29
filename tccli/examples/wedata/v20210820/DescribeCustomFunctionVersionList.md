**Example 1: 查询函数版本列表**



Input: 

```
tccli wedata DescribeCustomFunctionVersionList --cli-unfold-argument  \
    --ClusterIdentifier hive_emr-dbcygrxq \
    --FunctionId d21f43aa-96a8-40a6-92b1-59f09b36f640
```

Output: 
```
{
    "Response": {
        "ErrorMessage": "查询失败",
        "RequestId": "0d7fda9a-607d-4e0b-817e-b6d39dd18005",
        "Versions": [
            {
                "Comment": "函数版本1",
                "UserName": "test",
                "Timestamp": "20240101",
                "UserId": "5674342",
                "Content": "test",
                "Tag": "tag",
                "Type": "HIVE"
            }
        ]
    }
}
```

