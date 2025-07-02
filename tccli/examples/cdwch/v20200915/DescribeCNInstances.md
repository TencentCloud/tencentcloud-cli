**Example 1: 查询云原生实例列表**



Input: 

```
tccli cdwch DescribeCNInstances --cli-unfold-argument  \
    --Offset 0 \
    --Limit 0 \
    --SearchTags.0.AllValue 0 \
    --SearchTags.0.TagKey test \
    --SearchTags.0.TagValue test \
    --SearchInstanceID test \
    --SearchInstanceName test
```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "InstancesList": [
            {
                "ID": 0,
                "InstanceType": "abc",
                "InstanceName": "abc",
                "Status": "abc",
                "StatusDesc": "abc",
                "InstanceStateInfo": {
                    "InstanceState": "abc",
                    "FlowCreateTime": "abc",
                    "FlowName": "abc",
                    "FlowProgress": 0,
                    "InstanceStateDesc": "abc",
                    "FlowMsg": "abc",
                    "ProcessName": "abc",
                    "RequestId": "abc",
                    "ProcessSubName": "abc"
                },
                "InstanceID": "abc",
                "Resources": [
                    {
                        "ID": 0,
                        "InstanceID": "abc",
                        "AppID": 0,
                        "Uin": "abc",
                        "Component": "abc",
                        "DeployMode": 0,
                        "SpecName": "abc",
                        "ResourceID": "abc",
                        "Status": 0,
                        "IP": "abc",
                        "CPU": 1,
                        "Memory": 1,
                        "Storage": 1,
                        "UUID": "abc",
                        "Region": "abc",
                        "Zone": "abc",
                        "Details": "abc",
                        "CreateTime": "abc",
                        "ModifyTime": "abc",
                        "ExpireTime": "abc"
                    }
                ]
            }
        ],
        "ErrorMsg": "abc",
        "RequestId": "abc"
    }
}
```

