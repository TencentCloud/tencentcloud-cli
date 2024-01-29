**Example 1: 查询事件发布者信息**

查询事件发布者信息

Input: 

```
tccli wedata DescribeDsEventPublisher --cli-unfold-argument  \
    --ProjectId abc \
    --Key abc
```

Output: 
```
{
    "Response": {
        "Data": {
            "Key": "abc",
            "Type": "abc",
            "CreationTs": "abc",
            "PropertiesList": [
                {
                    "ParamKey": "abc",
                    "ParamValue": "abc"
                }
            ],
            "Description": "abc"
        },
        "RequestId": "abc"
    }
}
```

