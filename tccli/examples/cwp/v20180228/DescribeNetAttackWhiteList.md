**Example 1: 获取网络攻击白名单列表**

获取网络攻击白名单列表

Input: 

```
tccli cwp DescribeNetAttackWhiteList --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "c0a212e9-c598-4a2b-889f-5bc305f2e39f",
        "TotalCount": 1,
        "WhiteList": [
            {
                "CreateTime": "2023-05-22 18:38:24",
                "DealOldEvents": 0,
                "Description": "",
                "Id": 10001,
                "ModifyTime": "2023-05-22 18:43:16",
                "Quuids": "05f0bcab-726c-4ea4-8109-bcd03d5598f7",
                "Scope": 0,
                "SrcIP": "1.2.3.4;1.1.1.2-1.1.1.4;1.2.3.0/24"
            }
        ]
    }
}
```

