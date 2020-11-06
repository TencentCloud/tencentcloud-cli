**Example 1: 查询参数修改历史列表**



Input: 

```
tccli redis DescribeInstanceParamRecords --cli-unfold-argument  \
    --InstanceId crs-5a4py64p
```

Output: 
```
{
    "Response": {
        "InstanceParamHistory": [
            {
                "ModifyTime": "2019-01-07 11:28:58",
                "NewValue": "511",
                "ParamName": "hash-max-ziplist-entries",
                "PreValue": "512",
                "Status": 2
            },
            {
                "ModifyTime": "2019-01-07 11:28:48",
                "NewValue": "15001",
                "ParamName": "cluster-node-timeout",
                "PreValue": "15000",
                "Status": 2
            }
        ],
        "RequestId": "e546784b-709c-401d-aba6-73037eb4e522",
        "TotalCount": 2
    }
}
```

