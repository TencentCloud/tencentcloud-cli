**Example 1: 获取上网拦截网址分类**

获取上网拦截网址分类

Input: 

```
tccli ioa DescribeInternetBlockingUrlCategories --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "Id": 0,
                "CategoryId": "abc",
                "CategoryName": "abc",
                "HostCount": 0
            }
        ],
        "RequestId": "abc"
    }
}
```

