**Example 1: 查询用户继承自虚拟组的资源**

查询用户继承自虚拟组的资源

Input: 

```
tccli ioa DescribeAccountVirtualGroupResources --cli-unfold-argument  \
    --AccountId 928507
```

Output: 
```
{
    "Response": {
        "Data": {
            "Items": []
        },
        "RequestId": "038100f6-4570-461b-871e-ce2d93217eb2"
    }
}
```

