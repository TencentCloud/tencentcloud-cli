**Example 1: 查询终端节点可用地域**

查询终端节点可用地域

Input: 

```
tccli privatedns DescribeEndPointRegion --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RegionSet": [
            {
                "CnName": "北京",
                "EnName": "bj",
                "RegionCode": "ap-beijing",
                "RegionId": 8
            },
            {
                "CnName": "广州",
                "EnName": "gz",
                "RegionCode": "ap-guangzhou",
                "RegionId": 1
            },
            {
                "CnName": "南京",
                "EnName": "nj",
                "RegionCode": "ap-nanjing",
                "RegionId": 33
            },
            {
                "CnName": "上海",
                "EnName": "sh",
                "RegionCode": "ap-shanghai",
                "RegionId": 4
            }
        ],
        "RequestId": "036e44eb-02af-44cf-b46e-924a0e04ea4a"
    }
}
```

