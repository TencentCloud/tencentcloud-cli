**Example 1: 查询用户可使用的专属可用区列表**



Input: 

```
tccli cdz DescribeUserAvailableCloudDedicatedZones --cli-unfold-argument  \
    --CheckUin 700000775535 \
    --RegionId 1
```

Output: 
```
{
    "Response": {
        "ZoneIdSet": [
            "100001"
        ],
        "RequestId": "fa1ec983-3f83-4353-9ae7-1bd7aa60d77c"
    }
}
```

