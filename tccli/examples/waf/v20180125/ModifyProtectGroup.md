**Example 1: 编辑防护对象组**



Input: 

```
tccli waf ModifyProtectGroup --cli-unfold-argument  \
    --GroupId 11101 \
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

