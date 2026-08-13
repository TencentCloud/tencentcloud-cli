**Example 1: 查询容器资产EDR告警**



Input: 

```
tccli csip DescribeEdrAlertCountForContainer --cli-unfold-argument  \
    --ContainerIds 058282413b99b87b10b4c24ab353db46d72b72deba2490969758296b54743676
```

Output: 
```
{
    "Response": {
        "Items": [
            {
                "ClusterId": "",
                "ContainerId": "058282413b99b87b10b4c24ab353db46d72b72deba2490969758296b54743676",
                "TotalCount": 27
            }
        ],
        "RequestId": "2d310e41-4d29-46dc-92da-80e91b96f242"
    }
}
```

