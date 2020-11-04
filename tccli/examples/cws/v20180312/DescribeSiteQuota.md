**Example 1: 查看站点购买配额**

查询用户购买的站点总数和已使用数

Input: 

```
tccli cws DescribeSiteQuota --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Available": 16,
        "RequestId": "354f4ac3-8546-4516-8c8a-69e3ab73aa8a",
        "Total": 20,
        "Used": 4
    }
}
```

