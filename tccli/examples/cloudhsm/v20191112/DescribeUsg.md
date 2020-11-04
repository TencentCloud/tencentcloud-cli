**Example 1: 获取用户安全组列表**

获取用户安全组列表

Input: 

```
tccli cloudhsm DescribeUsg --cli-unfold-argument  \
    --Offset 0\
    --Limit 10
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "SgList": [
            {
                "SgId": "SgIdxxxxx",
                "SgName": "SgNamexxxxxx"
            }
        ],
        "RequestId": "6010cd3d-a85a-4e00-b37b-22606d017420"
    }
}
```

