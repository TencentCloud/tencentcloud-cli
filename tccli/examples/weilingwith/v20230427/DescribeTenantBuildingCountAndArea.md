**Example 1: 查询租户楼栋数量和楼栋建筑面积**

查询租户楼栋数量和楼栋建筑面积成功响应示例

Input: 

```
tccli weilingwith DescribeTenantBuildingCountAndArea --cli-unfold-argument  \
    --WorkspaceIdList 1015 1016 1018 \
    --ApplicationToken ZRCJHdnhqEUEqO1vyskCgWimPucHhREV
```

Output: 
```
{
    "Response": {
        "RequestId": "44e3188a-67a3-4a92-8e7b-517459c29816",
        "Result": {
            "BuildingArea": 202928.77732501808,
            "BuildingCount": 137
        }
    }
}
```

**Example 2: 查询租户楼栋数量和楼栋建筑面积示例-prod**

查询租户楼栋数量和楼栋建筑面积示例-prod

Input: 

```
tccli weilingwith DescribeTenantBuildingCountAndArea --cli-unfold-argument  \
    --WorkspaceIdList 1124 1133 \
    --ApplicationToken Sl5ZDmVuHzhN52o8n1KWagl7sLdrLfN7
```

Output: 
```
{
    "Response": {
        "RequestId": "fa570973-a1d2-4fbc-807e-a0546d7819cc",
        "Result": {
            "BuildingArea": 682550.335429272,
            "BuildingCount": 239
        }
    }
}
```

