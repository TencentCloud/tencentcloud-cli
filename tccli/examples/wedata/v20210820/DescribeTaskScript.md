**Example 1: 查询任务脚本范例**

查询任务脚本

Input: 

```
tccli wedata DescribeTaskScript --cli-unfold-argument  \
    --ProjectId 1 \
    --TaskId 20220727140613327
```

Output: 
```
{
    "Response": {
        "RequestId": "3100df93-5da5-45d1-b06b-dd08612f8224",
        "Data": {
            "ScriptContent": "[note: BASE64 encoding] #!/bin/bash\n#******************************************************************#\n##author: TBDS\n##create time: 2022-07-27 14:06:13\n#******************************************************************#\necho \"222\""
        }
    }
}
```

