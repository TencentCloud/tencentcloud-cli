**Example 1: 查询全部接入点列表**

此场景为查询全部接入点列表

Input: 

```
tccli mna DescribeAccessPointList --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "AccessPointList": [
            {
                "Available": true,
                "BigArea": "CN",
                "GwGroupId": "devGrp-2evt2qy*****",
                "PublicAddr": "49.233.112.***:443",
                "Region": "ap-beijing",
                "Vendor": "CHINA_TELECOM"
            }
        ],
        "RequestId": "4957c0d9-ddc6-460c-9ee2-a56f9e4f7173"
    }
}
```

**Example 2: 查询指定地域接入点列表**

此场景为查询指定地域接入点列表

Input: 

```
tccli mna DescribeAccessPointList --cli-unfold-argument  \
    --Regions ap-beijing
```

Output: 
```
{
    "Response": {
        "AccessPointList": [
            {
                "Available": true,
                "BigArea": "CN",
                "GwGroupId": "devGrp-2evt2qyd****",
                "PublicAddr": "49.233.112.***:443",
                "Region": "ap-beijing",
                "Vendor": "CHINA_TELECOM"
            }
        ],
        "RequestId": "5883dde6-d0ef-4519-b6a2-6875457f3120"
    }
}
```

