**Example 1: 查询地域列表**

此接口用于查询 TAT 产品后台地域列表。 RegionState 为 AVAILABLE，代表该地域的 TAT 后台服务已经可用；未返回，代表该地域的 TAT 后台服务尚不可用

Input: 

```
tccli tat DescribeRegions --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "TotalCount": 13,
        "RegionSet": [
            {
                "Region": "ap-guangzhou",
                "RegionName": "广州",
                "RegionState": "AVAILABLE"
            },
            {
                "Region": "ap-nanjing",
                "RegionName": "南京",
                "RegionState": "AVAILABLE"
            },
            {
                "Region": "ap-shanghai",
                "RegionName": "上海",
                "RegionState": "AVAILABLE"
            },
            {
                "Region": "ap-hongkong",
                "RegionName": "中国香港",
                "RegionState": "AVAILABLE"
            },
            {
                "Region": "ap-beijing",
                "RegionName": "北京",
                "RegionState": "AVAILABLE"
            },
            {
                "Region": "ap-singapore",
                "RegionName": "新加坡",
                "RegionState": "AVAILABLE"
            },
            {
                "Region": "na-siliconvalley",
                "RegionName": "硅谷",
                "RegionState": "AVAILABLE"
            },
            {
                "Region": "ap-chengdu",
                "RegionName": "成都",
                "RegionState": "AVAILABLE"
            },
            {
                "Region": "eu-frankfurt",
                "RegionName": "法兰克福",
                "RegionState": "AVAILABLE"
            },
            {
                "Region": "ap-seoul",
                "RegionName": "首尔",
                "RegionState": "AVAILABLE"
            },
            {
                "Region": "ap-chongqing",
                "RegionName": "重庆",
                "RegionState": "AVAILABLE"
            },
            {
                "Region": "ap-mumbai",
                "RegionName": "孟买",
                "RegionState": "AVAILABLE"
            }
        ],
        "RequestId": "6fb7f9db-b7da-4cb8-a912-3a3b1690f3a6"
    }
}
```

