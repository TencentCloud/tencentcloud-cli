**Example 1: 示例**

示例

Input: 

```
tccli dsgc DescribeBindDBList --cli-unfold-argument  \
    --DataSourceType abc \
    --DataSourceId abc \
    --DspaId abc
```

Output: 
```
{
    "Response": {
        "BindDBList": [
            "abc"
        ],
        "BindList": [
            {
                "ResourceId": "abc",
                "DbInfos": [
                    {
                        "DbName": "abc",
                        "ValidStatus": "abc"
                    }
                ]
            }
        ],
        "RequestId": "abc"
    }
}
```

