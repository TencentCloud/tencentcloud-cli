**Example 1: 查询跨地域备份的目标地域**



Input: 

```
tccli sqlserver DescribeCrossRegions --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Regions": [
            "ap-beijing",
            "ap-shanghai",
            "ap-taipei",
            "ap-hongkong",
            "ap-beijing-fsi",
            "ap-shanghai-fsi",
            "ap-shenzhen-fsi"
        ],
        "RequestId": "1373db1a-efd7-11ec-a46f-525400853186"
    }
}
```

