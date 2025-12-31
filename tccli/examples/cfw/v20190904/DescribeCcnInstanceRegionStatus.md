**Example 1: 查询CCN关联实例的地域引流网络状态**

输入CcnId和要查询的实例ID列表

Input: 

```
tccli cfw DescribeCcnInstanceRegionStatus --cli-unfold-argument  \
    --CcnId ccn-iidlg5oh \
    --InstanceIds vpc-p9qzo51x
```

Output: 
```
{
    "Response": {
        "RegionFwStatus": [
            {
                "Cidr": "",
                "Region": "na-siliconvalley",
                "Status": "NotDeployed"
            }
        ],
        "Total": 1,
        "RequestId": "bfc1cf67-5f2f-4253-864f-03be3d69777c"
    }
}
```

**Example 2: 查询CCN关联实例的地域引流网络状态（实例ID列表为空）**

输入CcnId和要查询，实例ID列表为空则默认获取所有关联地域状态

Input: 

```
tccli cfw DescribeCcnInstanceRegionStatus --cli-unfold-argument  \
    --CcnId ccn-iidlg5oh
```

Output: 
```
{
    "Response": {
        "RegionFwStatus": [
            {
                "Cidr": "",
                "Region": "na-siliconvalley",
                "Status": "NotDeployed"
            }
        ],
        "Total": 2,
        "RequestId": "61b6a85c-dff4-4b28-9349-160037582096"
    }
}
```

