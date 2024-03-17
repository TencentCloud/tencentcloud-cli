**Example 1: 查询服务下契约版本列表**

查询服务下契约版本列表

Input: 

```
tccli tse DescribeGovernanceServiceContractVersions --cli-unfold-argument  \
    --InstanceId abc \
    --Namespace abc \
    --Service abc
```

Output: 
```
{
    "Response": {
        "GovernanceServiceContractVersions": [
            {
                "Version": "abc",
                "Name": "abc",
                "Key": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

