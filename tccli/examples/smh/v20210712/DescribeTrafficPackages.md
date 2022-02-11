**Example 1: 查询官方实例**



Input: 

```
tccli smh DescribeTrafficPackages --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "List": [
            {
                "InstanceId": "jexrwwoa",
                "Domain": "jexrwwoa.cofile.net",
                "Type": 0,
                "Size": "107374182400",
                "SizeGB": 100,
                "Remain": "89017835619",
                "Used": "18356346781",
                "UsedPercentage": "17.10",
                "EffectiveTime": "2021-10-12T03:53:29Z",
                "ExpireTime": "2021-11-12T15:59:59Z"
            }
        ],
        "TotalCount": 1,
        "RequestId": "27ec9933-ad39-46b0-9ea1-f863a89dd00c"
    }
}
```

