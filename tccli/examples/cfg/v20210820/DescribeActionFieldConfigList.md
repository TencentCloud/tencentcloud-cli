**Example 1: 示例**



Input: 

```
tccli cfg DescribeActionFieldConfigList --cli-unfold-argument  \
    --ObjectTypeId 1 \
    --ActionIds 1
```

Output: 
```
{
    "Response": {
        "RequestId": "f3433a9a-e8fd-40b9-88e7-dd8b3f1a181f",
        "Common": [
            {
                "ActionId": 1,
                "ActionName": "关机",
                "ConfigDetail": [
                    {
                        "Type": "number",
                        "Lable": "动作超时时间(s)",
                        "Field": "ActionTimeout",
                        "DefaultValue": "1800",
                        "Config": "{\"max\": 86400, \"min\": 0, \"tooltip\": \"动作的超时时间\"}",
                        "Required": 1,
                        "Validate": "{\"op\": \"==\", \"value\": \"指定个数重启\", \"relatedField\": \"reboot_mod\"}",
                        "Visible": "{\"op\": \"<\", \"type\": \"need_insert\", \"value\": 0, \"relatedField\": \"ActionTimeout\"}"
                    }
                ]
            }
        ],
        "Results": []
    }
}
```

