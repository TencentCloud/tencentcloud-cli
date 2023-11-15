**Example 1: 查询项目空间楼栋数量与建筑面积**

查询项目空间楼栋数量与建筑面积成功响应示例

Input: 

```
tccli weilingwith DescribeWorkSpaceBuildingCountAndArea --cli-unfold-argument  \
    --WorkspaceIdList 1016 1015 1018 \
    --ApplicationToken fquCgDi2QfNDMlNyQ5YPoMR2Zw4tQs2B
```

Output: 
```
{
    "Response": {
        "RequestId": "42569a1b-01e1-4064-9288-b89ad76d55b7",
        "Result": {
            "List": [
                {
                    "BuildingArea": 0,
                    "BuildingCount": 2,
                    "WorkspaceId": "1018",
                    "WorkspaceName": "华北园区项目"
                },
                {
                    "BuildingArea": 202928.77732501808,
                    "BuildingCount": 127,
                    "WorkspaceId": "1016",
                    "WorkspaceName": "华南园区项目"
                },
                {
                    "BuildingArea": 0,
                    "BuildingCount": 8,
                    "WorkspaceId": "1015",
                    "WorkspaceName": "公共空间"
                }
            ]
        }
    }
}
```

**Example 2: 查询项目空间楼栋数量与建筑面积示例-prod**

查询项目空间楼栋数量与建筑面积-prod

Input: 

```
tccli weilingwith DescribeWorkSpaceBuildingCountAndArea --cli-unfold-argument  \
    --WorkspaceIdList 1124 1133 \
    --ApplicationToken Sl5ZDmVuHzhN52o8n1KWagl7sLdrLfN7
```

Output: 
```
{
    "Response": {
        "RequestId": "94a7a0d6-b2d4-4da7-a39d-ed79489e09c2",
        "Result": {
            "List": [
                {
                    "BuildingArea": 35990.08433069048,
                    "BuildingCount": 141,
                    "WorkspaceId": "1124",
                    "WorkspaceName": "测试空间"
                },
                {
                    "BuildingArea": 646560.2510985816,
                    "BuildingCount": 98,
                    "WorkspaceId": "1133",
                    "WorkspaceName": "体验项目空间"
                }
            ]
        }
    }
}
```

