**Example 1: 拉取项目参数版本详情**

拉取项目参数版本详情


Input: 

```
tccli wedata DescribeProjectParamVersionInfoDs --cli-unfold-argument  \
    --MyVersion 0 \
    --ProjectId abc
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "Id": 0,
                "ParamKey": "abc",
                "ParamType": "abc",
                "ParamBelong": "abc",
                "ParamDefine": "abc",
                "ParamValue": "abc",
                "ParamOwner": "abc",
                "CreateTime": "abc",
                "UpdateTime": "abc",
                "Result": true,
                "Msg": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

