**Example 1: 获取各主机漏洞防御插件状态**

获取各主机漏洞防御插件状态

Input: 

```
tccli cwp DescribeVulDefencePluginStatus --cli-unfold-argument  \
    --Order desc \
    --By CreateTime \
    --Offset 0 \
    --Limit 10 \
    --Filters.0.Name Exception \
    --Filters.0.Values 1 \
    --Filters.0.ExactMatch False
```

Output: 
```
{
    "Response": {
        "List": [
            {
                "Quuid": "f3076bef-0fdf-44f4-bb63-b5232e13e167",
                "Alias": "machinename",
                "PrivateIp": "10.0.1.2",
                "PublicIp": "43.139.183.147",
                "Exception": 1,
                "CreateTime": "2024-09-04 10:55:34",
                "ModifyTime": "2024-11-03 16:26:33"
            }
        ],
        "RequestId": "1a2eba98-7a6f-4798-9724-d774c5172044",
        "TotalCount": 1
    }
}
```

