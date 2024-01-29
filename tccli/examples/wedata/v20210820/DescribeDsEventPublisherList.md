**Example 1: 查询事件发布者列表**

查询事件发布者列表

Input: 

```
tccli wedata DescribeDsEventPublisherList --cli-unfold-argument  \
    --KeySet abc
```

Output: 
```
{
    "Response": {
        "Data": [
            {
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
            }
        ],
        "RequestId": "abc"
    }
}
```

