**Example 1: 查询事件监听者**

查询事件监听者

Input: 

```
tccli wedata DescribeDsEventListener --cli-unfold-argument  \
    --Key abc \
    --ProjectId abc
```

Output: 
```
{
    "Response": {
        "Data": {
            "Key": "abc",
            "Type": "abc",
            "EventProjectId": "123",
            "CreationTs": "abc",
            "PropertiesList": [
                {
                    "ParamKey": "abc",
                    "ParamValue": "abc"
                }
            ],
            "EventName": "abc"
        },
        "RequestId": "abc"
    }
}
```

