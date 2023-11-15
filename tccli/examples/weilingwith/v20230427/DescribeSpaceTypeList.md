**Example 1: 查询空间分类**

查询空间分类成功响应示例

Input: 

```
tccli weilingwith DescribeSpaceTypeList --cli-unfold-argument  \
    --WorkspaceId 1016 \
    --PageNumber 1 \
    --PageSize 10 \
    --ApplicationToken ZRCJHdnhqEUEqO1vyskCgWimPucHhREV
```

Output: 
```
{
    "Response": {
        "RequestId": "dbb6362d-4e7c-459f-a6e9-ecef04842722",
        "Result": {
            "SpaceTypeList": [
                {
                    "SpaceTypeCode": "CESHILEIXING",
                    "SpaceTypeName": "测试类型"
                },
                {
                    "SpaceTypeCode": "HAHAHA",
                    "SpaceTypeName": "哈哈哈"
                }
            ]
        }
    }
}
```

**Example 2: 查询空间分类示例-prod**

查询空间分类示例-prod

Input: 

```
tccli weilingwith DescribeSpaceTypeList --cli-unfold-argument  \
    --WorkspaceId 1124 \
    --PageNumber 1 \
    --PageSize 10 \
    --ApplicationToken Sl5ZDmVuHzhN52o8n1KWagl7sLdrLfN7
```

Output: 
```
{
    "Response": {
        "RequestId": "21770e5e-a17e-4023-8cc9-51129f6cd37a",
        "Result": {
            "SpaceTypeList": [
                {
                    "SpaceTypeCode": "DIANTIJIAN",
                    "SpaceTypeName": "电梯间"
                },
                {
                    "SpaceTypeCode": "LOUTIJIAN",
                    "SpaceTypeName": "楼梯间"
                },
                {
                    "SpaceTypeCode": "WODEFANGJIAN",
                    "SpaceTypeName": "我的房间"
                },
                {
                    "SpaceTypeCode": "XIUXISHI",
                    "SpaceTypeName": "休息室"
                }
            ]
        }
    }
}
```

