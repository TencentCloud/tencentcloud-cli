**Example 1: 查询项目参数历史版本**

查询项目参数历史版本


Input: 

```
tccli wedata DescribeProjectParamVersionDs --cli-unfold-argument  \
    --ProjectId abc
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "Id": 0,
                "Version": 0,
                "Name": "abc",
                "ParamBelong": "abc",
                "Description": "abc",
                "Creator": "abc",
                "CreatorId": "abc",
                "CreateTime": "abc",
                "UpdateTime": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

