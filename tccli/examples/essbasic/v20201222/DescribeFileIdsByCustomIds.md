**Example 1: 根据用户自定义ID查询文件id**



Input: 

```
tccli essbasic DescribeFileIdsByCustomIds --cli-unfold-argument  \
    --Caller.ApplicationId c17bdf9c2a7bdcb32611f4d0200fee3d \
    --Caller.OperatorId a08c79b56afcd3b64317b33bee00ce12 \
    --CustomIds my-custom-id
```

Output: 
```
{
    "Response": {
        "CustomIdList": [
            {
                "CustomId": "my-custom-id",
                "FileId": "d54e3caec25ad0ea6be24406762b7562"
            }
        ],
        "RequestId": "s1609646162664722594"
    }
}
```

