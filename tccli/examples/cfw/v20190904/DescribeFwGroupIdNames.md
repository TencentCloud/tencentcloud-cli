**Example 1: 查询防火墙组ID 名称**

查询防火墙组ID 名称

Input: 

```
tccli cfw DescribeFwGroupIdNames --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "FwGroupId": "cfwg-xxsddsa",
                "FwGroupName": "新防火墙"
            }
        ],
        "RequestId": "xxxxxxxxxx"
    }
}
```

