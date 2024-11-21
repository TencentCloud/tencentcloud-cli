**Example 1: 镜像仓库查询镜像高危行为列表**



Input: 

```
tccli tcss DescribeAssetImageRegistryRiskInfoList --cli-unfold-argument  \
    --Offset 0 \
    --Limit 10 \
    --Filters.0.Name Level \
    --Filters.0.Values all \
    --Filters.0.ExactMatch False \
    --Filters.1.Name Behavior \
    --Filters.1.Values all \
    --Filters.1.ExactMatch False \
    --Filters.2.Name Type \
    --Filters.2.Values all \
    --Filters.2.ExactMatch False \
    --Id 100078461
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "Behavior": 3,
                "Desc": "Dockerfile中环境变量包含密码",
                "InstructionContent": "2024-05-06 10:49:58\n/bin/sh -c #(nop)  ENV ROOTPASSWD=2473",
                "Level": "3",
                "Type": 2
            },
            {
                "Behavior": 3,
                "Desc": "Dockerfile中环境变量包含密码",
                "InstructionContent": "2024-05-06 10:50:10\n/bin/sh -c #(nop)  ENV ROOTPASSWD=17666",
                "Level": "3",
                "Type": 2
            },
            {
                "Behavior": 3,
                "Desc": "Dockerfile中环境变量包含密码",
                "InstructionContent": "2024-05-06 10:50:08\n/bin/sh -c #(nop)  ENV ROOTPASSWD=17065",
                "Level": "3",
                "Type": 2
            },
            {
                "Behavior": 3,
                "Desc": "Dockerfile中环境变量包含密码",
                "InstructionContent": "2024-05-06 10:50:05\n/bin/sh -c #(nop)  ENV ROOTPASSWD=20419",
                "Level": "3",
                "Type": 2
            },
            {
                "Behavior": 3,
                "Desc": "Dockerfile中环境变量包含密码",
                "InstructionContent": "2024-05-06 10:50:03\n/bin/sh -c #(nop)  ENV ROOTPASSWD=6079",
                "Level": "3",
                "Type": 2
            },
            {
                "Behavior": 3,
                "Desc": "Dockerfile中环境变量包含密码",
                "InstructionContent": "2024-05-06 10:50:00\n/bin/sh -c #(nop)  ENV ROOTPASSWD=31991",
                "Level": "3",
                "Type": 2
            },
            {
                "Behavior": 3,
                "Desc": "Dockerfile中环境变量包含密码",
                "InstructionContent": "2024-05-06 10:49:53\n/bin/sh -c #(nop)  ENV ROOTPASSWD=19826",
                "Level": "3",
                "Type": 2
            },
            {
                "Behavior": 3,
                "Desc": "Dockerfile中环境变量包含密码",
                "InstructionContent": "2024-05-06 10:49:49\n/bin/sh -c #(nop)  ENV ROOTPASSWD=25831",
                "Level": "3",
                "Type": 2
            },
            {
                "Behavior": 3,
                "Desc": "Dockerfile中环境变量包含密码",
                "InstructionContent": "2024-05-06 10:49:51\n/bin/sh -c #(nop)  ENV ROOTPASSWD=19978",
                "Level": "3",
                "Type": 2
            },
            {
                "Behavior": 3,
                "Desc": "Dockerfile中环境变量包含密码",
                "InstructionContent": "2024-05-06 10:50:12\n/bin/sh -c #(nop)  ENV ROOTPASSWD=4883",
                "Level": "3",
                "Type": 2
            }
        ],
        "RequestId": "1c23b3e4-ea15-4705-990d-fe63890dc992",
        "TotalCount": 658
    }
}
```

