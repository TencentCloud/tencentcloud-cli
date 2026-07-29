**Example 1: 查询当前地域的支持亲和性等级设置的专区列表**



Input: 

```
tccli cynosdb DescribeClusterLevels --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "LevelList": [
            "L1"
        ],
        "Zones": [
            "ap-guangzhou-3"
        ],
        "RequestId": "9db131da-3bd7-4d0f-980e-db3899e38aea"
    }
}
```

