**Example 1: 查询置放群组配额**



Input: 

```
tccli dbdc DescribeDBCustomDisasterRecoverGroupQuota --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "CurrentNum": 1,
        "GroupQuota": 50,
        "NodeInHostGroupQuota": 50,
        "RequestId": "204a6569-ff99-4433-8b68-4640fd62e802"
    }
}
```

