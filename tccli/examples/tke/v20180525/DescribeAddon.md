**Example 1: 获取addon列表**

获取一个或多个addon列表

Input: 

```
tccli tke DescribeAddon --cli-unfold-argument  \
    --ClusterId cls-123deabc \
    --AddonName cbs
```

Output: 
```
{
    "Response": {
        "Addons": [
            {
                "AddonName": "cbs",
                "AddonVersion": "1.1.0",
                "RawValues": ""
            }
        ],
        "RequestId": "abc"
    }
}
```

