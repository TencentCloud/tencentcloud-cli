**Example 1: 查询用户可使用的专属可用区列表**



Input: 

```
tccli cdz DescribeUserAvailableCloudDedicatedZones --cli-unfold-argument  \
    --CheckUin abc \
    --RegionId 1
```

Output: 
```
{
    "Response": {
        "ZoneIdSet": [
            "123"
        ],
        "RequestId": "123"
    }
}
```

