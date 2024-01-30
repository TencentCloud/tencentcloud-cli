**Example 1: 获取探测节点列表**

获取探测节点列表

Input: 

```
tccli igtm DescribeDetectors --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "xxx",
        "DetectorGroupSet": [
            {
                "Gid": 30,
                "InternetFamily": "ipv4",
                "GroupType": "bgp",
                "GroupName": "广州",
                "PackageSet": [
                    "FREE",
                    "STANDARD",
                    "ULTIMATE"
                ]
            }
        ]
    }
}
```

