**Example 1: 查询监听者列表**

查询监听者列表

Input: 

```
tccli wedata DescribeDsEventListenerList --cli-unfold-argument  \
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
                "EventName": "abc"
            }
        ],
        "RequestId": "abc"
    }
}
```

