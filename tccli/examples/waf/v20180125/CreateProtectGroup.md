**Example 1: 新建防护对象组**



Input: 

```
tccli waf CreateProtectGroup --cli-unfold-argument  \
    --Name group name \
    --Remark group remark \
    --Domains www.testwaf1.com www.testwaf2.com
```

Output: 
```
{
    "Response": {
        "GroupId": 55201922,
        "RequestId": "xxxx"
    }
}
```

