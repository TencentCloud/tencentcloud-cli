**Example 1: 示例**

示例

Input: 

```
tccli clouddc GetTreeNodeInfoByCodes --cli-unfold-argument  \
    --Codes abc
```

Output: 
```
{
    "Response": {
        "NodeInfoList": [
            {
                "Code": "abc",
                "CenterIds": [
                    0
                ],
                "DepartmentIds": [
                    0
                ],
                "Level": 0,
                "Managers": [
                    "abc"
                ],
                "Name": "abc",
                "Status": 0,
                "Version": 0
            }
        ],
        "RequestId": "abc"
    }
}
```

