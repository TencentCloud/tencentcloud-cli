**Example 1: 新增漏洞误报信息**

将漏洞标记为误报

Input: 

```
tccli cws CreateVulsMisinformation --cli-unfold-argument  \
    --VulIds 1
```

Output: 
```
{
    "Response": {
        "RequestID": "354f4ac3-8546-4516-8c8a-69e3ab73aa8a"
    }
}
```

