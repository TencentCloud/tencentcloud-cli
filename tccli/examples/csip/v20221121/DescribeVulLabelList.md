**Example 1: 获取漏洞标签列表**

获取漏洞标签列表

Input: 

```
tccli csip DescribeVulLabelList --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "List": [
            {
                "Level": "CRITICAL",
                "Name": "应急漏洞",
                "Remark": "被人为标记为应急漏洞"
            }
        ],
        "RequestId": "39b78e13-550d-4606-a957-f690ccd2b903"
    }
}
```

