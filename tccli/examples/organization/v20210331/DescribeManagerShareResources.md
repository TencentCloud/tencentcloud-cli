**Example 1: 获取我的共享资源列表**



Input: 

```
tccli organization DescribeManagerShareResources --cli-unfold-argument  \
    --Area guangzhou \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "Items": [
            {
                "CreateTime": "2021-03-06 17:11:30",
                "ResourceId": "shareResource-kfgfrd2e3xx",
                "ProductResourceId": "subnet-ewd23dd",
                "SharedMemberNum": 0,
                "Type": "subnet",
                "UnitId": "shareUnit-xhreofra2p",
                "UnitName": "",
                "SharedMemberUseNum": 0
            }
        ],
        "RequestId": "2d82212e-63f5-4d1f-b703-d27122c4ea35",
        "Total": 1
    }
}
```

