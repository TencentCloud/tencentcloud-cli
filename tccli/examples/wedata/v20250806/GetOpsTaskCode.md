**Example 1: 获取任务代码（生产态）**



Input: 

```
tccli wedata GetOpsTaskCode --cli-unfold-argument  \
    --ProjectId 1460947878944567296 \
    --TaskId 20241219152335518
```

Output: 
```
{
    "Response": {
        "RequestId": "dc46283a-b493-48c5-a7c1-2c9d14b31f35",
        "Data": {
            "CodeContent": "#!/bin/bash\n#******************************************************************#\n##author: test_user\n##create time: 2024-12-19 15:23:31\n#******************************************************************#\necho \"abc\"",
            "CodeFileSize": 213
        }
    }
}
```

