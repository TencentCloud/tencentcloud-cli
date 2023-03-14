**Example 1: 根据域名查UIN**

根据域名查UIN

Input: 

```
tccli dnspod DescribeUinByDomain --cli-unfold-argument  \
    --Domain xx.com
```

Output: 
```
{
    "Response": {
        "RequestId": "712d3b96-9d12-4c43-972c-7880b5c795c0",
        "Uin": 11101101101
    }
}
```

