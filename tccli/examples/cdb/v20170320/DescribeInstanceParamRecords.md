**Example 1: 查询实例参数修改历史**



Input: 

```
tccli cdb DescribeInstanceParamRecords --cli-unfold-argument  \
    --InstanceId cdb-f35wr6wj
```

Output: 
```
{
    "Response": {
        "RequestId": "1a42feb9-82087f71-6a0031ac-699a92a8",
        "TotalCount": "28",
        "Items": [
            {
                "InstanceId": "cdb-1234asdf",
                "ParamName": "lower_case_table_names",
                "OldValue": "0",
                "NewValue": "1",
                "IsSucess": true,
                "ModifyTime": "2019-01-15 18:59:40"
            }
        ]
    }
}
```

