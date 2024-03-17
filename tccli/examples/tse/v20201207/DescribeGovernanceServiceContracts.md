**Example 1: 查询服务契约定义列表**

查询服务契约定义列表

Input: 

```
tccli tse DescribeGovernanceServiceContracts --cli-unfold-argument  \
    --InstanceId abc \
    --Namespace abc \
    --Service abc \
    --Name abc \
    --ContractVersion abc \
    --Protocol abc \
    --Brief True \
    --Offset 0 \
    --Limit 0
```

Output: 
```
{
    "Response": {
        "TotalCount": 0,
        "Size": 0,
        "ServiceContracts": [
            {
                "Name": "abc",
                "Namespace": "abc",
                "Protocol": "abc",
                "ID": "abc",
                "Service": "abc",
                "Version": "abc",
                "Revision": "abc",
                "Content": "abc",
                "CreateTime": "abc",
                "ModifyTime": "abc",
                "Interfaces": [
                    {
                        "ID": "abc",
                        "Method": "abc",
                        "Path": "abc",
                        "Content": "abc",
                        "Source": "abc",
                        "Revision": "abc",
                        "CreateTime": "abc",
                        "ModifyTime": "abc",
                        "Name": "abc"
                    }
                ]
            }
        ],
        "RequestId": "abc"
    }
}
```

