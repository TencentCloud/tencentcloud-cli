**Example 1: 查询云原生实例列表**



Input: 

```
tccli cdwpg DescribeInstances --cli-unfold-argument  \
    --Offset 0 \
    --Limit 0 \
    --SearchTags.0.AllValue 0 \
    --SearchTags.0.TagKey test \
    --SearchTags.0.TagValue test \
    --SearchInstanceId test \
    --SearchInstanceName test
```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "InstancesList": [
            {
                "Status": "xx",
                "InstanceID": "xx",
                "InstanceType": "xx",
                "InstanceStateInfo": {
                    "FlowName": "xx",
                    "FlowMsg": "xx",
                    "FlowProgress": 0,
                    "ProcessName": "xx",
                    "InstanceState": "xx",
                    "FlowCreateTime": "xx",
                    "InstanceStateDesc": "xx"
                },
                "StatusDesc": "xx",
                "InstanceName": "xx",
                "ID": 0
            }
        ],
        "RequestId": "xx",
        "ErrorMsg": "xx"
    }
}
```

