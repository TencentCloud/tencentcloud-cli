**Example 1: 获取addon列表**

获取一个或多个addon列表

Input: 

```
tccli tke DescribeAddon --cli-unfold-argument  \
    --ClusterId cls-kihzth22 \
    --AddonName cbs
```

Output: 
```
{
    "Response": {
        "Addons": [
            {
                "AddonName": "cbs",
                "AddonVersion": "1.1.7",
                "CreateTime": "2024-12-23T13:06:44Z",
                "Phase": "Succeeded",
                "RawValues": "e30=",
                "Reason": ""
            }
        ],
        "RequestId": "7eb2cf94-6cc3-40d0-8843-3ac1314e61e5"
    }
}
```

