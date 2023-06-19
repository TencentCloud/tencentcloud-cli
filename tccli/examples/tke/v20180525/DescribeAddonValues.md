**Example 1: 获取addon的参数**

获取一个addon的参数

Input: 

```
tccli tke DescribeAddonValues --cli-unfold-argument  \
    --ClusterId cls-123deabc \
    --AddonName eniipamd
```

Output: 
```
{
    "Response": {
        "Values": "",
        "DefaultValues": "",
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

