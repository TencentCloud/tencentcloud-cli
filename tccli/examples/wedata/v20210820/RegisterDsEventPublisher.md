**Example 1: 注册事件发布者**

注册事件发布者

Input: 

```
tccli wedata RegisterDsEventPublisher --cli-unfold-argument  \
    --ProjectId abc \
    --Key abc \
    --Type abc \
    --Properties.0.ParamKey abc \
    --Properties.0.ParamValue abc \
    --Description abc
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

