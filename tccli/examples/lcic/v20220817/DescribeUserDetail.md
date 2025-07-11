**Example 1: DescribeUserDetail**



Input: 

```
tccli lcic DescribeUserDetail --cli-unfold-argument  \
    --UserId 2jatnsjdosdnjuT8l60980Rh50FP \
    --OriginId teacher8383
```

Output: 
```
{
    "Response": {
        "RequestId": "865810-31a6-4378-a6ea-d9b719552",
        "Users": [
            {
                "Avatar": "",
                "Name": "teacher8383",
                "OriginId": "teacher8383",
                "SdkAppId": 39234193,
                "UserId": "2jatnsjdosdnjuT8l60980Rh50FP"
            }
        ]
    }
}
```

